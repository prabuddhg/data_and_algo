import time
intervals = [
    [1,2],
    [3,5],
    [6,7],
    [8,10],
    [12,16]
]
new_interval= [1,10]

def insert_interval(intervals, new_interval):
    mod_interval = []
    lower = new_interval[0]
    upper = new_interval[1]
    i = 0
    j = 0
    k = 0
    while i < len(intervals):
        #time.sleep(1)
        print(f"first {intervals[i]}")
        if intervals[i][0] <= lower and lower <= intervals[i][1]:
            new_lower = intervals[i][0]
            # found it
            i = i + 1
            break
        mod_interval.append(intervals[i])
        i = i + 1
    while j < len(intervals):
        if intervals[j][1] >= upper and intervals[j][0] >= new_lower:
            new_upper = intervals[j][1]
            # found it
            j = j + 1
            break
        j = j + 1
    print(f"new entries {[new_lower, new_upper]}")
    mod_interval.append([new_lower, new_upper])
    k = j
    while k < len(intervals):
        mod_interval.append(intervals[k])
        k = k + 1
    return mod_interval


print(insert_interval(intervals, new_interval))
