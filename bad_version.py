"""
                      |  this is tot build
                      v
 100 101 102 103 104 105
 G   G   G   B   B   B

 Brute force is to go back n times

 1. i = 102
 100 101 102 103 104 105
         mid
             l=4     h=6
             mid
         l=3 h=4
"""
import time
versions = []
total_versions = 20
bad_version = 1

def create_versions(versions, total_versions, bad_version):
    count = 1
    while count <= total_versions:
        if count < bad_version:
            versions.append("G")
        else:
            versions.append("B")
        count += 1
    print(versions)
    return versions

def find_earliest_bad_version(version_list):
    low = 0
    high = len(version_list) - 1
    mid = int((low + high) / 2)
    while (low <= high):
        time.sleep(1)
        if version_list[mid] == 'B':
            high = mid
        else:
            low = mid+1
        mid = int((low + high) / 2)
        if low == high and version_list[mid]=="B":
            print(f"***found the first bad version={mid+1}, with low={low} and high={high} and mid={mid}")
            return
    print(f"not found the first bad version")



version_list = create_versions(versions, total_versions, bad_version)
find_earliest_bad_version(version_list)
