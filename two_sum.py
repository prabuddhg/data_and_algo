'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

       0
     2   7   x  x  (If number greater than 9, dont add to queue) 11  15
  9(reached)

        0
   3    2    4
5   x  5  6(achieved)         (If the sum is greater than 6, dont add to queue) 4

       0
    3     3
  3 (achieved)

                      0(target=10)
   2        4                    9    6    5
6  8  7   x  10(achieved via 6)


  1. Queue to add elements
  2. If number greater than target, dont add to queue
  3. If sum greater than target, dont add to queue
  4. If the sum is already there, dont add to the queue

Need a way to keep track of the position, may be a tuple like (value,position)

1. Start with 0
2. Add each element to 0 and if the sum is > target, dont add   (what if number == target)
3. Each element in #2 is a child of 0
4. For each child of #3, iterate through all children of #2 without itself
      and add these nodes to the element itself with following conditions:
         4.1 If sum greater than target, dont add to queue
         4.2 If the sum already exists in the queue, dont add it
         4.3 If the sum = Target, return found

adjacency_dict = {
    '0' : {
        parent: Root
        visited: True
        children: [2, 7]
        position: [0, 1]
    },
    '2' : {
        visited: True
        parent: '0'
        children: [9]
        position: [1]
    },
    '7': {
        visited: False
        children: []
        position: []
    },
    '9': {
        visited: False
        children: []
        position: []
    },
}

Input: nums = [3,2,4], target = 6
Output: [1,2]

      0
   3   2   4
5  x  6(achieved)

adjacency_dict = {
    '0' : {
        parent: Root
        visited: True
        children: [3, 2, 4]
        position: [0, 1, 2]
    },
    '3' : {
        visited: True
        parent: '0'
        children: [5] # only 3+2 added, as 3+4>6
        position: [1] # only 2 noted
    },
    '2': {
        visited: True
        parent: '0'
        children: ['6']
        position: ['2']
    },
    '4': {
        visited: False
        parent: '0'
        children: []
        position: []
    },
}
'''
import pprint
import copy
queue = []
inner_dict = {
    'parent': '',
    'visited': False,
    'children': [],
    'position': [],
    'duplicates': []
}
adjacency_dict= dict()
target = 9
input = [2,7,11,15]
#input = [3,2,4]
#input=[3,3]
#target=6
input=[1,2,3,4,5]
target=15
queue.append(0)

def find_if_equal(each_num, input, adjacency_dict, parent, each_num_count):
    index_list = []
    count = 0
    if parent==0:
        return False
    for each_element in input:
        index_list.append(count)
        count += 1
    if len(adjacency_dict[parent]['duplicates']):
        if each_num_count not in adjacency_dict[parent]['duplicates']:
            # False case
            # this is a duplicate scenario and new entry
            return False
        else:
            # True case
            # this is a duplicate scenario and not a new entry
            if adjacency_dict[parent]['position'][0] == adjacency_dict[parent]['duplicates'][each_num_count]:
                #  duplicate for adding
                return True
            else:
                return False
    else:
        if each_num == parent:
            return True
        else:
            return False


def traversal(adjacency_dict, target, input, queue):
    while len(queue) != 0:
        parent = queue.pop(0)
        print(f'from queue |__> {parent}')
        if parent == target:
            print(f"found it")
            adjacency_dict[parent]['visited'] = True
            return parent
        if parent == 0:
            adjacency_dict[parent] = copy.deepcopy(inner_dict)
            adjacency_dict[parent]['parent'] = 'root'
            adjacency_dict[parent]['visited'] = True
        count = 0
        for each_num in input:
            print(f'each num {each_num}')
            child = parent + each_num
            #if child > target or child in queue or each_num == value:
            #if child > target or (each_num == parent):
            find_if_equal_val = find_if_equal(each_num, input, adjacency_dict, parent, count)
            if child > target:
                print(f'skip adding {child} to dict sum is big')
                count += 1
                continue
            if (find_if_equal_val):
                print(f'skip adding {child} to dict for count {count}')
                count += 1
                continue
            if child == target:
                print(f'adding {child} to dict, found it for parent {parent}')
                adjacency_dict[child] = copy.deepcopy(inner_dict)
                adjacency_dict[child]['parent'] = parent
                adjacency_dict[child]['visited'] = True
                adjacency_dict[parent]['visited'] = True
                adjacency_dict[child]['position'].append(count)
                queue.append(child)
                count += 1
                return child
            if each_num in adjacency_dict and parent==0:
                print(f'duplicate found {each_num}, updating duplicates')
                adjacency_dict[each_num]['visited'] = True
                adjacency_dict[each_num]['duplicates'].append(count)
                count += 1
                continue
            elif (child) <= target:
                print(f'adding new {child} to dict for parent {parent}')
                queue.append(child)
                adjacency_dict[parent]['children'].append(child)
                adjacency_dict[parent]['position'].append(input.index(each_num))
                adjacency_dict[parent]['visited'] = True
                adjacency_dict[child] = copy.deepcopy(inner_dict)
                adjacency_dict[child]['parent'] = parent
                adjacency_dict[child]['duplicates'].append(count)
                adjacency_dict[child]['position'].append(count)
            count += 1

def backtrack(backtrack_num, adjacency_dict):
    done = False
    position_list = []
    while not done:
        if adjacency_dict[backtrack_num]['parent'] == 'root':
            done = True
            return position_list
        else:
            parent = adjacency_dict[backtrack_num]['parent']
            #index = adjacency_dict[parent]['children'].index(backtrack_num)
            #position_list.append(adjacency_dict[parent]['position'][index])
            #position_list.append(adjacency_dict[parent]['position'][-1])
            position_list.append(adjacency_dict[backtrack_num]['position'][-1])
            backtrack_num = parent

backtrack_num = traversal(adjacency_dict, target, input, queue)
pprint.pprint(adjacency_dict)

print(f'backtrack from: {backtrack_num}')
back_list = backtrack(backtrack_num, adjacency_dict)

back_list.reverse()
print(back_list)

