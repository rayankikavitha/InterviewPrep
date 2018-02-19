"""
https://discuss.leetcode.com/topic/8592/comparably-concise-java-code


Use the DFS helper function to find solutions recursively.
A solution will be found when the length of queens is equal to n ( queens is a list of the indices of the queens).

In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) where p + q == x + y or p - q == x - y would be invalid.
We can use this information to keep track of the indicators (xy_dif and xy_sum ) of the invalid positions and then call DFS recursively with valid positions only.


use "p + q == x + y or p - q == x - y" is fine. "p - q == x - y" is used to check no other queens on diagonal 1 (left top to right bottom), and "p + q == x + y" for diagonal 2 (right top to left bottom).

and the list queens, can make sure every col/row only contains one queen.

"""

def solveNQueens( n):
    def DFS(queens, xy_dif, xy_sum):
        #print "in DFS"
        #print queens, xy_dif, xy_sum
        #print result
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            # first condition makes sure it is not in the same column
            # second condition and third condition for diagonal elimination
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    result = []
    DFS([],[],[])
    #print "final result"
    #print result
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

print solveNQueens(4)