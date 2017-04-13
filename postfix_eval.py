# Postfix Exp evaluation
# Python program to evaluate value of a postfix expression
# http://quiz.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
# Infix expression:The expression of the form a op b. When an operator is in-between every pair of operands.
# Postfix expression:The expression of the form a b op. When an operator is followed for every pair of operands.
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
from sys import maxsize

class Evaluate:
            def __init__(self, capacity):
                        self.top = -1
                        self.capacity = capacity
                        self.array = []
            # check if the stack is empty
            def isEmpty(self):
                return True if self.top == -1 else False
             
            # Return the value of the top of the stack
            def peek(self):
                return self.array[-1]
             
            # Pop the element from the stack
            def pop(self):
                if not self.isEmpty():
                    self.top -= 1
                    return self.array.pop()
                else:
                    return "$"
             
            # Push the element to the stack
            def push(self, op):
                self.top += 1
                self.array.append(op) 
         
         
            # The main function that converts given infix expression
            # to postfix expression
            def evaluatePostfix(self, exp):
                 
                # Iterate over the expression for conversion
                for i in exp:
                     
                    # If the scanned character is an operand
                    # (number here) push it to the stack
                    if i.isdigit():
                        self.push(i)
         
                    # If the scanned character is an operator,
                    # pop two elements from stack and apply it.
                    else:
                        val1 = self.pop()
                        val2 = self.pop()
                        self.push(str(eval(val2 + i + val1)))
         
                return int(self.pop())
                                         

def main():
        exp = "231*+9-"
        obj = Evaluate(len(exp))
        print "Value of %s is %d" %(exp, obj.evaluatePostfix(exp))
main()
