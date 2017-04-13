# LinkedList Merge Sort Simpler Version
# http://stackoverflow.com/questions/39337414/python-implementation-of-mergesort-for-linked-list-doesnt-work?rq=1

import os
import sys
import re
import operator
import csv
import itertools
import math
import collections
import fileinput
import bisect

from itertools import groupby
from sys import argv
from operator import itemgetter, attrgetter, methodcaller
from operator import add

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.data = new_data
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        tmp = self.head
        while (tmp):
            print "%d" %(tmp.data)
            tmp = tmp.next

def MergeSort(head):
    if (head is None) or (head.next is None):
        return head
    lefthalf, righthalf = splitTheList(head)

    lefthalf = MergeSort(lefthalf)
    righthalf = MergeSort(righthalf)

    return mergeTheLists(lefthalf, righthalf)

def splitTheList(sourceList):
    if (sourceList is None)or(sourceList.next is None):
        lefthalf = sourceList
        rigthalf = None

        return lefthalf, righthalf
    else:
        midPointer = sourceList
        frontRunner = sourceList.next
        while frontRunner is not None:
            frontRunner = frontRunner.next
            if frontRunner is None:
                frontRunner = frontRunner.next
                midPointer = midPointer.next

        lefthalf = sourceList
        righthalf = midPointer.next
        midPointer.next = None

        return lefthalf, righthalf

def mergeTheLists(lefthalf, righthalf):
    fakehead = Node(None)
    current = fakehead


    while lefthalf and righthalf:
        if lefthalf.data < righthalf.data:
            current.next = lefthalf
            lefthalf = lefthalf.next
        else:
            current.next = righthalf
            righthalf = righthalf.next

        current = current.next

        if lefthalf is None:
            current.next = righthalf

        elif righthalf is None:
            current.next = lefthalf

        return fakehead.next
            

def main():
   llist1 = LinkedList()
   llist1.push(6)
   llist1.push(7)
   llist1.push(1)
   llist1.push(4)
   llist1.push(3)
   llist1.push(8)
   print "Sorted list"
   new_head = MergeSort(llist1.head)
   llist1.printList()
main()
