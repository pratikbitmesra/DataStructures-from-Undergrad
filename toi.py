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

def tower(n, source, destination, auxillary):
    if n == 0:
        return
    tower((n-1), source, destination, auxillary)
    print 'MOve the disks %s from %s to %s'%(n,source,destination)
    tower((n-1), auxillary, destination, source)
def main():
    tower(3, 'S', 'D', 'A')
main()
