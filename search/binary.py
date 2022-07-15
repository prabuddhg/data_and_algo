import time
test_list = [1, 3, 31, 44, 50, 69, 77, 88, 93, 100] # 10/2, 5/2, 2/2
def binary_search(test_list, find_item):
    first = 0
    last = len(test_list) - 1
    mid = int((first + last)/2)
    found = False
    while (first<last):
        print(f'first = {first} last = {last}')
        if (find_item == test_list[mid]):
            found = True
            break
        if find_item < test_list[mid]:
            last = mid - 1
        elif find_item > test_list[mid]:
            first = mid + 1
        mid = int((first + last) / 2)

    if found:
        print(f'found item {find_item} at {mid}')
    else:
        print(f'item {find_item} not found')

binary_search(test_list, 31)