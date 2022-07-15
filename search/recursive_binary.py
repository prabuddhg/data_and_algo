'''
iteration #1:
             0                                  9
test_list = [1, 3, 31, 44, 50, 69, 77, 88, 93, 100]
find_item = 100
first = 0
last = 9
mid = 4
compare 50 with 100

iteration #2:
                           4                   9
test_list = [1, 3, 31, 44, 50, 69, 77, 88, 93, 100]
find_item = 100
first = 5
last = 9
mid = 7
compare 77 with 100

iteration #3:
                                            8   9
test_list = [1, 3, 31, 44, 50, 69, 77, 88, 93, 100]
find_item = 100
first = 8
last = 9
mid = 8
compare 93 with 100

iteration #4:
                                        8       9
test_list = [1, 3, 31, 44, 50, 69, 77, 88, 93, 100]
find_item = 100
first = 9
last = 9
mid = 9
compare 100 with 100

'''


test_list = [1, 3, 31, 44, 50, 69, 77, 88, 93, 100] # 10/2, 5/2, 2/2

def binary_search(test_list, find_item, first, last):
    mid = int((first + last)/2)
    print(f'first {first} last {last} mid {mid}')
    if(first>last):
        print(f'item {find_item} not found')
        return False
    if (find_item == test_list[mid]):
        print(f'found item {find_item} at {mid}')
        return True
    if (find_item < test_list[mid]):
        last = mid - 1
        return binary_search(test_list, find_item, first, last)
    elif (find_item > test_list[mid]):
        first = mid + 1
        return binary_search(test_list, find_item, first, last)

    else:
        return False

return_value = binary_search(test_list, 44, 0, len(test_list) - 1)

if not (return_value):
    print(f'No item {return_value} found')
else:
    print(f'found item')