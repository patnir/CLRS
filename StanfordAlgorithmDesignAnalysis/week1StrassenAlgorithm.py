# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:42:14 2016

@author: Rahul Patni
"""

# Strassen's algorithm to multiply two NxN matrices
def Mul22(X, Y):
    a = X[0][0]
    b = X[0][1]
    c = X[1][0]
    d = X[1][1]
    e = Y[0][0]
    f = Y[0][1]
    g = Y[1][0]
    h = Y[1][1]
    p1 = a * (f - h)
    p2 = h * (a + b)
    p3 = e * (c + d)
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)
    return [[p5 + p4 - p2 + p6, p1 + p2], [p3 + p4, p1 + p5 - p3 - p7]]

def MulMat(X, Y):
    if len(X) == 2:
        return Mul22(X, Y)
    return
    

X = [[1, 2],[3, 4]]
Y = [[5, 6],[7, 8]]

print MulMat(X, Y)