def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        print left, right
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1




nums = [9,3,6,2,1,7,5,8,4]
nums2 =[5,-2,-1,4,5,1,0]
"""
merge_sort(nums)
merge_sort(nums2)
print nums2
print nums
"""

def MergeSort(intArr):
    if len(intArr) > 1:
        mid = len(intArr) // 2
        left = intArr[:mid]
        right = intArr[mid:]
        MergeSort(left)
        MergeSort(right)
        # i for iterating left array, j for iterating right array and k for interating nums ( the final merge)
        # Start the merge process
        i, j, k = 0, 0, 0
        # compare left and right index by index, which ever is less assign it to nums
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                intArr[k] = left[i]
                i += 1
            else:
                intArr[k] = right[j]
                j += 1
            k += 1
        # copy left over left side if left side element are all not visited
        while i < len(left):
            intArr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            intArr[k] = right[j]
            j += 1
            k += 1


string =list('kavitha')
MergeSort(nums2)
MergeSort(string)
print nums2
print string