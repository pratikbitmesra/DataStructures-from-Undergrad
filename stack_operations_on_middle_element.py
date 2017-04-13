'''Design a stack with operations on middle element
How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.
http://www.geeksforgeeks.org/design-a-stack-with-find-middle-operation/
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

# Using double LinkedList
class DDLNode:
        def __init__(self, data):
                self.prev = None
                self.next = None
                self.data = data

class Stack:
        def __init__(self):
                self.head = None
                self.mid = None
                self.count = 0
        
        def push(self, new_data):
                new_node = DDLNode(new_data)
                new_node.data = new_data
                new_node.prev = None
                new_node.next = self.head
                self.count += 1
                
                if self.count == 1:
                        self.mid = new_node
                else:
                        self.head.prev = new_node
                        # Update mid if count is odd
                        if (self.count and 1):
                                self.mid = self.mid.prev
                        
                self.head = new_node
                                
        def pop(self):
                if self.count == 0:
                        print "Overflow"
                        return -1
                item = self.head.data
                self.head = self.head.next
                
                # If Linked list doesnt become empty
                if self.head is not None:
                        self.head.prev = None
                self.count -=1
                
                gc.collect()    
                
                # Update mid pointer when even number of elements in stack, i.e. move down th
                # mid pointer
                
                if (self.mid and 1) == False:
                        self.mid = self.mid.next
                return item      
                
        def findMiddle(self):
                if self.count == 0:
                        print "Stack Empty"
                        return -1
                return self.mid.data                                                             
                        
def main():
        
        stack_dll = Stack()
        print "1. Middle Element:%s"%stack_dll.findMiddle()
        stack_dll.push(1212)
        stack_dll.push(231313)
        print "2. Middle Element:%s"%stack_dll.findMiddle()
        stack_dll.push(463128364)  
        stack_dll.push(4631)
        
        print "Middle Element:%s"%stack_dll.findMiddle()
        print "Pop:%s"%stack_dll.pop()
        print "Middle Element after pop:%s"%stack_dll.findMiddle()
               
main()                

