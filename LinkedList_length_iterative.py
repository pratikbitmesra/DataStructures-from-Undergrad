#Find length of a Linked List iteratively
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

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCount_iterative(self):
        tmp = self.head
        count = 0

        while (tmp):
            count = count + 1
            tmp = tmp.next
        return count

    ###Recursive Count

    def rec(self,node):
        if (not node):
            return 0
        else:
            return 1+ self.rec(node.next)

    def getrec(self):
        return self.rec(self.head)
    ###

def main():
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)

    print "Iterative Count of nodes is :%s" %llist.getCount_iterative()   
    print "Recursive Count of nodes is :%s" %llist.getrec() 
main()
