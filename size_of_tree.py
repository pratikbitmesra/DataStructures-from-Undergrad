'''
http://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/

Size of a tree is the number of elements present in the tree. 
Size of a tree = Size of left subtree + 1 + Size of right subtree

Algorithm:

size(tree)
1. If tree is empty then return 0
2. Else
     (a) Get the size of left subtree recursively  i.e., call 
          size( tree->left-subtree)
     (a) Get the size of right subtree recursively  i.e., call 
          size( tree->right-subtree)
     (c) Calculate size of the tree as following:
            tree_size  =  size(left-subtree) + size(right-
                               subtree) + 1
     (d) Return tree_size
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
        
        def __init(self,data):
                self.data = data
                self.left = left
                self.right = right
def size(root):
        if root is None:
                return 0
         else:
                return (size(root.left) + 1 + size(root.right))

def main():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left  = Node(4)
        root.left.right = Node(5)
         
        print "Size of the tree is %d" %(size(root))
 

main()
