''' Given an array, print the Next Greater Element (NGE) for every element. 
The Next greater Element for an element x is the first greater element on 
the right side of x in array. Elements for which no greater element exist, 
consider next greater element as -1.

Examples:
a) For any array, rightmost element always has next greater element as -1.
b) For an array which is sorted in decreasing order, all elements have next greater element as -1.
c) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.
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

def push(stack,x):
        stack.append(x)
        
def pop(stack):
        if isEmpty(stack):
                print "Stack Underflow"
        else:
                return stack.pop()
                
def printNGE(arr):
        s = createStack()
        element = 0
        next = 0
        push(s, arr[0])
        
        for i in range(1,len(arr), 1):
                next = arr[i]
                if isEmpty(s) == False:
                        element = pop(s)
                        while element < next:
                                print element + "NGE" + next
                                if isEmpty(s) == True:
                                        break
                                element = pop(s)
                                
                        if element > next:
                                push(s, element)

                push(s, next)
                
        while isEmpty(s) == False:
                element = pop(s)
                next = -1
                print element +"NGE"+next                                
                
                
                

def main():
        arr = [11, 13, 21, 3]
        printNGE(arr)
main()
