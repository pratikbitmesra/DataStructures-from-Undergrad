# -*- coding: cp1252 -*-
'''
BFS_2 Method 2
http://www.geeksforgeeks.org/level-order-tree-traversal/
For each node, first the node is visited and then it’s child nodes are put in a FIFO queue.
printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root 
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children (first left then right children) to q
    c) Dequeue a node from q and assign it’s value to temp_node
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

def printLevelOrder(root):

    if root is None:
        return
    queue = []
    queue.append(root)

    while len(queue)>0:
        print queue[0].data
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    print "Level Order Traversal of binary tree is -"
    printLevelOrder(root)
main()
