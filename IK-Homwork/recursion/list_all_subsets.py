"""
https://www.youtube.com/watch?v=NdF1QDTRkck&feature=PlayList&p=FE6E58F856038C69&index=9

Explanation:
https://stackoverflow.com/questions/728972/finding-all-the-subsets-of-a-set


for a set of n elements, get the value of 2^n. There will be 2^n no.of subsets. (2^n because each element can be either present(1) or absent(0). So for n elements there will be 2^n subsets. )
Eg. for 3 elements, say {a,b,c}, there will be 2^3=8 subsets
"""

def find_subsets(so_far, rest):
    #print 'parameters', so_far, rest
    if not rest:
        print so_far
    else:
        find_subsets(so_far + [rest[0]], rest[1:]) # include first element in the subset
        find_subsets(so_far, rest[1:])  # exclude first element in the subset

def subsets(s):
    find_subsets([],s)


print subsets('abcd')
print subsets([1,2,3])