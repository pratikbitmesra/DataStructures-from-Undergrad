'''
Inorder without Recurssion
http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
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


def inorder(root):
        current = root
        s = [] #stack
        done = 0
        
        while (not done):
                if current is not None:
                        s.append(current)
                        current = current.left
                else:
                        if len(s)>0:
                                current = s.pop()
                                print current.data
                                
                                current = current.right
                                
                        else:
                                done = 1
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
