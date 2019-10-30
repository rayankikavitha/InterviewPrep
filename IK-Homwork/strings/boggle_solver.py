"""
nput: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ

https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/  ( inefficient)

Expected: Trie implementation
https://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver/746102#746102

The fastest solution you're going to get will probably involve storing your dictionary in a trie.
 Then, create a queue of triplets (x, y, s), where each element in the queue corresponds to a
 prefix s of a word which can be spelled in the grid, ending at location (x, y). Initialize the queue with N x N elements
  (where N is the size of your grid), one element for each square in the grid. Then, the algorithm proceeds as follows:

While the queue is not empty:
  Dequeue a triple (x, y, s)
  For each square (x', y') with letter c adjacent to (x, y):
    If s+c is a word, output s+c
    If s+c is a prefix of a word, insert (x', y', s+c) into the queue
"""

class Node:
    def __init__(self, letter):
        self.letter=letter
        self.isTerminal=False
        self.children={}  # dictionary to store key as child letter, value as pointer address to node
        self.positions=[] # to store the order of the incoming text

class Trie():

    def __init__(self):
        self.root = Node('')

    def __str__(self):
        self.output([self.root])
        return ''


    def output(self, currentPath, indent=''):
        # Depth First Search
        currentNode = currentPath[-1]
        if currentNode.isTerminal:
            word = ''.join([node.letter for node in currentPath])
            print (indent + word + ' ' + str(currentNode.positions))
            indent += '  '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:] + [node], indent)

    def __getitem__(self, word):  # inserts a word
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True
        return current.positions

import re
def getWords(text):
    return re.sub(r'[^a-z0-9]',' ',text.lower()).split()

def MakeTrie(text):
    trie = Trie()
    words = getWords(text)
    for pos, word in enumerate(words):
        trie[word].append(pos)
    # return trie
    return trie


def BoggleWords(grid, dictpointer):
    """
    :param grid: grid words
    :param dict: trie root pointer
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])
    queue = []
    words = []

    for y in range(cols):
        for x in range(rows):
            c = grid[y][x]
            print c
            node = dictpointer.children.get(c, None)
            if node is not None:
                queue.append((x, y, c, node))
    print queue
    while queue:
        x, y, s, node = queue[0]
        del queue[0]
        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < cols and 0 <= y2 < rows:
                s2 = s + grid[y2][x2]
                node2 = node.children.get(grid[y2][x2], None)
                if node2 is not None:
                    if node2.isTerminal:
                        words.append(s2)
                    queue.append((x2, y2, s2, node2))

    return words


#Example usage:

d= MakeTrie("geeks for quiz go")
print (d)
print (d.root.children)
print BoggleWords(["giz","uek","qse"],d.root)
print BoggleWords(["giz","uek","qse"],d.root)