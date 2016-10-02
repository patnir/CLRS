# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 19:05:44 2016

@author: Rahul Patni
"""

# largest continous subsequence

# -*- coding: utf-8 -*
"""
Created on Thu Sep 29 00:45:45 2016

@author: Rahul Patni
"""

# largest string subsequence

def printMatrix(S):
    for i in S:
        print i

def reconstructSolution(S, B):
    result = []
    row = 0
    col = 0
    printMatrix(S)
    while row < len(S) - 1:
        curr = S[row][col]
        n = S[row + 1][col]   
        if n != curr:
            result.append(B[row])
            col += 1
        row += 1
    return "".join(result)

def lss(a, b):
    A = list(a)
    B = list(b)
    S = []
    S = [[0] * (len(A) + 1) for i in range(len(B) + 1)]
    for i in range(len(B) - 1, -1, -1):
        for j in range(len(A) - 1, -1, -1):
            S[i][j] = min(S[i + 1][j], S[i][j + 1])
            if B[i] == A[j]:
                S[i][j] = 1 + S[i + 1][j + 1]
    printMatrix(S)
    #print reconstructSolution(S, B)
    return
    
    
    
def main():
    a = "aaccaaccaacc"
    b = "aabbaabbaaccaabbaa"
    print lss(a, b)
    return
    
    
main()