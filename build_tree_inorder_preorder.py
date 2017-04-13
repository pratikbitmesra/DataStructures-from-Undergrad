'''
Build a tree from INorder and Preorder

Let us consider the below traversals:

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F

In a Preorder sequence, leftmost element is the root of the tree. So we know ‘A’ is root for given sequences. By searching ‘A’ in Inorder sequence, we can find out all elements on left side of ‘A’ are in left subtree and elements on right are in right subtree. So we know below structure now.

                 A
               /   \
             /       \
           D B E     F C
We recursively follow above steps and get the following tree.

         A
       /   \
     /       \
    B         C
   / \        /
 /     \    /
D       E  F
Algorithm: buildTree()
1) Pick an element from Preorder. Increment a Preorder Index Variable (preIndex in below code) to pick next element in next recursive call.
2) Create a new tree node tNode with the data as picked element.
3) Find the picked element’s index in Inorder. Let the index be inIndex.
4) Call buildTree for elements before inIndex and make the built tree as left subtree of tNode.
5) Call buildTree for elements after inIndex and make the built tree as right subtree of tNode.
6) return tNode.

For Inorder and Postorder, refer http://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/
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
"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of inStrt and inEnd should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """
def buildTree(inorder, preorder, in_start, in_end):
        if in_start > in_end:
                return None
        
        """" Pick current Node from Preorder traversal using preIndex and incremented preindex"""
        tempNode = Node(preorder[buildTree.preIndex])
        buildTree.preindex += 1
        
        if in_start == in_end:
                return tempNode

        inIndex = search(inorder, preorder, in_start, in_end, tempNode.data)
        
        tempNode.left = buildTree(inorder, preorder, in_start, inIndex-1)
        tempNode.right = buildTree(inorder, preorder, inIndex+1, in_end)
        
def search(arr, start, end, value):
        for i in range(start, end+1):
                if arr[i] == value:
                        return i

def printInorder(node):
        if node is None:
                return
                
                printInorder(node.left)
                print node.data
                printInorder(node.right)       



def main():

        inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
        preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
        # Static variable preIndex
        buildTree.preIndex = 0
        root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
         
        # Let us test the build tree by priting Inorder traversal
        print "Inorder traversal of the constructed tree is"
        printInorder(root)
main()
