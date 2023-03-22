"""
Refer: https://towardsdatascience.com/raft-algorithm-explained-a7c856529f40
"""

import time
import logging
import random
import append_entries as ae
import curio
import term

STATE_MACHINE = {
    'initial': {
        'condition': ['startup'],
        'startup': 'follower'  # next state
    },
    'follower': {
        'condition': ['timeout_f'],
        'timeout_f': 'candidate'  # next state
    },
    'candidate': {
        'condition': ['timeout_c', 'majority'],  # , 'majority', 'new_term', 'current_leader'],
        'timeout_c': 'leader',  # next state
        'majority': 'leader',  # next state
        'new_term': 'follower',  # next state
        'current_leader': 'follower'  # next state
    },
    'leader': {
        'condition': ['timeout_l'],  # ['discover_server_with_higher_term', 'crash', 'no_change'],
        'discover_server_with_higher_term': 'follower',  # next state
        'crash': 'follower',  # next state
        'no_change': 'leader', # next state
        'timeout_l': 'follower'
    }
}

logging = logging.getLogger()

class RaftState():

    def __init__(self, state='initial', port_number='25001'):
        self._current_state = state
        self.heart_beat = True # True means heart beat received from peers, False is reverse
        self.prepare_for_election = False
        self.majority_status = False
        self.term = term.Term(port_number)

    async def startup(self, timeout=5):
        logging.info("Inside timeout: startup")
        await curio.sleep(0)
        return 'follower'

    async def timeout_f(self, timeout=5):
        logging.info("Inside timeout: follower")
        await curio.sleep(5)
        if not self.heart_beat:
            return 'candidate'
        else:
            await self.timeout_f()

    async def majority(self, timeout=5):
        logging.info("Inside majority: leader")
        await curio.sleep(5)
        if self.majority:
            return 'leader'
        # else:
        #    await self.timeout_l()

    async def timeout_c(self, timeout=10):
        logging.info("Inside timeout: candidate")
        await curio.sleep(5)
        if self.majority:
            return 'leader'
        else:
            await self.timeout_c()


    async def timeout_l(self, timeout=5):
        logging.info("Inside timeout: leader")
        await curio.sleep(20)
        return 'follower'

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
            next_state = getattr(self, self._current_state)
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
        time.sleep(2)
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
        time.sleep(2)
        term = 0
        leader_id = 0
        entries = []
        prev_log_index = 0
        prev_log_term = 0
        leader_commit = 0
        return [term, leader_id, entries, prev_log_index, prev_log_term]

    def leader(self):
        logging.info("running as -> leader")
        # Construct message if you are leader
        #     'term',           # int		// current term of the leader, very IMPORTANT
        #     'leader_id',      # int		// id of the leader, 0 to N-1 where N = total servers
        #     'entries',        # [] Entry  // new data to sync
        #     'prev_log_index', # int		// important metadata for log correctness
        #     'prev_log_term',  # int		// important metadata for log correctness
        #     'leader_commit'   # int 	    // what index have been received by the majority
        time.sleep(2)
        term = 0
        leader_id = 0
        entries = []
        prev_log_index = 0
        prev_log_term = 0
        leader_commit = 0
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
        time.sleep(2)
        term = 0
        leader_id = 0
        entries = []
        prev_log_index = 0
        prev_log_term = 0
        leader_commit = 0
        return [term, leader_id, entries, prev_log_index, prev_log_term]

    def construct_send_message_based_on_current_state(self, server_obj=None):
        current_state = getattr(server_obj.role, '_current_state')
        logging.info(f"Constructing send message based on my role {current_state}")
        method_for_message = getattr(self, current_state)
        message_details = method_for_message()
        return ae.get_append_entry_args_list(*message_details)

    def construct_ack_message_based_on_current_state(self, server_obj=None):
        current_state = getattr(server_obj.role, '_current_state')
        logging.info(f"Constructing response message based on my role {current_state}")
        method_for_message = getattr(self, current_state)
        message_details = method_for_message()
        return ae.get_append_entry_args_list(*[0,0,0,0])

    def digest_message(self):
        pass


if __name__ == "__main__":

    raft_state_obj = RaftState()
    while True:
        raft_state_obj.iterate_state_machine()