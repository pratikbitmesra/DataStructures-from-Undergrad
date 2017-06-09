# -*- coding: utf-8 -*-
"""
http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
Created on Wed Jun 07 18:17:17 2010

@author: Pratik Mishra
"""
import os
import sys

max = sys.maxsize
min = -sys.maxsize

class Node:
    
    def __init__(self,data):
        self.rchild = None
        self.lchild = None
        self.data = data

class BST:  

               
    def binary_insert(self,root,node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.lchild is None:
                    root.lchild = node
                else:
                    self.binary_insert(root.lchild,node)
                    
            else:
                if root.rchild is None:
                    root.rchild = node
                else:
                    self.binary_insert(root.rchild,node)
        
    def inorder_traversal(self,root):
        if not root:
            return
        self.inorder_traversal(root.lchild)
        print root.data
        self.inorder_traversal(root.rchild)
    
    def preorder_traversal(self,root):
        if not root:
            return
        print root.data
        self.preorder_traversal(root.lchild)
        self.preorder_traversal(root.rchild)
        
    def isBST(self,node):
       return (self.isBSTUtil(node, min, max))
    
    def isBSTUtil(self,node,mini,maxi):
        
        if node is None:
            return True
        
        if node.data < mini or node.data> maxi:
            return False
        
        
        print node.data
        return (self.isBSTUtil(node.lchild, mini, node.data-1) and self.isBSTUtil(node.rchild, node.data+1,max))
        
        

if __name__ == "__main__":
    
    root = Node(20)
    binary = BST()
    binary.binary_insert(root,Node(732))
    binary.binary_insert(root,Node(12))
    binary.binary_insert(root,Node(32))
    binary.binary_insert(root,Node(2))
    
    print "In-order Tree:"
    binary.inorder_traversal(root)
    
    print "PreOrder Tree:"
    binary.preorder_traversal(root)
    
    root = Node(20)
    root.rchild = Node(732)
    root.lchild = Node(12)
    root.rchild.lchild = Node(32)
    root.lchild.lchild = Node(2)
    #binary1 = BST()
    if (binary.isBST(root)):
        print "BST"
    else:
        print "Not BST"
