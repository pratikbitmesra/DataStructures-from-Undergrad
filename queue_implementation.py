'''
Array Implementation of Queue
http://quiz.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/
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

class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity - 1
        self.array = [0]*capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        if isEmpty(self):
            return
        self.rear = (self.rear + 1)%(self.capacity)
        self.array[self.rear] = data
        self.size = self.size + 1
        print "%d Enqueued to Queue" %data

    def dequeue(self):
        if isEmpty(self):
            return (-sys.maxint - 1)
        data = self.array[self.front]
        self.front = (self.front + 1)%(self.capacity)
        self.size = self.size - 1
        return data

    def front(self):
        if isEmpty(self):
            return (-sys.maxint - 1)
        return self.array[self.front]

    def rear(self):
        if isEmpty(self):
            return (-sys.maxint - 1)
        return self.array[self.rear]

def main():
    queue1 = QueueArray(1000)
    queue1.enqueue(10)
    queue1.enqueue(3110)
    queue1.enqueue(3210)
    queue1.enqueue(210)
    queue1.enqueue(110)
    queue1.enqueue(810)
    queue1.enqueue(30)

    print "%s Dequeued from Queue" %queue1.dequeue()
    print "Front Item:%s" %queue1.front()
    print "Rear Item:%s"%queue1.rear()
main()
