'''
LinkedList Implementation of Queues
http://quiz.geeksforgeeks.org/queue-set-2-linked-list-implementation/
http://www.studytonight.com/data-structures/queue-data-structure
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

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class QueueLL:
    def __init__(self):
        self.front = None #head
        self.rear = None  #tail

    
    def enQueue(self, new_data):
        new_node = Node(data)
        if (self.rear == None):
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def deQueue(self):
        if self.front is None:
            return None
        tmp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None
            return tmp


def main():

    queue1 = QueueLL()
    queue1.enQueue(10)
    queue1.enQueue(42)
    queue1.enQueue(313)
    queue1.deQueue()
    queue1.deQueue()
    queue1.enQueue(4312)
    queue1.enQueue(131342)
    
main()
        
