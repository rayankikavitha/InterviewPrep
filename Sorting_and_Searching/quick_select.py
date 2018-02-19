"""
Quick select is used when you know the input size = n and has to pick up k first elements

We can also use heap to get k min elements, but here the size is known.

So, doing quick sort until there first k positions are filled, we can stop the quick sort

Remember quick sort if p - pivot is the first element, it puts the pivot value in its final position.

"""
import quick_sort as qs


def quick_select(nums, k):
    pi = qs.partition(nums, 0, len(nums) - 1)

    #print nums
    #print pi

    while pi != k - 1:

        if pi > k - 1:  ## the kth element is in the left partition
            return quick_select(nums[:pi ], k)
        else:  # the kth element is in the right partition
            return quick_select(nums[pi + 1:], k)
    if pi == k - 1:
        return nums[0:k] #if you return nums[k-1] , you can do kth element


print "**********  Quick Select ************"
nums1 = [9, 3, 6, 2, 1, 7, 5, 8, 4]
nums2 = [5, -2, -1, 4, 5, 1, 0]
print quick_select(nums1, 4)
print quick_select(nums2, 3)

