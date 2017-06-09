'''
Maximum and Minimum in a Binary tree

http://quiz.geeksforgeeks.org/find-maximum-or-minimum-in-binary-tree/

In Binary Search Tree, we can find maximum by traversing right pointers until we reach rightmost node. 
But in Binary Tree, we must visit every node to figure out maximum. So the idea is to traverse the given
tree and for every node return maximum of 3 values.
1) Nodes data.
2) Maximum in nodes left subtree.
3) Maximum in nodes right subtree.
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
                self.data = data
                self.left = None
                self.right = None
                
        
def find_max(root):
                 if root is None:
                        return -(sys.maxint + 1)
                 
                 res = root.data
                 print 'res:%d'%res
                 lres = find_max(root.left)
                 print 'lres:%d, node:%d'%(lres,root.data)
                 
                 rres = find_max(root.right)
                 print 'rres:%d'%rres
                 
                 if lres>res:
                        res = lres
                        print "left"
                        print " "
                 if rres>res:
                        res = rres
                        print "right"
                        print " "
                 print "Final res:%d"%res
                 return res
                    
def find_min(root):
        if root is None:
                return -(sys.maxint+1)
        res = root.data
        lres = findMin(root.left)
        rres = findMin(root.right)
        if lres<res:
                res = lres
        if rres < res:
                res = rres
        return res
def main():

        root = Node(1)
        root.left = Node(20)
        root.right = Node(201)
        root.left.left = Node(102)
        root.left.right = Node(120)
        root.right.left = Node(12)
        root.left.left.right = Node(13)
        
        
        findMax_tree = find_max(root)
main()
