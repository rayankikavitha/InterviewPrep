"""
Given a point P and other N points in 2 dimentional space, find K points out of N which are nearest to P

This problem can be done with QuickSort Partitioning or can be done he Heaps.

"""

def quickSort(nums):
    quickSortHelper(nums,0,len(nums) -1)

def quickSortHelper(nums,lt,rt):
    while lt < rt:
        p = partition(nums,lt,rt)
        quickSortHelper(nums,lt,p-1)
        quickSortHelper(nums,p+1,rt)

def partition(nums,lt,rt):
    pivot = nums[0]
    lt
    done = True
