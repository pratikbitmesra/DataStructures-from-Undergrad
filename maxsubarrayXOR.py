# http://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/
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
class TrieNode:
        def __init__(self, value):
                self.value = value
                self.left = None # 0
                self.right = None    # 1
                
def find_current_bit(pre_xor):
        binary_pre_xor = bin(pre_xor)
        digits_in_binary = binary_pre_xor[2:]     # strip 0b from 0b0101010101111
        number_of_bits = len(digits_in_binary)
        while number_of_bits < INT_SIZE: 
                digits_in_binary = '0' + digits_in_binary
                number_of_bits = number_of_bits + 1

        return digits_in_binary        

          
def  insert(root, pre_xor):
        tmp = TrieNode(None)
        tmp = root  
        # From MSb to LSB
        # Finding current bit in prefix  
        digits_in_binary = find_current_bit(pre_xor)      

       
        for i in digits_in_binary:
                if i=='0' and tmp.left is not None:
                        tmp.left = TrieNode(None)
                elif i == '1' and tmp.right is not None:
                        tmp.right = TrieNode(None) 
        tmp.value = pre_xor
               
# Finds the maximum XOR ending with last number in
# prefix XOR 'pre_xor' and returns the XOR of this maximum
# with pre_xor which is maximum XOR ending with last element
# of pre_xor.                

def query(root, pre_xor):
        tmp = TrieNode(None)
        tmp = root
        digits_in_binary = find_current_bit(pre_xor)
        for i in digits_of_binary:
                #Traverse Trie, first look for a
                #prefix that has opposite bit
                # if there is no prefix with opposite bit, then look for same bit
                if (i == '0'):
                        if (tmp.right is not None):
                                tmp = tmp.right
                        elif (tmp.left is not None):
                                tmp = tmp.left
                                
                elif (i == '1'):
                        if (tmp.left is not None):
                                tmp = tmp.left
                        elif (tmp.right is not None):
                                tmp = tmp.right 
        
        return pre_xor^(tmp.value)
                
                
                                    
             
                                
                          
def maxsubarrayXOR(mylist=[], *args):
        
        root = TrieNode(None)
        insert(root,0)
        result = -sys.maxint - 1 # Get Minimum
        pre_xor = 0
        for i in arr:
                pre_xor = pre_xor^i
                insert(pre_xor,i)
                result = max(result, query(root, pre_xor))
        return result

def main():
        global arr
        arr  = [8, 1, 2, 12]
        n = len(arr)
        print "Maximum subarray XOR:%s" %(maxsubarrayXOR(arr,n))
main()
