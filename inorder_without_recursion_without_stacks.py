'''
Inorder Traversal without recursion without stack

Also known as Morris Traversal based on threaded binary tree
http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

Using Morris Traversal, we can traverse the tree without using stack and recursion. The idea of Morris Traversal is based on Threaded Binary Tree. In this traversal, we first create links to Inorder successor and print the data using these links, and finally revert the changes to restore original tree.

1. Initialize current as root 
2. While current is not NULL
   If current does not have left child
      a) Print currents data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as right child of the rightmost node in current's left subtree
      b) Go to this left child, i.e., current = current->left

'''
import os
import sys
import operator
import csv
import itertools
import math
import collections
import gc

from itertools import groupby
from sys import argv
from operator import itemgetter, attrgetter, methodcaller
from sys import maxsize

class Node:

        def __init__(self,data):
                self.data = data
                self.right = None
                self.left = None

def inorder(root):
        
        current = root
        
        while current is not None:
                if current.left is None:
                        print current.data
                        current = current.right
                else:
                        # Find the inorder predecessor of current
                        pre = current.left
                        while (pre.right is not None and pre.right is not current):
                                pre = pre.right
                                
                                if pre.right is None:
                                        pre.right = current
                                        current = current.left
                                
                                else:
                                pre.right = None
                                print current.data
                                current = current.right
                                            

def main():

        
        root = Node(1)
        root.left = Node(20)
        root.right = Node(201)
        root.left.left = Node(102)
        root.left.right = Node(120)
        root.right.left = Node(12)
        root.left.left.right = Node(13)
        

        inorder(root)
main()
