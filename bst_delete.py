# -*- coding: utf-8 -*-
"""
http://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
Created on Thu Jun 08 00:54:11 2017

@author: Pratik Mishra
"""

import sys
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,root,data):
        if root is None:
            return Node(data)
        
        # recur down the tree
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        return root
    
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print root.data
            self.inorder(root.right)
    
    def minValue(self,root):
        currentNode = self.root
        while (currentNode.left is not None):
            currentNode = currentNode.left
        return currentNode
    
    def deleteNode(self, root, data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self.deleteNode(root.left,data)
        elif data > root.data:
            root.right = self.deleteNode(root.right,data)
        else:
            # Node with one or no child
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp
            # Node with two children: Find inorder successor
            tmp = self.minValue(root.right)
            root.data = tmp.data
            #delete the successor
            root.right = self.deleteNode(root.right, tmp.data)
        return root

if __name__ == "__main__":
    classObject = BST()
    root = None
    root = classObject.insert(root, 40)
    root = classObject.insert(root, 4628)
    root = classObject.insert(root, 2)
    root = classObject.insert(root, 18)
    root = classObject.insert(root, 48)
    root = classObject.insert(root, 188)
    root = classObject.insert(root, 163638)
    root = classObject.insert(root, 4518648)
    root = classObject.insert(root, 94628)
    root = classObject.insert(root, 8)
    root = classObject.insert(root, 21)
    
    print "Inorder Tree Traversal of the given tree:"
    classObject.inorder(root)
    
    print "\Delete 21:"
    root = classObject.deleteNode(root,21)
    print "Inorder after deleting 21 or node with no children or leaf"
    classObject.inorder(root)
    
    print "\Delete 2:"
    root = classObject.deleteNode(root,2)
    print "Inorder after deleting 2 or node with one child"
    classObject.inorder(root)    
    
    print "\Delete 4628:"
    root = classObject.deleteNode(root,4628)
    print "Inorder after deleting 4628 or node with two children"
    classObject.inorder(root)    