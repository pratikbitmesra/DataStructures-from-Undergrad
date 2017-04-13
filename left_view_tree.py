'''
Print Left view

http://www.geeksforgeeks.org/print-left-view-binary-tree/

Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from left side. Left view of following tree is 12, 10, 25.

          12
       /     \
     10       30
            /    \
          25      40 
The left view contains all nodes that are first nodes in their levels.
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
                self.left = None
                self.right = None

def leftViewUtil(root, level, max_level):
        if root is None:
                return
         
        if max_level[0]<level:
                print "%d\t"%(root.data)
                max_level[0] = level   
        
        print "root:%d" %root.data             
        leftViewUtil(root.left,level+1,max_level)
        print "root.left:%d"%root.data
        leftViewUtil(root.right,level+1,max_level)
        print "root.right:%d" %root.data
        
def left_view(root):
        max_level = [0]
        leftViewUtil(root,1,max_level)        

def main():

        root = Node(1)
        root.left = Node(20)
        root.right = Node(201)
        root.left.left = Node(102)
        root.left.right = Node(120)
        root.right.left = Node(12)
        root.left.left.right = Node(13)
        
        
        left_view(root)
main()
