"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""

from typing import *

class TrieNode:

    def __init__(self):
        self.__isWord = False
        self.__links = {}

    def isWord(self) -> bool:
        return self.__isWord
    
    def setWord(self) -> None:
        self.__isWord = True

    def getKey(self, char: str) -> Optional['TrieNode']:
        return self.__links.get(char)

    def putKey(self, char: str, node: 'TrieNode') -> 'TrieNode':
        self.__links[char] = node
        return node
    
    def iterLinks(self):
        for c, n in self.__links.items():
            yield c, n


class Trie:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.__root
        for c in word:
            key = currNode.getKey(c)
            if key:
                currNode = key
            else:
                currNode = currNode.putKey(c, TrieNode())
        currNode.setWord()

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie where 
        word may contain dots '.' to match any character
        """
        def helper(node, word):
            for i,c in enumerate(word):
                if c == ".":
                    possibles = [n for c,n in node.iterLinks()]
                    for n in possibles:
                        if helper(n, word[i+1:]): return True
                    return False
                else:
                    key = node.getKey(c)
                    if key:
                        # continue search starting from this node
                        return helper(key, word[i+1:])
                    else:
                        return False
            # Reach end of search string
            if node.isWord():
                return True
            return False

        return helper(self.__root, word)
    

class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        return self.trie.search(word)