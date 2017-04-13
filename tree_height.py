'''
http://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
maxDepth()
1. If tree is empty then return 0
2. Else
     (a) Get the max depth of left subtree recursively  i.e., 
          call maxDepth( tree->left-subtree)
     (a) Get the max depth of right subtree recursively  i.e., 
          call maxDepth( tree->right-subtree)
     (c) Get the max of max depths of left and right 
          subtrees and add 1 to it for the current node.
         max_depth = max(max dept of left subtree,  
                             max depth of right subtree) 
                             + 1
     (d) Return max_depth

      maxDepth('1') = max(maxDepth('2'), maxDepth('3')) + 1
                               = 2 + 1
                                  /    \
                                /         \
                              /             \
                            /                 \
                          /                     \
               maxDepth('1')                  maxDepth('3') = 1
= max(maxDepth('4'), maxDepth('5')) + 1
= 1 + 1   = 2         
                   /    \
                 /        \
               /            \
             /                \
           /                    \
 maxDepth('4') = 1     maxDepth('5') = 1
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

# A binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
            print node
            if node is None:
                
                return 0
            else:
                
                lDepth = maxDepth(node.left)
                print 'ldept:%d'%lDepth
                rDepth = maxDepth(node.right)
                print 'rdepth:%d' %rDepth

                if lDepth > rDepth:
                    print 'left'
                    return lDepth+1
                else:
                    print 'right'
                    return rDepth+1
    

def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(8)
    root.left.left = Node(4)
    root.left.left.left = Node(7)
    root.left.right = Node(5)
    root.left.right.right = Node(6)


    print 'Height of tree: %d' %(maxDepth(root))
main()
