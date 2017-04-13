'''
Diameter of a Binary Tree
http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.

The diameter of a tree T is the largest of the following quantities:

the diameter of Ts left subtree
the diameter of Ts right subtree
the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)

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


def height(node):
                if node is None:
                        return 0
                
                return 1 + max(height(node.left), height(node.right))
                
def diameter(root):
                if root is None:
                        return 0
                        
                lheight = height(root.left)
                rheight = height(root.right)
                
                ldiameter = diameter(root.left)
                rdiameter = diameter(root.right)
                
                return max(lheight+rheight+1, max(ldiameter,rdiameter))
        
        



def main():

        
        root = Node(1)
        root.left = Node(20)
        root.right = Node(201)
        root.left.left = Node(102)
        root.left.right = Node(120)
        root.right.left = Node(12)
        root.left.left.right = Node(13)
        

        
        
        print "Diameter of given binary tree is %d" %(diameter(root))
main()
