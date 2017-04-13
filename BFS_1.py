'''
BFS Method 1 using recursion
printLevelorder(tree)
for d = 1 to height(tree)
   printGivenLevel(tree, d);

/*Function to print all nodes at a given level*/
printGivenLevel(tree, level)
if tree is NULL then return;
if level is 1, then
    print(tree->data);
else if level greater than 1, then
    printGivenLevel(tree->left, level-1);
    printGivenLevel(tree->right, level-1);
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
        else:
        # Compute the height of each subtree
            lheight = height(node.left)
            rheight = height(node.right)

            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1
            
    # Function to print level order traversal of tree
    def printLevelOrder(root):
        h = height(root)
        for i in range(1,(h+1)):
            printGivenLevel(root,i)
        
    '''
    Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    '''
 

def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    #print "Level order traversal of binary tree is -"
    Node.printLevelOrder(root)
    #height(root)
main()
            
