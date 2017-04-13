# http://quiz.geeksforgeeks.org/stack-set-1/
import os
import sys
import operator
import csv
import itertools
import math
import collections


from itertools import groupby
from sys import argv
from operator import itemgetter, attrgetter, methodcaller
from sys import maxsize

class StackNode:
        def __init__(self,data):
                self.data = data
                self.next = None

class Stack:
        def __jnit__(self):
                self.root = None
        
        def isEmpty(self):
                return True if self.root is None else False
        
        def push(self,data):
                new_node = StackNode(data)
                new_node.next = self.root
                self.root = new_node  
                print "%d Pushed item" %data      
        def pop(self):
                if (self.isEmpty()):
                        return float("-inf")
                tmp = self.root
                self.root = self.root.next
                popped = tmp.data
                return popped
        def peek(self):
                if self.isEmpty()
                        return float ("-inf")
                 return self.root.data
def main():
        stack = Stack()
        stack.push(10)        
        stack.push(20)
        stack.push(30)
         
        print "%d popped from stack" %(stack.pop())
        print "Top element is %d " %(stack.peek())

main()
