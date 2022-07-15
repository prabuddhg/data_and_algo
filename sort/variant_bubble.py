
#new_list = [6, 5, 4, 3, 2, 1, 0]
new_list = [6, 5, 100, 4, 99, 3, 2, 24, 1, 0, -24]
def sort(unsorted_list):
    comparision = 0
    for i in range(len(unsorted_list)):
        for j in range(i+1, len(unsorted_list)):
            print(f'j = {j}')
            if unsorted_list[i] > unsorted_list[j]:
                comparision += 1
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
                print(f'list = {unsorted_list}')
            else:
                print(f'no exchange')
        print(f'list = {unsorted_list}')
    print(f'Total comparision = {comparision}')
    return unsorted_list

print(f'unsorted list = {new_list}')
print(f'sorted list = {sort(new_list)}')
