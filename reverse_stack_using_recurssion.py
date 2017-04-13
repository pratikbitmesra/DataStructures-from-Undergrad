'''Reverse a stack using recursion
You are not allowed to use loop constructs like while, for..etc, 
and you can only use the following ADT functions on Stack S:
isEmpty(S)
push(S)
pop(S)
http://www.geeksforgeeks.org/reverse-a-stack-using-recursion/

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
        
def isEmpty(stack):
        return len(stack) == 0

def push(stack, item):
        stack.append(item)
        
def pop(stack):
        if (isEmpty(stack)):
                print "Stack Overflow"
                exit(1)
        return stack.pop()
        
def printStack(stack):
        for i in stack:
                print i        

def reverse(stack,k):
        if isEmpty(stack) == False:
                temp = pop(stack)
                push(k, temp)
                reverse(stack, k)
                
def main():

       s = createStack()
       k = createStack()
       
       push(s, 10)
       push(s, 2348023)
       push(s, 120)       
       push(s, 341234)
       print " Original"
       printStack(s)
       reverse(s,k)
       print "reversed"
       printStack(k)
       
main()
