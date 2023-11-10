
#arr_1 = [-1,2,3,7,8]
#arr_2 = [0,2,3,5,6,100, 101, 102]
arr_1 = [1,2,4]
arr_2 = [1,3,4]

def merge_sorted_arrays(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    new_len = len_arr1 + len_arr2
    new_array = []
    min_len = min(len_arr1, len_arr2)
    x, y = 0, 0
    while (x <= len_arr1) and (y <= len_arr2):
        if x == len_arr1 or y == len_arr2:
            print(f'reached end of first loop arr2 len  {len_arr1} arr2 len {len_arr2}')
            break
        if arr1[x] == arr2[y]:
            print(f'arr1 {arr1[x]} equal to arr2 {arr2[x]}')
            new_array.append(arr1[x])
            x += 1
            new_array.append(arr2[y])
            y += 1
            continue
        elif arr1[x] < arr2[y]:
            print(f'arr1 {arr1[x]} less than arr2 {arr2[x]}')
            new_array.append(arr1[x])
            x += 1
            continue
        elif arr1[x] > arr2[y]:
            print(f'arr1 {arr1[x]} greater than arr2 {arr2[x]}')
            new_array.append(arr2[y])
            y += 1
            continue


    print(f'x={x}, len_arr1={len_arr1}, y ={y}, len_arr2={len_arr2}')
    if y <= len_arr2:
        while y < len_arr2:
            new_array.append(arr2[y])
            y += 1
    if x <= len_arr1:
        while x < len_arr1:
            new_array.append(arr2[x])
            x += 1
    return new_array


print(f'sorted array {merge_sorted_arrays(arr_1, arr_2)}')
