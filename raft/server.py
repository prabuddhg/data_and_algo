from curio import run, \
    tcp_server, Lock, \
    TaskGroup, Queue, sleep, open_connection, run_in_process
import curio
import messages as msg
import argparse
import constants as const
import socket
import logging
from logging.config import fileConfig
import term
import state_machine as sm

fileConfig("logging_config.ini", disable_existing_loggers=False)
logging = logging.getLogger(__name__)

lock = Lock()
messages = Queue()
subscribers = set()

# https://stackoverflow.com/questions/62637871/using-delimiters-in-a-python-tcp-stream

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--server", dest="server", help="1 for server1, 2 for server 2"
    )
    # Parse and print the results
    args = parser.parse_args()
    return args


class RaftNode:
    def __init__(self, port_number, ip_address="127.0.0.1", peers=None, server_number=1):
        self.port_number = port_number
        self.ip_address = ip_address
        self.peers = peers
        self.term = term.Term(port_number)
        self.member_status = 'initial' # initial, follower, candidate, leader
        self.role = sm.RaftState(self.member_status)
        self.leader_id = None
        self.id = server_number

    async def dispatcher(self):
        while True:
            msg = await messages.get()
            for q in subscribers:
                await q.put(msg)

    async def connect_peers(self, peer, result_tcp=None):
        flag = True
        logging.info(f"Connecting with peer server-{peer} in cluster")
        while flag:
            try:
                conn_peer = await open_connection(self.ip_address, peer)
                logging.info(f"Preparing to add peer server-{peer} in cluster")
                # import pdb;pdb.set_trace()
                peer_message = self.role.construct_send_message_based_on_current_state(self)
                # peer_message = f"server-{self.port_number}"
                await conn_peer.sendall(peer_message.encode("utf-8"))
                flag = False
            except Exception as e:
                logging.warning(e)
                await sleep(5)
                logging.info(f"Retrying to add peer server-{peer} in cluster")
        logging.info(f"Added peer server-{peer} added in cluster")
        # finish this task and exit

        # do it here
        return True


    # Publisher
    async def publish(self, msg):
        await messages.put(msg)

    # Task that writes chat messages to clients
    async def outgoing(self, client_stream, name):
        queue = Queue()
        try:
            subscribers.add(queue)
            while True:
                name, msg = await queue.get()
                output = msg.encode("utf-8")
                logging.info(f"Sending {output} to {name}")
                if '-' in name:
                    peer = int(name.split('server-')[1])
                    conn_peer = await open_connection(self.ip_address, peer)
                    await sleep(2)
                    peer_message = self.role.construct_ack_message_based_on_current_state(self)
                    # await conn_peer.sendall(msg.encode("utf-8"))
                    await conn_peer.sendall(peer_message.encode("utf-8"))
        finally:
            subscribers.discard(queue)


    # task that reads chat messages and publishes them
    async def incoming(self, client_stream, name):
        async for line in client_stream:
            decoded_line = line.decode("utf-8").strip()
            logging.info(f"Received message {decoded_line} from name")
            if ":" in decoded_line:
                ret_msg = msg.process(decoded_line, self.port_number)
            await self.publish((name, ret_msg))


    # task that reads chat messages and publishes them
    async def peer_recovery_server(self, client_stream, name):
        logging.info("Server: Waiting for cluster to form")
        await sleep(10)
        logging.info(f"\n\nStarting recovery for peer {name}\n\n")
        all_executions = msg.recover_peers(self.port_number)
        for each_execution in all_executions:
            logging.info(f"Sync up execution: {each_execution}.. with peers")
            await self.publish((name, each_execution))
        # finish this task and exit
        return True

    async def chat_handler(self, client, addr):
        logging.info(f"Started TCP server at {self.port_number}")
        async with client:
            client_stream = client.as_stream()
            # while True:
            data = await client_stream.read(100000)
            #if not data:
            #    continue
            decoded_line = data.decode("utf-8").strip()
            if ':' in decoded_line:
                decoded_line = data.decode("utf-8").strip()
                logging.info(f"Replication in progress for data:{decoded_line} .. ")
                ret_msg = msg.process(decoded_line, self.port_number)
                if not ret_msg:
                    logging.info(f" Sync compete for :{decoded_line} .. ")
                # Step 1: use this flag to say all caught up
                # peer_message = self.role.construct_message_based_on_current_state(self)
            else:
                logging.info(f"Received request from peer {data} to join cluster")
            name = data.decode('utf-8')
            async with TaskGroup(wait=all) as workers:
                await workers.spawn(self.outgoing, client, name)
                await workers.spawn(self.incoming, client_stream, name)
                # await workers.spawn(self.peer_recovery_server, client_stream, name)

                # await publish((name, b"has gone away\n"))

        logging.info("Connection closed")

    async def chat_server(
        self,
    ):
        #msg.recover(self.port_number)
        async with TaskGroup() as g:
            result_tcp = await g.spawn(
                tcp_server, self.ip_address, self.port_number, self.chat_handler,
            )
            await g.spawn(self.dispatcher)
            # dependency here result_tcp is needed for connect_peers
            await g.spawn(self.connect_peers, self.peers[0], result_tcp)
            await g.spawn(self.connect_peers, self.peers[1], result_tcp)
            await g.spawn(self.role.iterate_state_machine())


if __name__ == "__main__":
    args = get_args()
    port_number, peers = const.get_port_number(args.server)
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except Exception as e:
        ip_address = '127.0.0.1'
    logging.info(
        f"Starting raft node {args.server} for ip {ip_address} on port {port_number} with peers {peers}"
    )
    raft_node = RaftNode(port_number, ip_address, peers, args.server)
    run(raft_node.chat_server(), with_monitor=True)
