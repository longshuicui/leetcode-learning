# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :  2021/02/13
@function:
208. Implement Trie (Prefix Tree) (Meidum)
https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Trie:
    def __init__(self):
        self.root={}
        self.end=-1

    def insert(self, word):
        curNode=self.root
        for c in word:
            if c not in curNode:
                curNode[c]={}
            curNode=curNode[c]
        curNode[self.end]=True

    def search(self,word):
        curNode=self.root
        for c in word:
            if c not in curNode:
                return False
            curNode=curNode[c]
        if self.end not in curNode:
            return False
        return True

    def startsWith(self, prefix):
        curNode=self.root
        for c in prefix:
            if c not in curNode:
                return False
            curNode=curNode[c]
        return True


trie=Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
