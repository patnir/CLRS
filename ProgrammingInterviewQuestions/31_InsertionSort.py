# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 15:43:56 2016

@author: Rahul Patni
"""

# Insertion

import random

def insertionSort(A):
    for j in range(1, len(A)):
        i = j
        temp = A[i]
        while i > 0 and A[i - 1] > temp:
            A[i] = A[i - 1]   
            i -= 1
        A[i] = temp
        
    print A
    
    checkIncreasing(A)
    return




def checkIncreasing(A):
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            print "not increasing"
            return
    print "increasing"
    return     
    
def main():
    A = []    
    for i in range(101):
        A.append(random.randint(10, 90))
    print A
    insertionSort(A)
    
    
main()