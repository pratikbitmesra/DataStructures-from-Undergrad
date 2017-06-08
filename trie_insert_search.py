# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 11:30:14 2017
http://www.geeksforgeeks.org/trie-insert-and-search/
@author: Pratik Mishra
"""

import os
import sys

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class Trie:
    
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    def charToIndex(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self,key):
    
        traverse = self.root
        
        for level in range(len(key)):
            index = self.charToIndex(key[level])
            if not traverse.children[index]:
                traverse.children[index] = self.getNode()
            traverse = traverse.children[index]
        traverse.isLeaf = True
            
        
    def search(self,key):
        traverse = self.root
        for level in range(len(key)):
            index = self.charToIndex(key[level])
            if not traverse.children[index]:
                return False
            traverse = traverse.children[index]
        return traverse != None and traverse.isLeaf
    
def main():
    
    keys = ["kudzie","wants","to","eat","foodie"]
    output = ["Not Present","Present"]
    
    trie_obj = Trie()
    
    for key in keys:
        trie_obj.insert(key)
    finding_terms = ["ud","to","food"]
    
    for finds in finding_terms:
        print ("%s is %s"%(finds,output[trie_obj.search(finds)]))
if __name__ == "__main__":
    main()
