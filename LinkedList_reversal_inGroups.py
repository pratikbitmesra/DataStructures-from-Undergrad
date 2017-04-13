# Reverse a Linked List in groups of given size
# Given a linked list, write a function to reverse every k nodes
# (where k is an input to the function)
# http://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
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

    def reverseinGroups(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current . And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverseinGroups(next,k)

        return prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.data = new_data
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        tmp = self.head
        while(tmp):
            print tmp.data
            tmp = tmp.next


def main():
    llist = LinkedList()
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
     
    print "Given linked list"
    llist.printList()
    llist.head = llist.reverseinGroups(llist.head, 3)
     
    print "\nReversed Linked list"
    llist.printList()
main()
