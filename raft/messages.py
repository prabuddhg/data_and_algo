import os
import operations as op
from functools import lru_cache
import logging

logging = logging.getLogger(__name__)


@lru_cache
def get_file(server_number):
    curr_dir = os.getcwd()
    key_store = os.path.join(curr_dir, f"key_store-{server_number}.txt")
    return key_store


def save(input, server_number):

    if "set" in input or "del" in input:
        logging.info(f"Saving {input.strip()}")
        with open(get_file(server_number), "a") as ks:
            ks.write(f"{input}\n")
    else:
        logging.info(f"Skipping {input.strip()}")


def process(input, server_number):
    cache = []
    if input.strip() not in cache:
        cache.append(input.strip())
        save(input, server_number)
        return op.execute(input)
    else:
        logging.info(f"Skipping {input.strip()}")
        return



def recover(server_number):
    with open(get_file(server_number), "r") as ks:
        file_line = ks.readline()
        while file_line:
            logging.info(f"Processing {file_line.strip()}")
            if "set" in file_line or "del" in file_line:
                logging.info(f"Recovering {file_line.strip()}")
                op.execute(file_line)
            else:
                logging.info(f"Skipping {file_line.strip()}")
            # use realine() to read next line
            file_line = ks.readline()

def recover_peers(server_number):
    all_executions = []
    with open(get_file(server_number), "r") as ks:
        file_line = ks.readline()
        while file_line:
            if "set" in file_line or "del" in file_line:
                all_executions.append(file_line)
            file_line = ks.readline()
    return all_executions