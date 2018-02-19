
"""

def partition(nums, low, high):
    pivot = low
    swap(nums,pivot,high)
    for i in range(low,high):
        if nums[i] <= nums[high]:
            swap(nums,i,high)
            low += 1
    swap(nums,low,high)
    return low

def swap(nums,x, y):
    temp = nums[x]
    nums[x] = nums[y]
    nums[y] = temp

def quick_sort(nums,low, high):
    if low < high:
        p = partition(nums,low, high)
        quick_sort(nums,low,p-1 )
        quick_sort(nums,p+1, high)


nums = [6,3,9,2,1,7,5,8,4]
quick_sort(nums,0,len(nums))
print nums
"""

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


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

def pairs(nb):
    result =[]
    n = len(nb)/2
    for i in range(n):
        result.append(nb[i]+nb[i+n])
    return result

if __name__ == "__main__":

    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)

    nuts_and_bolts = ['N1','N2','B1','B3','B0','N3','B2','N0']
    quickSort(nuts_and_bolts)
    print nuts_and_bolts
    print pairs(nuts_and_bolts)

    dutch = [3,2,1,2,3,2,3,3,1,1,1,0,0,0,0,1]
    quickSort(dutch)
    print dutch