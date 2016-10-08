# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 16:35:42 2016

@author: Rahul Patni
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def printMat(n):
    for i in n:
        print i

def knappy(n, k, a):
    newA = []
    a.sort()
    for i in a:
        newA.append([i] * (k / i))
    A = []
    for i in newA:
        for j in i:
            A.append(j)
    #print len(A)
       
    mat = [[0] * (len(A) + 1) for i in range(len(A) + 1)]
    #printMat(mat)
    Max = -1 * sys.maxint
    for i in range(1, len(A) + 1):
        for j in range(1, 1 + len(A)):
            left = mat[i][j - 1]
            top = mat[i - 1][j]
            diag = mat[i - 1][j - 1]
            diag = diag + A[j - 1]
            if diag <= k:
                m = max(diag, left, top)
                mat[i][j] = m
                if m > Max:
                    Max = m
            else:
                currI = i
                currJ = j
                while diag > k and currI >= 0 and currJ >= 0:
                    diag = mat[currI - 1][currJ - 1] + A[j - 1]
                    currI -= 1
                    currJ -= 1
                mat[i][j] = diag   
                if diag > Max:
                    Max = diag

    #print 
    #printMat(mat)
    
    return Max

def readInputs():
    T = int(raw_input())
    for i in range(T):
        first = raw_input()
        first = first.rstrip()
        first = first.split(" ")
        n = int(first[0])
        k = int(first[1])
        #print n, k
        second = raw_input()
        second = second.rstrip()
        second = second.split(" ")
        a = []
        for i in second:
            a.append(int(i))
        #print a
        print knappy(n, k, a)
        #print recursive(n, k, a, 0, len(a) - 1)

def recursive(n, k, a, start, end):
    if start == end:
        return a[start]
    if end < start:
        return a[end]
    first = a[start] + recursive(n, k, a, start + 1, end)
    if first > k:
        first = first - a[start]
    second = recursive(n, k, a, start + 1, end - 1)
    third = recursive(n, k, a, start - 1, end - 1)
    
    return max(first, second, third)
    
        
def main():
    readInputs()
    
main()