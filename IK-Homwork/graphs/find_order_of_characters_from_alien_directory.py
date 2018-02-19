"""
https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs

Given a sorted dictionary of an alien language. You have to find the order of characters in that language.
(This a popular interview problem)

Input Format:

There is only one argument, array of strings which denotes sorted dictionary of an alien language.

Output Format:

Return a string denoting order of characters in the alien language.

Length of the output string will be the number of different characters present in input dictionary.

For more clarity see the sample test cases.

Constraints:

1 <= total number of characters in dictionary (not words) <= 10^5
Character in any word will be lower case alphabet letter.
Input will be such that it is possible to determine the order uniquely.

Sample Test Cases:

Sample Input1:

words = ["baa", "abcd", "abca", "cab", "cad"]

Sample Output1:

"bdac"

Sample Input2:

words = ["caa", "aaa", "aab"]

Sample Output2:

"cab"

Notes:

Maximum time allowed in interview: 20 Minutes.

Here input is given such that it is possible to determine order uniquely.
But in interview you should clarify these things with interviewer. Like if we are given words = ["z" "bc"] then we can
only conclude that 'z' will come before 'b', but nothing about the order of 'c'!

"""

def alienOrder(words):

    result = ""
    if not words or len(words) == 0:
        return result
    graph = {} # adjency dictionary to store node and their related nodes
    degree = {}
    for word in words:
        for c in word:
            degree[c] = 0
    print graph
    print degree

    #build graph
    for i in range(len(words)-1):
        cur = words[i]
        next = words[i+1]
        minlen = min(len(cur),len(next))
        for j in range(minlen):
            c1 = cur[j]
            c2 = next[j]
            if c1 != c2:
                charset = set()
                if graph.get(c1,None):
                    charset = graph.get(c1,None)
                #print charset
                if c2 not in charset:
                    charset.add(c2)
                    graph[c1]=charset
                    degree[c2]= degree.get(c2,0) +1
                #print degree
                break
    print graph
    print degree
    # queue for dfs
    q = []
    for key in degree.keys():
        if degree[key] == 0:
            q.append(key)
    #print "degree"
    #print degree
    #print "graph"
    #print graph
    #print q
    while q:
        c = q.pop(0)
        result += c
        #print result,c
        if c in graph:
            for each_char in graph[c]:
                degree[each_char] = degree[each_char] - 1
                if degree[each_char] == 0 :
                    q.append(each_char)

    if len(result) != len(degree): return ""
    return result


print alienOrder(["baa", "abcd", "abca", "cab", "cad"])