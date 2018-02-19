
"""
# returns count of steps
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
from collections import deque
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        def construct_dict(word_list):
            """Creates a map of all combinations of words with missing letters mapped
            to all words in the list that match that pattern.
             E.g. hot -> {'_ot': ['hot'], 'h_t': ['hot'], 'ho_': ['hot']}
            """
            d = collections.defaultdict(list)
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s].append(word)
            return d

        def bfs_words(begin, end, dict_words):
            queue = deque([(begin, 1)]) # add being word as step 1
            visited = set()
            while queue:
                # Get the next node to explore from the top of the queue
                word, steps = queue.popleft()
                if word not in visited:
                    if word == end:
                        return steps
                    visited.add(word)
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words[s]
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        #print wordList | set([beginWord, endWord])

        d = construct_dict(wordList+[beginWord, endWord])
        return bfs_words(beginWord, endWord, d)

input = ["cat","hat","bad","had"]
start,stop = "bat", "had"
sol = Solution()
print sol.ladderLength(start, stop,input)


