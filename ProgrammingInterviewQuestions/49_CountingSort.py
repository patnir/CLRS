# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:10:31 2016

@author: Rahul Patni
"""

# COUNTING SORT

import random

def main():
    size = 10
    A = [0] * 10
    for i in range(0, size):
        A[i] = random.randint(11, 20)
    print A    
    largest = max(A)
    smallest = min(A)
    buff = smallest
    for i in range(len(A)):
        A[i] -= buff
    print A
    print largest
    B = [0] * (largest - smallest + 1)
    for i in A:
        B[i] += 1
    print "stage 1"
    print B
    
    print "stage2"
    for i in range(1, len(B)):
        B[i] += B[i - 1]
        
    print B
    
    C = list(A)
    
    for i in range(len(A) - 1, -1, -1):
        C[B[A[i]] - 1] = A[i]
        B[A[i]] = B[A[i]] - 1
    for i in range(0, len(C)):
        C[i] += buff
    print C
    
main()




