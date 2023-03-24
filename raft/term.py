import os
from functools import lru_cache
import logging
import time

logging = logging.getLogger(__name__)

class Term():

    def __init__(self, server_number=None):
        self.server_number = server_number
        self._term = 0
        self.latest_term_tuple = None
        self.last_term_tuple = None
        # self.set_term()
        curr_dir = os.getcwd()
        self.key_file = os.path.join(curr_dir, f"term-{self.server_number}.txt")

    def get_latest_term_tuple(self):
        count = 0
        while count < 10:
            try:
                lock_file = f"/tmp/term-{self.server_number}.lock"
                with open(lock_file, "x") as fn:
                    fn.write(str(os.getpid()))
                    with open(self.get_file(), "r") as ks:
                        file_line = ks.readline()
                        while file_line:
                            file_line = ks.readline()
                        last_line = file_line
                        self.latest_term_tuple = last_line.strip()
                        logging.info(f"Server-{self.server_number}: Last line is {self.latest_term_tuple}")
                        os.remove(lock_file)
                        return self.latest_term_tuple
            except FileExistsError:
                time.sleep(1)
                count += 1


    def save_latest_term_tuple(self, raft_tuple):
        count = 0
        while count < 10:
            try:
                lock_file = f"/tmp/term-{self.server_number}.lock"
                with open(lock_file, "x") as fn:
                    fn.write(str(os.getpid()))
                    with open(self.get_file(), "w") as ks:
                        logging.info(f"Server-{self.server_number}: saving {raft_tuple}")
                        ks.write(f"{raft_tuple}\n")
                    os.remove(lock_file)
                    logging.info(f"Server-{self.server_number}: saving complete")
            except FileExistsError:
                time.sleep(1)
                count += 1


    # def get_term(self):
    #     with open(self.get_file(), "r") as ks:
    #         file_line = ks.readline()
    #         while file_line:
    #             self._term = file_line.strip()
    #             logging.info(f"For server: {self.server_number}, current term is {self._term} ")
    #     return self._term
    #
    # def set_term(self, input_term=0):
    #     self._term = input_term
    #     count = 0
    #     while count < 10:
    #         try:
    #             lock_file = f"/tmp/term-{self.server_number}.lock"
    #             with open(lock_file, "x") as fn:
    #                 fn.write(str(os.getpid()))
    #                 with open(self.get_file(), "w") as ks:
    #                     ks.write(f"{self._term}\n")
    #         except FileExistsError:
    #             time.sleep(1)
    #             count += 1
    #     logging.info(f"For server: {self.server_number}, new term is {self._term} ")

    @lru_cache
    def get_file(self):
        return self.key_file