"""
k=xyz  A='xyyzyzx' output ='yzx'
"""
def cleard(d):
    for k,v in d.items():
        d[k] = 0

def minWindow_kr(s, t):

    need ={}
    missing =len(t)
    for each in t:
        need[each] = 0

    print need, missing
    head = 0
    i = 0
    res = s+s
    newstart = 0
    while  i < len(s):
        if s[i] in need:
            if need[s[i]] == 0:
                need[s[i]] += 1
            if sum(need.values()) == 2:
                newstart = i
            print i,need
            if sum(need.values()) == len(t):
                print s[head:i+1], newstart
                res = min(res, s[head:i+1], key = len)
                i = newstart
                head = newstart
                cleard(need)
                print i,head
        i +=1
    return res

# leetcode
def minWindow(s, t):
    need={}
    #initalize with highest value to compare against
    minlen = len(s)+1
    #start point of the minimal window
    minstart = 0
    # mapping to get counts of each character
    for each in t:
        need[each] = need.get(each,0)+1
    # counter for text
    counter = len(t)
    start = 0
    end = 0
    head = 0
    while end < len(s):
        # If char in s exists in t, decrease the counter
        if s[end] in need:
            if need[s[end]] > 0:
                counter -= 1
            need[s[end]] -= 1
        print need
        # If the current window has all the chars
        while counter == 0:
            # see if the window is smaller
            if end - start+ 1 < minlen:
                minlen = end - start + 1
                minstart = start
                print minstart, minlen

            #if s[start] is desired, we need to add it to map and increase counter
            if s[start] in need:
                need[s[start]] += 1
                # update the counter only if the current char is critical
                if need.get(s[start]) > 0:
                    counter  += 1
            # move forward to find the smaller window
            start += 1
            print end,need, minstart, minlen
        # end forward to find another valid window
        end += 1

    if minlen == len(s)+1:
        return ""
    else:
        return s[minstart:minstart+minlen]



#print smallsubstring("xyz","xyyzyzx")
print minWindow("ayzabobecodxbanc", "abc")
print minWindow("acdbddddddddaaaaaaaadabbbbba", "baad")