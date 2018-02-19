"""
https://articles.leetcode.com/sliding-window-maximum/


"""

def sliding_window(arr,w):
    # initialize with the max element
    q = [max(arr[0:w])]
    # start from the next element of the window
    for i in xrange(w,len(arr)):
        # if incoming element is max than the current max, push it
        if q and q[len(q)-1] < arr[i]:
            q.append(arr[i])
        # else push the same element
        else:
            q.append(q[len(q)-1])

    return q, q[len(q)-1]

input = [1,3,-1,-3,5,3,6,7]
w = 3
print sliding_window(input, w)
# output : [3, 3, 5, 5, 6, 7]