""""
Write a function that list any 3 elements that sum to zero, from an array of integers.

Notes:

We need all unique solutions. (-5, -5, 10) is same as (10, -5, -5)
The same element can be used multiple times.
Example
Input: [-5, 1, 10, 2, 3] // array of integers
Output: [(-5, -5, 10), (-5, 2, 3)] // array of tuples

"""
def threesumzero(a):
    """
    Find triplets that sum to zero
    :param a: an array of integers to analyze
    :return: return unique triplets out of input array that sum to zero, an item in triplet may repeat at most twice
    """
    result = set()  # set to eliminate deuplicates!
    a.sort() # sort it
    n = len(a) # number of items in a
    for x in a: # for each element in a, see if its part of some triplet
        target_sum = 0 - x # x and other two items must sum to 0, so other two must sum to -x
        i = 0 # from beginning
        j = n - 1 # from end
        while i < j:
            if a[i] + a[j] == target_sum: # we found triplet
                result.add( tuple( sorted( [x, a[i], a[j] ] ) ) ) # sort it (for uniqueness) and convert it to tuple as its immutable
                i += 1
                j -= 1
            elif a[i] + a[j] > target_sum:
                j -= 1
            else: # a[i] + a[j] < target_sum
                i += 1

    return result


Input = [-5, 1, 10, 2, 3]
print threesumzero(Input)