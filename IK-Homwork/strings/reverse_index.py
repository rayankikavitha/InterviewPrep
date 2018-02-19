"""
Given a text file and a word, find the positions where word occurs in the file.
You will be asked to find the positions of many words in the same file. i.e think precomputing with a reverse index.
Implement the solution with a Hashtable and Trie. Write full implementation of a Trie.

Solution: http://www.ardendertat.com/2011/12/20/programming-interview-questions-23-find-word-positions-in-text/

#!/usr/bin/python

filename = "myfile.txt"
with open( filename ) as f:
    # file read can happen here
    # print "file exists"
    print f.readlines()

with open( filename, "w") as f:
    # print "file write happening here"
    f.write("write something here ")
"""

# using dictionary
# o(n) - creating an index, querying an index
# o(n) - space n-words
#
import re
import collections
def getWords(text):
    return re.sub(r'[^a-z0-9]',' ',text.lower()).split()

def createIndex1(text):
    index=collections.defaultdict(list)
    words=getWords(text)
    for pos, word in enumerate(words):
        index[word].append(pos)
    return index

def queryIndex1(index, word):
    if word in index:
        return index[word]
    else:
        return []

# Trie implementation
# optimizing hash, image used, useful, user, requres (14) spaces in hash, where as in trie (8) spaces

class Node:
    def __init__(self, letter):
        self.letter=letter
        self.isTerminal=False
        self.children={}  # dictionary to store key as child letter, value as pointer address to node
        self.positions=[] # to store the order of the incoming text

def stringMatching(r,i,s,j):
    """

    :param r:  reg expression string like a.c for abc or a*bc for abc
    :param i:   index of r
    :param s:  string
    :param j: index of s
    :return:  True /False
    """
    # if i reached the end, j has to reach end too.
    if i == len(r):
        return j == len(s)
    if j != len(s) and (r[i] == s[j] or r[i] =='.'):  # . any one character, then increment both indexes.
        return stringMatching(r,i+1,s,j+1)
    return False

class Trie:
    def __init__(self):
        self.root = Node('')

    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isTerminal

    def contains(self, word, start= None, i = 0): # takes care of regular expression search for '.'
        if start == None:
            current = self.root
        else:
            current = start
        print current.letter,current.children
        while i < len(word):
            print word[i],i
            if word[i] == '.':
                return self.contains(word, start = current.children, i=i+1)

            if word[i] not in current.children:
                return False
            current = current.children[word[i]]
        return current.isTerminal


    def __getitem__(self, word):# inserts a word
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True
        return current.positions

    def __str__(self):
        self.output([self.root])
        return ''

    def output(self, currentPath, indent=''):
        # Depth First Search
        currentNode = currentPath[-1]
        if currentNode.isTerminal:
            word = ''.join([node.letter for node in currentPath])
            print indent + word + ' ' + str(currentNode.positions)
            indent += '  '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:] + [node], indent)



def createIndex2(text):
    trie = Trie()
    words = getWords(text)
    for pos, word in enumerate(words):
        trie[word].append(pos)
    return trie


def queryIndex2(index, word):
    if word in index:
        return index[word]
    else:
        return []

t=createIndex2("abc abcc abd use used useful user username using us utah")
print t
#t.__getitem__("amazing")
#print t
print t.contains("utah",)
print t.__contains__("utah")
#print queryIndex2(t, "useful")