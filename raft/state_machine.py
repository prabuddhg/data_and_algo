"""
Refer: https://towardsdatascience.com/raft-algorithm-explained-a7c856529f40
"""

import time
import logging
from random import *
import append_entries as ae
import curio
import term
from logging.config import fileConfig

# fileConfig("logging_config.ini", disable_existing_loggers=False)

STATE_MACHINE = {
    'initial': {
        'condition': ['startup'],
        'startup': 'follower'  # next state
    },
    'follower': {
        'condition': ['election_timer'],
        'election_timer': 'candidate'  # next state
    },
    'candidate': {
        'condition': ['timeout_c', 'majority'],  # , 'majority', 'new_term', 'current_leader'],
        'timeout_c': 'leader',  # next state
        'majority': 'leader',  # next state
        'new_term': 'follower',  # next state
        'current_leader': 'follower'  # next state
    },
    'leader': {
        'condition': ['discover_server_with_higher_term'],  # ['discover_server_with_higher_term', 'crash', 'no_change'],
        'discover_server_with_higher_term': 'follower',  # next state
    }
}

logging = logging.getLogger(__name__)

class RaftState():

    def __init__(self, state='initial', port_number='25001', server_number=1, io_queue=None):
        self._current_state = state
        self.heart_beat = True # True means heart beat received from peers, False is reverse
        self.prepare_for_election = False
        self.majority_status = 0
        self.port_number = port_number
        self.discover_server_with_higher_term_status = False
        self.term = term.Term(self.port_number)
        self.name = f"Server-{self.port_number}:"
        self.id = server_number
        self.io_queue = io_queue
        self.trigger_election = False
        logging.info(f"{self.name} state machine set with server number {self.id} initial state {self._current_state}")

    async def startup(self, timeout=5):
        logging.info(f"{self.name} is startup")
        await curio.sleep(0)
        return 'follower'

    async def election_timer(self, timeout=5):
        logging.info(f"{self.name} is follower election_timer will go off in {str(int(self.id)*5)}")
        # await curio.sleep(randint(1, 10))
        await curio.sleep(int(self.id)*5)
        if self.trigger_election:
            logging.info(f"{self.name} *********Election timer expired, prepare for candidacy*****")
            self.prepare_for_election = True
            return 'candidate'
        else:
            await self.election_timer()

    async def majority(self, timeout=5):
        logging.info(f"{self.name} checking for majority")
        await curio.sleep(int(self.id)*10)
        if self.majority_status > 1:
            logging.info(f"{self.name} Won the election, now leader")
            return 'leader'
        # else:
        #    await self.timeout_l()

    async def timeout_c(self, timeout=10):
        logging.info(f"{self.name} No response, may be peers are offline, lets become leader")
        await curio.sleep(int(self.id)*10)
        if not self.heart_beat:
            return 'leader'
        else:
            await self.timeout_c()


    async def discover_server_with_higher_term(self, timeout=5):
        logging.info(f"{self.name} checking for another server with higher term")
        await curio.sleep(int(self.id)*10)
        if self.discover_server_with_higher_term_status:
            return 'follower'
        else:
            if self._current_state == 'leader':
                logging.info(f"{self.name} Still Leader!!!")
            else:
                raise RuntimeError("Something not right, please check")
            await self.discover_server_with_higher_term()

    async def iterate_state_machine(self):
        while True:
            await curio.sleep(1)
            current_state = self._current_state
            current_state_condition_list = STATE_MACHINE[current_state]['condition']
            next_state = await self.find_conditions(current_state_condition_list)
            # next_condition = self.find_conditions(current_state_condition_list)
            # import pdb;pdb.set_trace()
            # self._current_state = STATE_MACHINE[current_state][next_condition]
            self._current_state = next_state
            try:
                next_state = getattr(self, self._current_state)
            except Exception as e:
                import pdb;pdb.set_trace() # -->
            next_state()

    async def find_conditions(self, current_state_condition_list):
        async with curio.TaskGroup(wait=any) as g:
            for i in current_state_condition_list:
                method_i = getattr(self, i)
                logging.info(f"Spawning {i}")
                await g.spawn(method_i())
        next_condition = g.result
        # next_condition = random.choice(current_state_condition_list)
        logging.info(f"found next condition! {next_condition}")
        return next_condition

    def follower(self):
        logging.info("running as -> follower")
        # Construct message if you are follower
        #     'term',           # int		// current term of the leader, very IMPORTANT
        #     'leader_id',      # int		// id of the leader, 0 to N-1 where N = total servers
        #     'entries',        # [] Entry  // new data to sync
        #     'prev_log_index', # int		// important metadata for log correctness
        #     'prev_log_term',  # int		// important metadata for log correctness
        #     'leader_commit'   # int 	    // what index have been received by the majority
        #     'server-id'       # int       // for debugging :-)
        latest_term_tuple = self.term.get_latest_term_tuple()
        if latest_term_tuple in ['', None, 0]:
            #      [term, leader_id, entries, prev_log_index, prev_log_term, self.id]
            ret_msg = [self.term._term, 0, [], 0, 0, self.id]
            logging.info(f"{self.name} current term={ret_msg}")
            return [self.term._term, 0, [], 0, 0, self.id]
        latest_term_tuple.append(self.id)
        logging.info(f"{self.name} current term={latest_term_tuple}")
        # latest_term_tuple will help us extract term, leader_id, prev_log_index, prev_log_term
        term, leader_id, entries, prev_log_index, prev_log_term = latest_term_tuple.split(',')
        return [term, leader_id, entries, prev_log_index, prev_log_term]

    def candidate(self):
        logging.info("running as -> candidate")
        # Construct message if you are candidate
        #     'term',           # int		// current term of the leader, very IMPORTANT
        #     'leader_id',      # int		// id of the leader, 0 to N-1 where N = total servers
        #     'entries',        # [] Entry  // new data to sync
        #     'prev_log_index', # int		// important metadata for log correctness
        #     'prev_log_term',  # int		// important metadata for log correctness
        #     'leader_commit'   # int 	    // what index have been received by the majority
        term = self.term._term + 1
        leader_id = self.id
        prev_log_index = 0
        prev_log_term = 0
        leader_commit = 0
        latest_term_tuple = [term, leader_id, prev_log_index, prev_log_term, leader_commit]
        logging.info(f"{self.name} current term={latest_term_tuple}")
        return latest_term_tuple

    def leader(self):
        logging.info("{self.name} running as -> leader")
        # Construct message if you are leader
        #     'term',           # int		// current term of the leader, very IMPORTANT
        #     'leader_id',      # int		// id of the leader, 0 to N-1 where N = total servers
        #     'entries',        # [] Entry  // new data to sync
        #     'prev_log_index', # int		// important metadata for log correctness
        #     'prev_log_term',  # int		// important metadata for log correctness
        #     'leader_commit'   # int 	    // what index have been received by the majority
        term = 0
        leader_id = 0
        entries = []
        prev_log_index = 0
        prev_log_term = 0
        leader_commit = 0
        return [term, leader_id, entries, prev_log_index, prev_log_term]



    def construct_send_message_based_on_current_state(self):
        current_state = getattr(self, '_current_state')
        logging.info(f"{self.name} Constructing send message based on my role {current_state}")
        method_for_message = getattr(self, current_state)
        message_details = method_for_message()
        append_entry_message = ae.get_append_entry_args_list(*message_details)
        logging.info(f"{self.name} ready to send append_message {append_entry_message}")
        return append_entry_message

    def construct_ack_message_based_on_current_state(self):
        current_state = getattr(self, '_current_state')
        logging.info(f"{self.name} Constructing response message based on my role {current_state}")
        method_for_message = getattr(self, current_state)
        message_details = method_for_message()
        ack_message = ae.get_append_entry_reply_list(*message_details)
        logging.info(f"{self.name} ready to send ack_message {ack_message}")
        return ack_message

    def digest_message(self, message=None, ack=False, initial=False):
        output_digest_message = None
        if message is not None and type(eval(message[2])) is list:
            append_entry_args_message = True
            if message[0] == '0' and message[1] == '0':
                logging.info(f"{self.name} No leader in this term, lets wait for elections")
                logging.info(f"{self.name} Releasing task for 10 seconds no responding")
                self.trigger_election = True
                output_digest_message = self.construct_send_message_based_on_current_state()
        if initial:
            logging.info(f"{self.name} Initial message")
            output_digest_message = self.construct_send_message_based_on_current_state()
        if ack:
            logging.info(f"{self.name} Ack message")
            output_digest_message = self.construct_ack_message_based_on_current_state()
        return output_digest_message


if __name__ == "__main__":

    raft_state_obj = RaftState()
    while True:
        raft_state_obj.iterate_state_machine()