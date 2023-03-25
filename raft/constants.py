CLUSTER = {"1": 25001, "2": 26001, "3": 27001}
#CLUSTER = {"1": 25001, "2": 26001}


def get_port_number(server_number):
    peers = [value for key, value in CLUSTER.items() if key not in [server_number]]
    return CLUSTER[server_number], peers

if __name__ == "__main__":
    print(get_port_number("1"))
