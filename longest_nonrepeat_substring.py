"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

     ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b']
1)   x = 1
     count = 1
     local_longest = a
     global_longest = None
2)   x = 1
     count = 2
     local_longest = ab
     global_longest = None
3)   x = 1
     count = 3
     local_longest = abc
     global_longest = None
4)   x = 4
     count = 4
     local_longest = a
     global_longest = abc
5)   x = 4
     count = 5
     local_longest = ab
     global_longest = abc
6)   x = 4
     count = 6
     local_longest = abc
     global_longest = abc
7)   x = 7
     count = 7
     local_longest = b
     global_longest = abc
8)   x = 8
     count = 8
     local_longest = b
     global_longest = abc
"""


input = "abcabcbb"
#input = "abccbaabccbad"
#input = "bbb"
#input = "pwwkew"

def longest_nonr_substring(input):

    global_longest = ""
    local_longest = None
    input_list = [i for i in input]
    print(input_list)
    length = len(input_list)
    count = 0
    while count < length:
        if local_longest is None:
            # Case 1 initialization
            local_longest = input_list[count]
            print(f"Case 1 local_longest {local_longest}")
            count += 1
            continue
        if input_list[count] == local_longest or input_list[count] in local_longest:
            # Case 2 repeating characters
            print(f"Case 2 repeating character {input_list[count]} in {local_longest}")
            if len(local_longest) > len(global_longest):
                global_longest = local_longest
                local_longest = input_list[count]
            count += 1
            continue
        if input_list[count] not in local_longest:
            local_longest = local_longest + input_list[count]
            count += 1
            print(f"Case 3 creating longest string local longest {local_longest}")
            continue
        print("global longest {global_longest} with count {count}")
    if len(local_longest) > len(global_longest):
        global_longest = local_longest
        local_longest = None
    return global_longest




print(f"output {longest_nonr_substring(input)}")