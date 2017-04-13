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

class LinkedList_reverse:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next


def main():
    llist = LinkedList_reverse()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print "Given Linked List"
    llist.printList()
    llist.reverse()
    print "\nReversed LinedList"
    llist.printList()
    

main()
