# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 19:50:34 2016

@author: Rahul Patni
"""

# nuts and bolts

import random

def createArrays(size):
    A = [0] * size
    B = [0] * size
    for i in range(size):
        val = random.randint(10, 30)
        A[i] = val
        B[i] = val
    return A, B
    
def shuffleArray(A, size):
    for i in range(size / 2):
        place1 = random.randint(0, size - 1)
        place2 = random.randint(0, size - 1)
        A[place1], A[place2] = A[place2], A[place1]
    
def quickMatch(N, B):
    
    return    
    
def main():
    N, B = createArrays(10)
    print N
    print B
    print "after shuffle"
    shuffleArray(N, 10)
    shuffleArray(B, 10)
    print N
    print B
    return
    
    
main()