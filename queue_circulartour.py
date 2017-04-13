'''
http://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/
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

class PetrolPump:
        def __init__(self):
                self.petrol = None
                self.distance = None

class Queue:
        def __init__(self):
                self.array = []
                
        def push(self,pet, dist):
                new_node = PetrolPump()
                new_node.petrol = pet
                new_node.distance = dist
                self.array.append(new_node)
                #print len(self.array)
        
        # Function returns starting point if there is a solution else -1
        def printTour(self):
                length = len(self.array)
                start = 1
                end = 1
                current_petrol = self.array[start].petrol - self.array[start].distance
                
                while end != start or current_petrol < 0:
                        while current_petrol<0 and start !=end:
                                current_petrol -= self.array[start].petrol - self.array[start].distance
                                start = (start + 1)%length
                                if start == 0:
                                        return -1
                        current_petrol += self.array[end].petrol - self.array[end].distance
                        end = (end+1)%length
                return start
        

def main():
        arr = Queue()
        arr.push(6,4)
        arr.push(3,6)
        arr.push(7,3)
        
        start = arr.printTour()
        if start == -1:
                "no Solution" 
        else: 
                print 'Start:%s' % start

main()
