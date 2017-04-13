#Linked List traversal
# A simple Python program for traversal of a linked list
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

# Node class
class Node:
    #Function to initialize the node object
    def __init__(self,data):
        self.data = data # data assignment
        self.next = None # Initialize next as NULL

# LinkedList class contains a Node object
class LinkedList:

    #Function to initialize head
    def __init__(self):
        self.head = None
    print 'Hi'
    #print contents of a linkedlist

    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

if __name__=='main':

    llist = LinkedList()
    llist.head = Node(10)
    second = Node(20)
    third = Node(30)
    llist.head.next = second
    second.next = third

    llist.printList()
