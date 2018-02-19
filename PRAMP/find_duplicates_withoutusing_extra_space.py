"""
given = [1,2,2,1] output first duplicate in an array of size n . Array values are from 1.. n
"""

def first_dup(nums):
    nums.insert(0,0)
    for i,v in enumerate(nums):
        if i != v:
            if nums[v] == v:
                return v
    return None

print first_dup([1,2,2,1])
print first_dup([1,2,3])
print first_dup([1,1,1])
