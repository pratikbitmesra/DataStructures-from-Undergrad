# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 12:03:14 2017
http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
@author: Pratik Mishra
"""

import os
import sys

class HashTable:
    
    def __int__(self,size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self,slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    
    def get(self,key):                         
        startslot = self.hashfunction(key,len(self.slots))
        
        data = None
        stop = False
        found = False
        position = startslot
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self, key)
    
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

if __name__ == "__main__":
    H = HashTable(51)
    