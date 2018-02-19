"""
Convert character to ascii and sort on ascii values

ord('a') = 97
chr(97) ='a'

"""

t="I love coffee in the morning"

def Partition(A, start, end):
    pivot = A[start]
    left = start+1
    right = end
    while left <= right:
        if A[left] <= pivot:
            left = left+1
        elif A[right] >= pivot:
            right -= 1
        else:
            A[left],A[right] = A[right],A[left]
    A[start],A[right] = A[right],A[start]
    return right

def quick_sort_helper(input, st, end):
    if st < end:
        p = Partition(input,st,end)
        quick_sort_helper(input,st, p-1)
        quick_sort_helper(input,p+1,end)


def quick_sort(input):
    quick_sort_helper(input, 0, len(input)-1)


def sort_a_string(mystr):
    news = bytearray(mystr)
    quick_sort(news)
    return news

#print sort_a_string([9,3,56,79,1])
print sort_a_string(t)



# for code in bytearray(str): creats extra data structre