import logging

logging = logging.getLogger(__name__)

append_entry_args_list = [
    'term',  # int		// current term of the leader, very IMPORTANT
    'leader_id',  # int		// id of the leader, 0 to N-1 where N = total servers
    'entries',  # [] Entry  // new data to sync
    'prev_log_index',  # int		// important metadata for log correctness
    'prev_log_term',  # int		// important metadata for log correctness
    'leader_commit'  # int 	    // what index have been received by the majority
]

append_entry_reply_list = [
    'term',  # : None # int 	// current term of the receiving node
    'success',  # : None # bool	// AppendEntry declined or accepted
    'conflict_index',  # : None # int	// if declined, specifying the conflicting index
    'conflict_term'  # : None # int	// if declined, specifying the conflicting term
]


def get_append_entry_args_list(term=0, leader_id=0, entries=[], prev_log_index=0, prev_log_term=0, leader_commit=0):
    return_msg = None
    for each_value in append_entry_args_list:
        if return_msg is None:
            return_msg = str(eval(each_value))
        else:
            return_msg = return_msg + ',' + str(eval(each_value))
    return_msg = f'{return_msg}\n'
    return return_msg


def get_append_entry_reply_list(term=0, success=0, conflict_index=0, conflict_term=0):
    return_msg = None
    for each_value in append_entry_args_list:
        if return_msg is None:
            return_msg = str(eval(each_value))
        else:
            return_msg = return_msg + ',' + str(eval(each_value))
    return_msg = f'{return_msg}\n'
    return return_msg


if __name__ == "__main__":
    print(get_append_entry_args_list())
    print(get_append_entry_reply_list())
