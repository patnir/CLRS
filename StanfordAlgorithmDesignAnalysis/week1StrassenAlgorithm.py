# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:42:14 2016

@author: Rahul Patni
"""

import numpy as np

def PrintArray(array):
    for i in array:
        print i

def MakeSqureMatrix(dim):
    mat = []
    [mat.append([None] * dim) for num in range(dim)]
    return mat

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
    dim = len(X)
    if dim == 2:
        return Mul22(X, Y)
    halfDim = int(dim * 0.5)
    A = MakeSqureMatrix(halfDim)
    B = MakeSqureMatrix(halfDim)
    C = MakeSqureMatrix(halfDim)
    D = MakeSqureMatrix(halfDim)
    E = MakeSqureMatrix(halfDim)
    F = MakeSqureMatrix(halfDim)
    G = MakeSqureMatrix(halfDim)
    H = MakeSqureMatrix(halfDim)
    for i in range(halfDim):
        for j in range(halfDim):
            A[i][j] = X[i][j]           
            B[i][j] = X[i + halfDim][j]
            C[i][j] = X[i][j + halfDim]
            D[i][j] = X[i + halfDim][j + halfDim]
            E[i][j] = Y[i][j]           
            F[i][j] = Y[i + halfDim][j]
            G[i][j] = Y[i][j + halfDim]
            H[i][j] = Y[i + halfDim][j + halfDim]
    print MulMat(A, E)
    print MulMat(B, G)
    part1 = np.add(MulMat(A, E), MulMat(B, G))
    part2 = np.add(MulMat(A, F), MulMat(B, H))
    part3 = np.add(MulMat(C, E), MulMat(D, G))
    part4 = np.add(MulMat(C, F), MulMat(D, H))
    product = MakeSqureMatrix(dim)
    for i in range(dim):
        for j in range(dim):
            if i < halfDim and j < halfDim:
                product[i][j] = part1[i][j]
            elif i >= halfDim and j >= halfDim:
                product[i][j] = part4[i - halfDim][j - halfDim]
            elif i >= halfDim and j < halfDim:
                product[i][j] = part2[i - halfDim][j]
            else:
                product[i][j] = part3[i][j - halfDim]
    return product
    

#X = [[1, 2],[3, 4]]
#Y = [[5, 6],[7, 8]]

PrintArray(MulMat(np.ones([4, 4]), np.ones([4, 4])))