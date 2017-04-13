# http://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
# Sum of bit differences
# Given an integer array of n integers, find sum of bit differences in all pairs 
#that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y. 
#For example, bit difference for 2 and 7 is 2. Binary representation
# of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).
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

#Python treats everything as objects but we would assume int size
# 32 bits or 4 bytes
global INT_SIZE
INT_SIZE = 32


def find_current_bit(number,position):
        #position is from MSB
        binary_pre_xor = bin(number)
        digits_in_binary = binary_pre_xor[2:]     # strip 0b from 0b0101010101111
        number_of_bits = len(digits_in_binary)
        while number_of_bits < INT_SIZE: 
                digits_in_binary = '0' + digits_in_binary
                number_of_bits = number_of_bits + 1

        return digits_in_binary[position]

def sumBitDiff(myList=[],*args):
        number_of_elements = len(myList)
        ans = 0
        total = 0
        n = len(arr)
        
        for i in xrange(INT_SIZE):
                #count elements with ith bit set
                count = 0                
                for j in arr:
                        k = find_current_bit(j,i)                      
                        #print k
                        if k == '1':                                
                                count = count + 1
                #print ans
                ans = ans + (count*(n-count)*2)        

        return ans
        
def main():
        global arr
        arr = [1,3,5]
        print "Sum of Bit Differences:%s" %sumBitDiff(arr)
        
main()
