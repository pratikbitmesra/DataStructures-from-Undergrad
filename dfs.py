'''
Depth First Search- Inorder, Preorder, Postorder

http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
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
        def __init__(self, data):
                self.left = None
                self.right = None
                self.data = data

def Preorder(root):
        
        if root:
                print root.data
                Preorder(root.left)
                Preorder(root.right)

def Inorder(root):
        if root:
                Inorder(root.left)
                print root.data
                Inorder(root.right)
                
def Postorder(root):
        if root:
                Postorder(root.left)
                Postorder(root.right)
                print root.data
                
                
                
def Inorder(root):
        if root:
                Inorder(

def main():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        print "Preorder traversal of binary tree is"
        printPreorder(root)
 
        print "\nInorder traversal of binary tree is"
        printInorder(root)
 
        print "\nPostorder traversal of binary tree is"
        printPostorder(root)
main()
