# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:02:09 2016

@author: Rahul Patni
"""

# traversing through map 

def expandMatrix(A):
    l = len(A) + 2
    b = len(A[0]) + 2
    new_mat = []
    [new_mat.append(b * [0]) for x in range(l)]
    for i in range(l):
        for j in range(b):
            if i == 0 or i == l - 1 or j == 0 or j == b - 1:
                new_mat[i][j] = -1
            else:
                new_mat[i][j] = A[i - 1][j - 1]
                
    return new_mat
    
def printMat(A):
    for i in A:
        print i
    
def main():
    A = [[1, 2, 3, 14], [4, 5, 6, 11], [7, 8, 9, 10]]    
    
    N = expandMatrix(A)
    printMat(N)
    print 
    
main()