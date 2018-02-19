def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       # here if rt < lt, then we finished parsing the array
       if rightmark < leftmark:
           done = True
       else : #swap
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   # pivot ends up the right pointer
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


nuts_and_bolts = ['N1','N2','B1','B3','B0','N3','B2','N0']
quickSort(nuts_and_bolts)
print nuts_and_bolts
print pairs(nuts_and_bolts)