"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
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
    
    def getAllWords(self) -> List[str]:
        path, res = [], []
        def dfs(node: 'TrieNode', path: List[str]) -> None:
            if node.isWord():
                res.append(''.join(path))
            else:
                for c, n in node.iterLinks():
                    path.append(c)
                    dfs(n, path)
            path.pop()
            
        for c, n in self.__links.items():
            path.append(c)
            dfs(n, path)

        return res
                
            
class Trie:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.__root
        for c in list(word):
            key = currNode.getKey(c)
            if key:
                currNode = key
            else:
                currNode = currNode.putKey(c, TrieNode())
        currNode.setWord()

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie
        """
        currNode = self.__root
        for c in list(word):
            key = currNode.getKey(c)
            if key:
                currNode = key
            else:
                return False
        if currNode.isWord():
            return True
        # word is prefix of another added string
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the given prefix
        """
        currNode = self.__root
        for c in list(prefix):
            key = currNode.getKey(c)
            if key:
                currNode = key
            else:
                return False
        return True
    
    def prefixOf(self, prefix: str) -> List[str]:
        """
        Returns a list of all words in the trie with the given prefix 
        """
        currNode = self.__root
        for c in list(prefix):
            key = currNode.getKey(c)
            if key:
                currNode = key
            else:
                return []
            
        return [prefix + x for x in currNode.getAllWords()]
        

def main(strings: List[str], query: str) -> List[str]:
    trie = Trie()
    for s in strings:
        trie.insert(s)
    
    return trie.prefixOf(query)


if __name__ == "__main__":
    assert main(["dog", "deer", "deal"], "de") == ["deer", "deal"]
    assert main(["cat", "car", "caa"], "ca") == ["cat", "car", "caa"]
    assert main(["cat", "car", "cer"], "yy") == []
    
    