from decimal import Decimal

array = [-2, 1, -3, 4, -1 , 2, 1, -5, 4]
array = [8,1,-3,4,-1,2,1,-5,4]
def kadane(array):
    local_max = 0
    global_max = Decimal('-Infinity')
    sub_array = []
    for i in range(0, len(array)):
        already_added = True
        print(f"\nprocessing {array[i]}")
        local_max = max(array[i], (array[i] + local_max))
        print(f"local max = {local_max}")
        if local_max > global_max:
            global_max = local_max
        print(f"global max = {global_max}====")
    return global_max

print(kadane(array))
