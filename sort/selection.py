'''
new_list = [6, 5, 100, 4, 99]
            0  1   2   3   4

[6, 5, 100, 4, 99] - 4
i=0, j=1  6 ? 5,    so 6 is my max item, remember location of 6 i.e. 0
i=0, j=2  6 ? 100,  so 100 is my max item, remember location of 100 i.e. 2
i=0, j=3  100 ? 4,  so 100 is my max item, remember location of 100 i.e. 2
i=0, j=4  100 ? 99, so 100 is my max item, remember location of 100 i.e. 2

[6, 5, 99, 4, 100] - 3
i=0, j=1  6 ? 5,    so 6 is my max item, remember location of 6 i.e. 0
i=0, j=2  6 ? 99,   so 99 is my max item, remember location of 99 i.e. 2
i=0, j=3  99 ? 4,   so 99 is my max item, remember location of 99 i.e. 2

[6, 5, 4, 99, 100] - 2
i=0, j=1  6 ? 5,    so 6 is my max item, remember location of 6 i.e. 0
i=0, j=2  6 ? 4,    so 6 is my max item, remember location of 6 i.e. 0

[4, 5, 6, 99, 100] - 1
i=0, j=1  4 ? 5,    so 5 is my max item, remember location of 5 i.e. 1

'''

#new_list = [6, 5, 100, 4, 99]
new_list = [6, 5, 100, 4, 99, 3, 2, 24, 1, 0, -24]

def seletion(input_array):
    count = len(input_array) - 1
    print(f'{input_array}-->{count}')
    while count > 1:
        max_item_position = 0
        for j in range(0, count):
            if  input_array[max_item_position] < input_array[j]:
                max_item_position = j
        input_array[count], input_array[max_item_position] = input_array[max_item_position], input_array[count]
        count -= 1
        print(f'{input_array}-->{count}')

    return input_array

print(f'sorted {seletion(new_list)}')