# Delete a Linked List node at a given position
# Given a singly linked list and a position,
# delete a linked list node at the given position.
# http://quiz.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/
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
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,position):

        #If LL is empty
        if self.head == None:
            return
        tmp = self.head

        if position == 0:
            self.head = tmp.next
            tmp = None
            return

        for i in range(position -1):
            tmp = tmp.next
            if tmp is None:
                break

        if tmp is None:
            return
        if tmp.next is None:
            return

        next = tmp.next.next

        tmp.next = None
        tmp.next = next

    def printList(self):
        tmp = self.head
        while(tmp):
            print "%d" %(tmp.data)
            tmp = tmp.next


def main():
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)
     
    print "Created Linked List: "
    llist.printList()
    llist.deleteNode(4)
    print "\nLinked List after Deletion at position 4: "
    llist.printList()
main()
