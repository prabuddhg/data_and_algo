

source = "bat"
dest = "cab"

def check_anagram(source, dest):
    map = {}
    source_list = [i for i in source]
    dest_list = [i for i in dest]
    for each_entry in source_list:
        if each_entry in map.keys():
            map[each_entry] += 1
        else:
            map[each_entry] = 1
    print(map)
    for each_entry in dest_list:
        if each_entry not in map.keys():
            print("False")
            return
        if each_entry in map.keys():
            map[each_entry] -= 1
    for each_entry in map.keys():
        if map[each_entry] != 0:
            print("False")
            return
    print(map)
    print("True")


check_anagram(source, dest)