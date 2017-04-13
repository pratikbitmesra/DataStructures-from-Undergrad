
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

def createStack():
        stack = []
        return stack

def isEmpty(stack):
        return len(stack) == 0

def push(stack, item):
        stack.append(item)
        print ("Item Pushed:"+item)

def pop(stack):
        if(isEmpty(stack)):
                return str(-maxsize-1)
         return stack.pop()

def peek(stack):
        if(isEmpty(stack)):
                return str(-maxsize-1)
         return stack[len(stack)-1]        
def main():
        stack = createStack()
        push(stack, str(10))
        push(stack, str(20))
        push(stack, str(30))
        print(pop(stack) + " popped from stack")
        print("Top item is " + peek(stack))
main()
