import networkx as nx
import pprint

word = 'eertree'
word= 'toot'

def initiate_graph():
    graph = nx.DiGraph()
    graph.add_edges_from([("0", "-1"), ("-1", "-1")])
    return graph

def traverse_children_of_imaginary(each_char, last_char, children_of_imaginary):
    count = len(children_of_imaginary) - 1
    #import pdb;pdb.set_trace()
    while(count >= 0):
        child_list = [i for i in children_of_imaginary[count]]
        if child_list[-1] == last_char:
            return count
        else:
            count -= 1
            continue
    return False

def construct_palindrome_tree(graph, word):
    word_list = [i for i in word]
    print(f"word list {word_list}")
    #import pdb;pdb.set_trace()
    children_of_imaginary = []
    last_char = None
    for each_char in word_list:
        print(f"Processing character: {each_char}")
        print(f"Children of imaginary: {children_of_imaginary}")
        if each_char not in children_of_imaginary:
            # Case #1 if char not in imaginary node
            # then add it as a child of imaginary node
            # This acts as longest prefix part
            graph.add_edge("-1", each_char)
            # Part of case #1, make the child node
            # point to the empty node 0 which is the
            # longest suffix proper part
            graph.add_edge(each_char, "0")
            children_of_imaginary.append(each_char)
        elif each_char in children_of_imaginary and traverse_children_of_imaginary(each_char, last_char, children_of_imaginary):
            count = traverse_children_of_imaginary(each_char, last_char, children_of_imaginary)
            new_node = each_char + children_of_imaginary[count] + each_char
            if new_node not in word:
                print(f"substring= {new_node} no in {word}")
                if each_char in children_of_imaginary and each_char != last_char:
                    new_node = each_char + last_char + each_char
                    # Case #3 potential pallindrome
                    # First edge is find the longest prefix path
                    graph.add_edge(last_char, new_node)
                    # Also part of case #3, make it point to
                    # the child node under null node 0
                    # which helps us find the logest suffix proper
                    graph.add_edge(new_node, each_char)
                    children_of_imaginary.append(new_node)
            else:
                # Case #4 potential palindrome
                # First edge is find the longest prefix path
                graph.add_edge(last_char, new_node)
                # Also part of case #3, make it point to
                # the child node under null node 0
                # which helps us find the logest suffix proper
                graph.add_edge(new_node, each_char)
                children_of_imaginary.append(new_node)
        elif each_char in children_of_imaginary and each_char == last_char:
            new_node = each_char + last_char
            # Case #2 if char is already added
            # under imaginary node, then add the
            # concatenated new node under null node '0'
            graph.add_edge("0", new_node)
            # Also part of case #2, make it point to
            # the child node under imaginary node
            graph.add_edge(new_node, last_char)
        elif each_char in children_of_imaginary and each_char != last_char:
            new_node = each_char + last_char + each_char
            # Case #3 potential pallindrome
            # First edge is find the longest prefix path
            graph.add_edge(last_char, new_node)
            # Also part of case #3, make it point to
            # the child node under null node 0
            # which helps us find the logest suffix proper
            graph.add_edge(new_node, each_char)
            children_of_imaginary.append(new_node)
        last_char = each_char
    print(f"graph => ")
    pprint.pprint(nx.to_dict_of_dicts(graph))

graph = initiate_graph()
print(f"graph initiated {nx.to_dict_of_dicts(graph)}")
construct_palindrome_tree(graph, word)



