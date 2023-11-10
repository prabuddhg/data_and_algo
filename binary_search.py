arr = [-1,0,3,5,9,12]

def binary_search(arr, search_item):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = int((low + high)/2)
        print(f'low {low}, high {high}, mid {mid} and value {arr[mid]}')
        if search_item == arr[mid]:
            print(f'found at {mid}')
            return mid
        elif search_item < arr[mid]:
            high = mid
        elif search_item > arr[mid]:
            low = mid+1
    print(f'{-1}')
    return -1

binary_search(arr,3)