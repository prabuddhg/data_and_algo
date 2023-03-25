from curio import run, \
    tcp_server, Lock, \
    TaskGroup, Queue, sleep, open_connection, run_in_process
import argparse
import constants as const
import socket
import logging
from logging.config import fileConfig
import state_machine as sm

fileConfig("logging_config.ini", disable_existing_loggers=False)
logging = logging.getLogger(__name__)

lock = Lock()
messages = Queue()
subscribers = set()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--server", dest="server", help="1 for server1, 2 for server 2"
    )
    args = parser.parse_args()
    return args


class RaftNode:
    def __init__(self, port_number, ip_address="127.0.0.1", peers=None, server_number=1, io_queue=None):
        self.port_number = port_number
        self.ip_address = ip_address
        self.peers = peers
        self.member_status = 'follower'  # follower, candidate, leader
        self.role = sm.RaftState(self.member_status, port_number, server_number, io_queue)
        self.leader_id = None
        self.id = server_number
        self.io_queue = io_queue

    async def dispatcher(self):
        while True:
            msg = await messages.get()
            for q in subscribers:
                await q.put(msg)

    async def heart_beat(self, peer, result_tcp=None):
        """
        Send the heart beats to peers and also corresponding msgs
        :param peer:
        :param result_tcp:
        :return:
        """
        flag = True
        logging.info(f"Connecting with peer server-{peer} in cluster")
        while flag:
            try:
                # Send message in HAPPY PATH
                conn_peer = await open_connection(self.ip_address, peer)
                logging.info(f"Received heart-beat from server-{peer}")
                self.role.heart_beat = True
                initial = False
                if self.member_status in ['follower']:
                    initial = True
                logging.info(f"Preparing to send heart-beat to server-{peer}")
                peer_message = self.role.digest_message(initial=initial)
                logging.info(f"Preparing to send {peer_message} heart-beat to server-{peer}")
                await conn_peer.sendall(peer_message.encode("utf-8"))
                flag = False
            except Exception as e:
                # Send mesaage in SAD PATH
                await sleep(1)
                logging.info(f"No heart-beat received from server-{peer}")
                self.role.heart_beat = False
                logging.info(f"Waiting to receive heart-beat from server-{peer}")

    # Publisher
    async def publish(self, msg):
        await messages.put(msg)

    # Task that writes chat messages to clients
    async def outgoing(self, client, name):
        """
        Read the data from the queue and send to
        relevant server via heart_beat()
        :param client_stream:
        :param name:
        :return:
        """
        queue = Queue()
        try:
            subscribers.add(queue)
            while True:
                name, msg = await queue.get()
                output = msg.encode("utf-8")
                logging.info(f"Sending {output} to {name}")
                peer = int(name.split('server-')[1])
                peer_port_number = const.CLUSTER[str(peer)]
                # await client.sendall(output)
                await self.heart_beat(peer_port_number, msg)
        finally:
            subscribers.discard(queue)

    async def incoming(self, client, input_data):
        """
        task that reads chat messages and publishes them
        :param input_data:
        :return:
        """
        # async for line in client_stream:
        # decoded_line = line.decode("utf-8").strip()
        logging.info(f"Received message {input_data} from name")
        # import os;os._exit(1)
        if input_data not in ['']:
            decoded_data = input_data.strip()
            name = 'server-' + decoded_data.split(',')[-1]
            logging.info(f"Need to digest message {decoded_data} from {name}")
            decoded_data = decoded_data.split(',')
            return_data = self.role.digest_message(message=decoded_data)
            if not return_data:
                import pdb;pdb.set_trace()
            logging.info(f"Message digested, prepare to send {return_data} to {name}")
            await self.publish((name, return_data))

    async def chat_handler(self, client, addr):
        async with client:
            client_stream = client.as_stream()
            # while True:
            data = await client_stream.read(100000)
            input_data = data.decode('utf-8')
            async with TaskGroup(wait=all) as workers:
                await workers.spawn(self.outgoing, client, input_data)
                await workers.spawn(self.incoming, client, input_data)
        logging.info("Connection closed")

    async def chat_server(
            self,
    ):
        # msg.recover(self.port_number)
        logging.info(f"Started TCP server at {self.port_number}")
        async with TaskGroup() as g:
            result_tcp = await g.spawn(
                tcp_server, self.ip_address, self.port_number, self.chat_handler,
            )
            await g.spawn(self.dispatcher)
            # dependency here result_tcp is needed for connect_peers
            await g.spawn(self.heart_beat, self.peers[0], result_tcp)
            await g.spawn(self.heart_beat, self.peers[1], result_tcp)
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
    raft_node = RaftNode(port_number, ip_address, peers, args.server, messages)
    run(raft_node.chat_server(), with_monitor=True)
