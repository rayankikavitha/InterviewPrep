"""
If nums = [1,2,3], a solution is:
Note: The solution set must not contain duplicate subsets.
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def combinations(nums):
    res =[[]]
    for num in sorted(nums):
        res += [num]
        #res += [item + [num] for item in res]
        print res

print combinations([1,2,3])

