'''
http://www.geeksforgeeks.org/sort-a-stack-using-recursion/

Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed. 
We can only use the following ADT functions on Stack S:

is_empty(S)  : Tests whether stack is empty or not.
push(S)	     : Adds new element to the stack.
pop(S)	     : Removes top element from the stack.
top(S)	     : Returns value of the top element. Note that this
               function does not remove element from the stack.
'''
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

def push(stack,data):
        stack.append(data)
        
def isEmpty(stack):
        return len(stack) == 0

def pop(stack):
        if isEmpty(stack) == True:
                print "Overflow"                                
                exit(1)
                   
        return stack.pop()
        
def top(stack):
        return stack[-1]


def printStack(stack):
        for i in stack:
                print i   
                
def isGreater(a, b):
        return a>b == 1

def flush(temp, output):
        if isEmpty(temp) is False:
                push(output, pop(temp))
                flush(temp,output)

def sortedInsert(stack, x):
        
        if isEmpty(stack) or x>top(stack):
                push(stack,x)
                return
               
        temp = pop(stack)
        sortedInsert(stack,x)
        push(stack, temp)     
        
def sort(input_stack):
        if isEmpty(input_stack) is False:
                x = pop(input_stack)
                #print "X before:%s" %x
                # Sort remaining items
                sort(input_stack)
                #print "X after:%s" %x
                # push item back in sorted stack
                sortedInsert(input_stack, x)
                
        
                                

def main():
       s = createStack()
       #k = createStack()
       push(s, 10)
       push(s, 2348023)
       push(s, 120)       
       push(s, 341234)
       #print " Original"
       printStack(s)
       sort(s)
       #print "Sorted"
       printStack(s)         

main()
