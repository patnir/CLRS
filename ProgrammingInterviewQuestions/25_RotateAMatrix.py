# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 10:54:13 2016

@author: Rahul Patni
"""

# rotate a matrix


# Counter clockwise

import random

def rotate(A, i, j, currR, currC, currRot, NoR, NoC):
    oR = currR
    oC = currC
    nextR = currR
    nextC = currC
    moves = currRot
    while moves > 0:
        if nextR - i == 0 and nextC - j >= 1:
            nextC -= 1
        elif nextR - i + 1 == NoR and nextC + 1 - j < NoC:
            nextC += 1
        elif nextC - j == 0 and nextR - i >= i:
            nextR += 1
        elif nextC - j + 1 == NoC and nextR - i >= 1:
            nextR -= 1
        moves -= 1
        currR = nextR
        currC = nextC
    A[oR][oC], A[currR][currC] = A[currR][currC], A[oR][oC]
    return

def rotateMatrix(A, rotations):
    n = len(A)
    m = len(A[0])
    i = 0
    j = 0
    NoR = n
    NoC = m
    while NoR > 0 and NoC > 0:
        currRot = rotations % (NoR * NoC)
        for currR in range(i , i + NoR):
            for currC in range(j , j + NoC):
                if currR == i or currC == j:
                    rotate(A, i, j, currR, currC, currRot, NoR, NoC)             
        i += 1
        j += 1
        NoR -= 2
        NoC -= 2
        print
        printMat(A)
        
       
def printMat(A):
    for i in A:
        print i
    
    
def main():
    n = 4
    m = 5
    A = []
    A = ([[0] * m for i in range(n)])
    printMat(A)
    print
    for i in range(n):
        for j in range(m):
            A[i][j] = random.randint(10, 90)
    printMat(A)
    rotateMatrix(A, 7)
    print
    printMat(A)
            
            
main()