# Substract two numbers represented as LinkedList
#http://www.geeksforgeeks.org/subtract-two-numbers-represented-as-linked-lists/
import os
import sys
import re
import operator
import csv
import itertools
import math
import collections
import fileinput
import bisect

from itertools import groupby
from sys import argv
from operator import itemgetter, attrgetter, methodcaller
from operator import add

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
