"""
You are given a dictionary of words and two strings , start and stop
You can convert string start to stop by changing only one character at a time and making sure
1) all intermediate words are in the given dictionary of words
2) min number of intermediate words are used

Example input : [cat,hat,bad,had]
start = "bat", stop = had
output =[bat,bad,had] or [bat,hat,had]
following program returns count only :
https://leetcode.com/problems/word-ladder/description/
other problem word_ladder returns all the strings
concept : BFS on graph. Nodes are words, edges exists between nodes, if they differe atmost 1 character


"""
def findLadders(dict, start, end,):
    dict.append(start)
    dict.append(end)

    result =[] # to store results
    cur = [start]  # like a queue
    visited = set([start])
    found = False
    trace = {word:[] for word in dict}

    while cur and not found:
        for word in cur:
            visited.add(word)

        next = set()
        for word in cur:
            for i in xrange(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + j + word[i + 1:]
                    if candidate not in visited and candidate in dict:
                        if candidate == end:
                            found = True
                        next.add(candidate)
                        trace[candidate].append(word)
        cur = next
    print result, trace
    if found:
        backtrack(result, trace, [], end)

    return result





input = ["cat","hat","bad","had"]
start,stop = "bat", "had"
#output =[bat,bad,had] or [bat,hat,had]
#print word_ladder(input, start, stop)
#print word_ladder(["hot", "dot", "dog", "lot", "log"],"hit","cog")

def ladderlength(wordlist, start, end):
    wordlist.append(end)
    wordlist.append(start)
    queue =[]  # to visit
    addnextwords(start, wordlist,queue)
    print queue
    dist = 2
    while queue:
        num = len(queue)
        for i in range(num):
            word = queue.pop(0)
            if word == end:
                return dist
            addnextwords(word, wordlist, queue)
        dist += 1
    return dist

def addnextwords(word, wordlist,queue_tovisit):
    wordlist.remove(word)
    for i in range(len(word)):
        for j in 'abcdefghijklmnopqrstuvwxyz':
            candidate = word[:i] + j + word[i + 1:]
            if candidate in wordlist:
                queue_tovisit.append(candidate)
                wordlist.remove(candidate)

print ladderlength(input,start,stop)
