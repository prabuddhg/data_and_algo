import os
from functools import lru_cache
import logging
import time

logging = logging.getLogger(__name__)

class Term():

    def __init__(self, server_number=None):
        self.server_number = server_number
        self._term = 0
        self.set_term()

    def get_term(self):
        with open(self.get_file(), "r") as ks:
            file_line = ks.readline()
            while file_line:
                self._term = file_line.strip()
                logging.info(f"For server: {self.server_number}, current term is {self._term} ")
        return self._term

    def set_term(self, input_term=0):
        self._term = input_term
        count = 0
        while count < 10:
            try:
                lock_file = f"/tmp/term-{self.server_number}.lock"
                with open(lock_file, "x") as fn:
                    fn.write(str(os.getpid()))
                    with open(self.get_file(), "w") as ks:
                        ks.write(f"{self._term}\n")
            except FileExistsError:
                time.sleep(1)
                count += 1
        logging.info(f"For server: {self.server_number}, new term is {self._term} ")

    @lru_cache
    def get_file(self):
        curr_dir = os.getcwd()
        key_store = os.path.join(curr_dir, f"term-{self.server_number}.txt")
        return key_store