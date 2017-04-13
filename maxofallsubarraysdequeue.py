''' Maximum of all sub-arrays of size k
http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
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


# A Dequeue (Double ended queue) based method for printing maixmum element of
# all subarrays of size k

def printKMax(k, arr,*args):
        # Create a Double Ended Queue, Qi that will store indexes of array elements
        # The queue will store indexes of useful elements in every window and it will
        # maintain decreasing order of values from front to rear in Qi, i.e., 
        # arr[Qi.front[]] to arr[Qi.rear()] are sorted in decreasing order        

        Q = collections.deque()
        # Process first k elements of array
        for i in xrange(k):
                # For every element the prev smaller elements are useless
                d = False
                if Q:
                        d = False
                 else:
                        d = True
                        
                while (d and arr[i] >= arr[Q[-1]]):
                        Q.pop()
                # add new element to rear
                Q.append(i)

        # Process rest of the elements
        for i in xrange(3,n):
                # The element at front of the queue is the largest element of 
                # previous window
                print arr[Q[0]] 
                
                # Remove the elements whic are ot of this window
                d = False
                if Q:
                        d = False
                 else:
                        d = True
                        
                while (d and arr[i] >= arr[Q[-1]]):
                        Q.pop()
                # add new element to rear
                Q.append(i)
        print arr[Q[0]]
                
def main():

        arr = {3561,12,1,56,8,98,212,79}
        k = 3
        printKMax(k,arr)
main()
