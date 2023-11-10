import time
"""
input = [3,4,5,6,0,1,2]

1) 3,4,5,6,0,1,2
    l=1 H=7 M=4 (L=3, , M=6, H=2)
    if M is greater than L and M is greater than H
        # pivot is in right side
        l=mid+1, H=7
2) 6,0,1,2
    l=5 H=7 M=6 (L=0, , M=1, H=2)
    if M is greater than L and M is greater than H
        # pivot is in right side
        # condition not met
    if M is less than L and M is less than H
        # pivot is in left side side
        l=l, H=mid
    if M is greater than L and M is less than H
        # entered the sorted array section
        return L as the pivot
"""

input = [3,4,5,6,0,1,2]
input = [5,6,0,1,2,3,4]
input = [4,5,6,7,8,9,0,1,2]

def find_pivot(input):
    low=0
    high=len(input)-1
    print(f"finding pivot in input {input}")
    while (low<high):
        time.sleep(1)
        mid = int((low+high)/2)
        print(f"low={low}, mid={mid}, high={high}")
        low_val = input[low]
        high_val = input[high]
        mid_val = input[mid]
        if (mid_val > low_val) and (mid_val > high_val):
            # pivot is in right side
            # l = mid + 1, H = h
            low = mid + 1
            print(f"pivot is in right side {input[low:high+1]}")
        elif (mid_val < low_val) and (mid_val < high_val):
            # pivot is in left side side
            high = mid
            print(f"pivot is in left side {input[low:high+1]}")
        elif (mid_val >= low_val) and (mid_val <= high_val):
            # entered sorted list
            print(f"Entered sorted list, pivot found at {low} with lowest value={low_val}")
            return low, high
        elif (mid == low) or (mid == high):
            # entered last list
            print(f"Entered last list, pivot found at {high} with lowest value={high_val}")
            return low, high
    return low, high

print(f"{find_pivot(input)}")