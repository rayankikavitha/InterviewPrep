import unittest

class TrieNode:
    def __init__(self, letter):
        self.letter=letter
        self.isTerminal=False
        self.children={}  # dictionary to store key as child letter, value as pointer address to node
        self.positions=[] # to store the order of the incoming text


class Trie(TrieNode):

    # Implement a trie and use it to efficiently store strings
    def __init__(self):
        self.root_node=TrieNode('')
        self.wordcount = 0
        
    def __contains__(self,word):
        curr_node = self.root_node
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        if not curr_node.isTerminal:
            return 'prefix of existing word'
        else:
            return 'word already present'
        

    def add_word(self, word):
        status = self.__contains__(word)
        print status
        if not status:
            current_node = self.root_node
            for char in word:
                if char not in current_node.children:
                    current_node.children[char]=TrieNode('')
                current_node = current_node.children[char]
            current_node.isTerminal=True
            self.wordcount += 1
            return 'new word '+ str(self.wordcount)
        elif status == 'prefix of existing word':
            current_node = self.root_node
            for char in word:
                current_node = current_node.children[char]
            current_node.isTerminal = True
            self.wordcount +=1
            status = 'word already present'
        else:
            return status
        









# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)