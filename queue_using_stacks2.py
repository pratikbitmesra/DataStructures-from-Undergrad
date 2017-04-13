'''
Implement Queue as Stack- Method 2
http://www.geeksforgeeks.org/queue-using-stacks/

Method 1 (By making enQueue operation costly) 
This method 
makes sure that oldest entered element is always at the 
top of stack 1, so that deQueue operation just pops from stack1. 
To put the element at top of stack1, stack2 is used.

enQueue(q, x)
  1) While stack1 is not empty, push everything from satck1 to stack2.
  2) Push x to stack1 (assuming size of stacks is unlimited).
  3) Push everything back to stack1.

dnQueue(q)
  1) If stack1 is empty then error
  2) Pop an item from stack1 and return it

Method 2 (By making deQueue operation costly)
In this method, in en-queue operation, 
the new element is entered at the top of stack1. In de-queue operation, if stack2 
is empty then all the elements are moved to stack2 and finally top of stack2 is returned.

enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
Method 2 is definitely better than method 1.
Method 1 moves all the elements twice in enQueue operation, while method 2 
(in deQueue operation) moves the elements once and moves elements only if stack2 empty.
Implementation of method 2:
'''
import os
import sys
import operator
import csv
import itertools
import math
import collections
import gc

from itertools import groupby
from sys import argv
from operator import itemgetter, attrgetter, methodcaller
from sys import maxsize

class Stack_Node:
        def __init__(self):
                self.next = None
                self.data = []
        
        def push(self, item):
                return self.data.append(item)
                
        def pop(self):
                return self.data.pop()
        
        def size(self):
                return len(self.data)
        
        def isEmpty(self):
                return self.size() == 0
                
class Queue:
        def __init__(self):
                self.instack = Stack_Node()
                self.outstack = Stack_Node()

        def  enQueue(self, item):
                self.instack.push(item)      
        
        def deQueue(self):
                if not self.outstack:
                        while self.instack:
                                self.outstack.append(self.instack.pop())
                return self.outstack.pop()
                
                 
def main():
        q = Queue()
        for i in range(10):
            q.enQueue(i)
        for i in xrange(10):
            print q.deQueue()        
main()




























































































