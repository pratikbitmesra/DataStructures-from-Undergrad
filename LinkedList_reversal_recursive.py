# Iterate trough the linked list. In loop, change next to prev, prev to current and current to next.
# http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/
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
    #Constructor to Initializing node object 
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList_recursive_reversal:

    def __init__(self):
            self.head = None

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr

            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverse(self):
            if self.head is None:
                    return
            self.reverseUtil(self.head, None)
            
    def push(self,new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

            
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next


def main():
    llist = LinkedList_recursive_reversal()
    llist.push(20)
    llist.push(15)
    llist.push(4)
    llist.push(899)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print "Linked List"
    llist.printList()

    print "Reverse LinkedList"
    llist.reverse()
    llist.printList()

main()
