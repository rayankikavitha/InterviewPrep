input =[4,3,2,1,-7,2,3,8,2 ]
def delete_duplicates_from_a_list1(input):
    return list(set(input))

def delete_duplicates_from_a_list2(input):
    return list(set(input))

def delete_duplicates_from_a_list3(input):
    # order is not preserved
    s=set()
    for each in input:
        if each not in s:
            s.add(each)
    return list(s)

def delete_duplicates_from_a_list4(input):
    # order is not preserved
    d={}
    for each in input:
        if each not in d:
           d[each] = 1
    return d.keys()


def delete_duplicates_from_a_list5(input):
    # order is preserved
    newlist =[]
    for each in input:
        if each not in newlist:
           newlist.append(each)
    return newlist


def delete_duplicates_from_a_list6(s):
    # Finally, with out using any extra memory
    s.sort()
    print s
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            del s[i]
            print s
        else:
            i = i+1
    return s


def removeDuplicates( A):
    if not A:
        return 0

    newTail = 0
    A.sort()
    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]
            print A[newTail], A[i]
            print A

    return A[:newTail+1]



print input
#print delete_duplicates_from_a_list6(input)
print removeDuplicates(input)
