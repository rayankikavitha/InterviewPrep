"""
Max "Rectangle" area under histogram
https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""
def peek(s):
    if len(s)>0:
        return s[len(s)-1]

def findmaxarea(hist):
    """
    Insert into the stack
    :param arr:
    :return:
    """
    s= []
    max_area=0
    tp=0
    i=0
    n = len(hist)
    while i < n:
        # if incoming bar is higer than the top of the stack, push it
        if not s or hist[i] >= hist[peek(s)]:
            s.append(i)
            i +=1
            #print s
        #If the incoming bar is lower than the top of the stack, then calculate area of rectangle
        # with the stack top as the smallest(or minimum height) bar.
        # i is the right index for the top element before top in stack is left index
        else:

            tp = s.pop() #store top of the stack
            # Calculate the area with hist[tp] as the smallest bar
            if len(s) ==0:
                area_with_top = hist[tp] * i
            else:
                area_with_top = hist[tp] * (i-peek(s)-1)

            # update max area
            if max_area < area_with_top:
                max_area = area_with_top
            #print max_area, area_with_top,i
            #print s

    # now pop the remaining bars from stack and calculate area with every popped as the smallest bar
    while s:
        tp = s.pop()
        area_with_top = hist[tp] * (i if len(s) == 0 else i - tp - 1)
        if max_area < area_with_top:
            max_area = area_with_top

    return max_area

print findmaxarea([6,2,5,4,5,1,6])
print findmaxarea([2,1,2,3,1])