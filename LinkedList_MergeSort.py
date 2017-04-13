# Merge Sort using LinkedList Merge Sort
# http://www.geeksforgeeks.org/merge-sort-for-linked-list/
# MergeSort(headRef)
#1) If head is NULL or there is only one element in the Linked List 
#    then return.
#2) Else divide the linked list into two halves.  
#      FrontBackSplit(head, &a, &b); /* a and b are two halves */
#3) Sort the two halves a and b.
#      MergeSort(a);
#      MergeSort(b);
#4) Merge the sorted a and b (using SortedMerge() discussed here) 
#   and update the head pointer using headRef.
#     *headRef = SortedMerge(a, b);
# http://stackoverflow.com/questions/34874312/merge-sort-for-linked-list-implementation-in-python-is-not-working
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
        
 
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.data = new_data
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        tmp = self.head
        while (tmp):
            print "%d" %(tmp.data)
            tmp = tmp.next
            
def Mergesort(head):
##        head = self.head
##        a = LinkedList()
##        b = LinkedList()
    if (head is None) or (head.next is None):
        return
    a,b = FrontBackSplit(head)
    Mergesort(a)
    Mergesort(b)
    new_head = SortedMerge(a, b)
    return new_head

def SortedMerge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    s = t= Node(None)

    while (head1 and head2):
        if (head1.data<= head2.data):
            c = head1
            head1 = head1.next
        else:
            c = head2
            head2 = head2.next

        t.next = c
        t = t.next

    t.next = head1 or head2
    return s.next
##    Split the nodes of the given list into front and back halves,
##    and return the two lists using the reference parameters.
##    If the length is odd, the extra node should go in the front list.
##    Uses the fast/slow pointer strategy.

def FrontBackSplit(head):
    if head is None or head.next is None:
        head1 = head
        head2 = None
    else:
        slow = head
        fast = head.next
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
    head1 = head
    head2 = slow.next
    slow.next = None

    return head1, head2


def main():
   llist1 = LinkedList()
   llist1.push(6)
   llist1.push(7)
   llist1.push(1)
   llist1.push(4)
   llist1.push(3)
   llist1.push(8)
   print "Sorted list"
   new_head = Mergesort(llist1.head)
   llist1.printList()
main()
