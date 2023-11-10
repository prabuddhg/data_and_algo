"""
Input: accounts = [ ["John","johnsmith@mail.com","john_newyork@mail.com"],
                    ["John","johnsmith@mail.com","john00@mail.com"],
                    ["Mary","mary@mail.com"],
                    ["John","johnnybravo@mail.com"]
                ]
Output: [   ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]

account_map = {
     "John" = {
            "1": ["johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]
            "2": ["johnnybravo@mail.com"]
     }
     "Mary" = {
            "1": ["mary@mail.com"]
     }
}

"""
accounts = [["John","joe_a@mail.com","johna@mail.com"],
            ["John","a_joe@mail.com"],
            ["John","joe_b@mail.com", "joe-b@mail.com", "b_joe@mail.com"],
            ["John","a_joe@mail.com", "joe_a@mail.com"],
            ["Mary","mary@mail.com"],
            ]

class Solution(object):
    def __init__(self):
        self.acount_map = {}

    def accountsMerge(self, accounts):
        graph = {}
        group_count = 0
        email2accountindex = {}
        account_hashmap = {}
        for each_entry in accounts:
            each_entry.pop(0)
            account_hashmap[group_count] = each_entry
            group_count = group_count + 1
        print(f"account hash map = {account_hashmap}")
        count = 0
        set_count = 0
        for each_key in account_hashmap:
            emails = account_hashmap[each_key]
            for email in emails:
                if email not in email2accountindex:
                    email2accountindex[email] = count
                else:
                    set_count = 'G' + str(email2accountindex[email])
                    print(f"this {email} for {each_key} already there at {email2accountindex[email]}")
                    print(f"Adding these entries at {set_count}")
                    if email2accountindex[email] not in graph:
                        graph[email2accountindex[email]] = [each_key]
                    else:
                        graph[email2accountindex[email]].append(each_key)
                    if each_key not in graph:
                        graph[each_key] = [email2accountindex[email]]
                    else:
                        graph[each_key].append(email2accountindex[email])
                if each_key not in graph:
                    graph[each_key] = []
            count = count + 1
        groups = {}
        count_group = 1
        visited = []
        for each_key in graph:
            if graph[each_key] == {}:
                groups[count_group] = [each_key]
                groups[f"element-{each_key}"] = count_group
            else:
                queue = []
                queue.append(each_key)
                while len(queue) > 0:
                    neighbour = queue.pop(0)
                    if neighbour not in visited:
                        if count_group not in groups:
                            groups[count_group] = []
                        groups[count_group].append(neighbour)
                        groups[f"element-{neighbour}"] = count_group
                    visited.append(neighbour)
                    for new_neighbor in graph[neighbour]:
                        if new_neighbor not in visited:
                            queue.append(new_neighbor)
            count_group = count_group + 1
        # create return type
        return_list = {}
        for each_email in email2accountindex:
            index = email2accountindex[each_email]
            group_number = groups[f"element-{index}"]
            print(f"comparing index {index} with group {groups[group_number]}")
            if index in groups[group_number]:
                index_to_use = min(groups[group_number])
                if index_to_use not in return_list:
                    return_list[index_to_use] = [each_email]
                else:
                    return_list[index_to_use].append(each_email)

        print(f"{graph}")
        print(f"email account index = {email2accountindex}")
        print(f"Disjoint set data structure {groups}")
        print(f"return_list{return_list}")


obj = Solution()
obj.accountsMerge(accounts)


