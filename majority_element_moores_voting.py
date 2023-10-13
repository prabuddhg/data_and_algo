"""
Input: { 1,7,2,7,8,7,7}

Index 0: num = 1, count =1
Index 1: num = 1, count =0 ( 7 not equal to 1)
Index 2: num = 2 (as the count is 0 we initalise num to current), count =1
Index 3: num = 2, count =0 ( 7 not equal to 2)
Index 4: num = 8 (as the count is 0 we initalise num to current), count =1
Index 5: num = 8, count =0 ( 7 not equal to 8)
Index 6: num = 7 (as the count is 0 we initalise num to current), count =1

Now we can check for the frequency of 7, i.e, 4 which is > 7/2.


Input = 1,2,1,3,1,4,1

Index = 0: num = 1, count = 1
Index = 1: num = 1, count = 0 (because 2 is not equal to 1)
Index = 2: num = 1, count = 1 (since prev count = 0, init num to Index 2, set count = 1)
Index = 3: num = 1, count = 0 (because 3 is not equal to 1)
Index = 4: num = 1, count = 1 (since prev count = 0, init num to Index 4, set count = 1)
Index = 5: num = 1, count = 0 (because 4 is not equal to 1)
Index = 6: num = 1, count = 1 (since prev count = 0, init num to Index 6, set count = 1)
"""

input = [1,7,2,7,8,7,7,8,8,8,8,8, 8]

def moores_voting(input):
    index = 0
    num = input[index]
    count = 1
    print(f"Index = {index}: num = {num}, count = {count}, value {[input[index]]}")
    while(index < len(input)):
        """
        Index 0: num = 1, count =1
        Index 1: num = 1, count =0 ( 7 not equal to 1)
        Index 2: num = 2 (as the count is 0 we initalise num to current), count =1
        Index 3: num = 2, count =0 ( 7 not equal to 2)
        Index 4: num = 8 (as the count is 0 we initalise num to current), count =1
        Index 5: num = 8, count =0 ( 7 not equal to 8)
        Index 6: num = 7 (as the count is 0 we initalise num to current), count =1
        """
        #import pdb;pdb.set_trace()
        if index == 0:
            #print(f"Index = {index}: num = {num}, count = {count}, value {[input[index]]}")
            index += 1
            continue
        if count == 0:
            num = input[index]
            count = 1
        elif input[index-1] == input[index]:
            count = count + 1
        elif input[index-1] != input[index]:
            count = count - 1
        print(f"Index = {index}: num = {num}, count = {count}, value {[input[index]]}")
        index += 1

    count = 0
    majority = 0
    while (count < len(input)):
        if num == input[count]:
            majority = majority + 1
        count = count + 1
    if majority > len(input)/2:
        return num
    return -1


print(moores_voting(input))