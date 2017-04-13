#LinkedList Node Deletion
# http://quiz.geeksforgeeks.org/linked-list-set-3-deleting-node/
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
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurence of key in linked list

    def deleteNode(self,key):

        tmp = self.head

        while (tmp is not None):
            if (tmp.data == key):
                break
            prev = tmp
            tmp = tmp.next
        if (tmp == None):
            return
        prev.next = tmp.next
        tmp = None

    def printList(self):
        tmp = self.head
        while (tmp):
            print "%d" %(tmp.data)
            tmp = tmp.next
        
def main():
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
     
    print "Created Linked List: "
    llist.printList()
    llist.deleteNode(1) 
    print "\nLinked List after Deletion of 1:"
    llist.printList()

main()
