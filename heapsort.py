'''
Heap Sort
http://quiz.geeksforgeeks.org/heap-sort/
Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.
How to build the heap?
Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.
Lets understand with the help of an example:
Input data: 4, 10, 3, 5, 1
                 4(0)
		/   \
	     10(1)   3(2)
            /   \
	 5(3)    1(4)

The numbers in bracket represent the indices in the array 
representation of data.

Applying heapify procedure to index 1:
 		4(0)
		/   \
            10(1)    3(2)
           /   \
	5(3)    1(4)

Applying heapify procedure to index 0:
	        10(0)
		/  \
	     5(1)  3(2)
            /   \
         4(3)    1(4)
The heapify procedure calls itself recursively to build heap
 in top down manner.
C++JavaPython

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

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l< n and arr[i] < arr[l]:
        largest = l

    if r<n and arr[largest]<arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest]= arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build a Max Heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)


def main():
    arr = [12,14, 98, 181, 31, 48, 128]

    heapSort(arr)
    n = len(arr)
    print "Sorted Array:"
    for i in range(n):
        print "%d"%arr[i]
        
main()
