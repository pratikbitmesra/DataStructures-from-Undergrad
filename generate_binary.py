'''
Generate binary numbers from 1 to n
http://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/
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


def generateBinary(n):
        q = []
        q.append("1")
        
        while (n):
                s1 = q[0]
                del q[0]
                print s1
                s2 = s1
                s1 = s1 + "0"
                q.append(s1)
                s2 = s2 +"1"
                q.append(s2)
                n -= 1
def main():
        n = 10
        generateBinary(n)
        return 0
main()
