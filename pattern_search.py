# Searching Patterns in a given string
# python pattern_search.py abbabcahidhiedhpiahdhclksdlaabbab abbab
# Pattern found at position:0
# Pattern found at position:28
# Worst Case O(n^2)


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


def pattern_detector(inp_str, search_str):

        len_inp = len(inp_str)
        len_search = len(search_str)
        
        for x in xrange(len_inp-len_search+1):
                
                for y in xrange(len_search):
                        if inp_str[x+y] != search_str[y]:                                
                                break
                if y == len_search -1:
                        print "Pattern found at position (from 0 to endOfString) :%s" %x  
                                 
        

def main():
        inp_str = sys.argv[1]
        search_str = sys.argv[2]  
        pattern_detector(inp_str, search_str)      
main()
