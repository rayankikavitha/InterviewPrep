"""
https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
"""
def find_element_in_2d_sorted_array(nums,x):
    """
    :param nums: 2d array [ [1,2,3,4] [5,6,7,8] [9,10,11,12] ]
    :param x: 6
    :return:
    """
    m = len(nums)
    n = len(nums[0])
    # row index, column index to start from top right most corner
    ci = n-1
    ri = 0
    while nums[ri][ci]:
        e = nums[ri][ci]
        if x > e:
            ri += 1
            if ri > m-1:
                return False

        elif x < e:
            ci -= 1
            if ci <0:
                return False
        else:
            return (ri,ci)
    return False

arr = [ [1,2,3,4] ,[5,6,7,8] , [9,10,11,12] ]
print find_element_in_2d_sorted_array(arr, 6)
print find_element_in_2d_sorted_array(arr, 12)
print find_element_in_2d_sorted_array(arr, 15)


