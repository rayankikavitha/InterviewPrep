def partition(alist,first,last):
   pivotvalue = alist[first]
   #print "pivot value ="+str(pivotvalue)

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while leftmark <=rightmark and alist[rightmark] >= pivotvalue:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def quick_select(nums, k):
    pi = partition(nums, 0, len(nums) - 1)

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

