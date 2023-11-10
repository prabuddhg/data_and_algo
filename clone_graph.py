adj_list = [[2,4],[1,3],[2,4],[1,3]]

def clone_graph(adj_list):
    clone_map = {
        'start': None
    }
    node_index = 1
    for node_index in range(1, len(adj_list)+1):
        print(f"processing for {node_index}")
        if clone_map['start'] is None:
            clone_map['start'] = node_index
        real_index = node_index - 1
        clone_map[node_index] = {
            'links' : False,
            'visited' : False
        }
        clone_map[node_index]['links'] = adj_list[real_index]
    #print(f"map {clone_map}")
    queue = []
    queue.append(clone_map['start'])
    adj_list_copy = []
    while len(queue) > 0:
        node = queue.pop(0)
        clone_map[node]['visited'] = True
        print(f"Visiting  node {node}")
        for each_neighbor in clone_map[node]['links']:
            neigh_list = []
            if clone_map[each_neighbor]['visited']:
                print(f"already visited this node {each_neighbor}")
                continue
            queue.append(each_neighbor)
            neigh_list.append(each_neighbor)
        adj_list_copy.append(clone_map[node]['links'])
    print(adj_list_copy)

    return clone_map, adj_list_copy

print(clone_graph(adj_list))