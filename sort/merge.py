'''
[6, 5, 100, 4, 99, 3, 2, 24, 1, 0, -24]
[6, 5, 100, 4, 99, 3]                  [2, 24, 1, 0, -24]
[6, 5, 100]   [4, 99, 3]               [2, 24, 1][0, -24]
[6, 5][100]   [4, 99][3]               [2, 24][1][0][-24]
[6][5][100][] [4][99][3][]             [2][24][1][][0][][-24][]
Combine
[5,6][100]    [4,99][3]                [2,24][1][0],[-24]
[5,6, 100]    [3,4, 99]                [1,2, 24][-24, 0]
[3,4,5,6,99,100]                       [-24,0,1,2,24]
[-24, 0, 1, 2, 3, 4, 5, 6, 99, 100]

Simple combine:

[5,6, 101][23, 100]
A=3,  B=2

compare A[0] with B[0] A[0]->C[0] [5]           and increment A[0] to A[1] position 0
compare A[1] with B[0] A[1]->C[1] [5, 6]        and increment A[1] to A[2] position 1
compare A[2] with B[0] B[0]->C[2] [5, 6, 23]    and increment B[0] to B[1] position 2
compare A[2] with B[1] A[2]->C[3] [5,6,23,100]  and increment B[1] to B[2] position 3

B is exhausted
C is pending. How do we know that? Becuase A size is 3 min was 2

'''
new_list = [6, 5, 100, 4, 99, 3, 2, 24, 1, 0, -24]

def combine_sorted_lists(list_A, list_B):
    lengthA = len(list_A) - 1
    lengthB = len(list_B) - 1
    listC = []
    a_position = 0
    b_position = 0
    c_position = 0
    min_value = min(lengthA, lengthB)
    print(f'lengthA is {lengthA} and lengthB is {lengthB} and min_val {min_value} ')
    while (a_position <= min_value) or (b_position <= min_value):
        if (a_position > lengthA) or (b_position > lengthB):
            break
        print(f'a_position is {a_position} and b_position is {b_position}')
        if list_A[a_position] < list_B[b_position]:
            listC.append(list_A[a_position])
            a_position += 1
        elif list_A[a_position] > list_B[b_position]:
            listC.append(list_B[b_position])
            b_position += 1
        elif list_A[a_position] == list_B[b_position]:
            listC.append(list_B[b_position])
            a_position += 1
            b_position += 1
        print(listC)
        c_position += 1

    while a_position <= lengthA:
        print(f'a_position is {a_position} and lengthA is {lengthA}')
        listC.append(list_A[a_position])
        a_position += 1
    while b_position <= lengthB:
        print(f'b_position is {b_position} and lengthB is {lengthB}')
        listC.append(list_B[b_position])
        b_position += 1
    print(f'return sorted list C {listC}')
    return listC

#combine_sorted_lists([5,6],[0, 23, 100, 205])

def merge_sort(unsorted_list):
    print(f'input list is {unsorted_list}')
    import time; time.sleep(1)
    if len(unsorted_list) == 1 or len(unsorted_list) == 0:
        print(f'return list is {unsorted_list}')
        return unsorted_list
    mid = int(len(unsorted_list)/2)
    print(f'left input list is {unsorted_list[:mid]}')
    left_list = merge_sort(unsorted_list[:mid])
    print(f'right input list is {unsorted_list[mid:(len(unsorted_list))]}')
    right_list = merge_sort(unsorted_list[mid:(len(unsorted_list))])
    combined_list = combine_sorted_lists(left_list, right_list)
    return combined_list

new_list = [6, 5, 100, 4, 99, 3, 2, 24, 1, 0, -24]
#new_list = [100, 5, 6]
print(f'sorted list {merge_sort(new_list)}')