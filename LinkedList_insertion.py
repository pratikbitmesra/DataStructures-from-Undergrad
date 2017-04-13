# LinkedList Insertion
# http://quiz.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
# At the front of the LinkedList
# After a given node
# At the end of the LinkedList
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
    #Initialize the node object
    def __init__(self,data):
        self.data = data
        self.next = None

# LinkedList class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Insert at beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head # Make next of new ndoe as head
        self.head = new_node

    # Inserts a node at a given location or in between two nodes
    def insertAfter(self,prev_node, new_data):

        if prev_node is None:
            print "Node doesnt exists"
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #Insert at the end
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    #Print all nodes
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

def main():
 # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
 
    print 'Created linked list is:',
    llist.printLinkedList()
main()
