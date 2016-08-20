# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:42:03 2016

@author: Rahul Patni
"""

# How many times is a curcular sorted array sorted?

def rotations(A):
    start = 0
    end = len(A) - 1
    front = A[start]
    if front <= A[end]:
        return start
    while start <= end:
        med = ((start + end) / 2)
        if A[med - 1] > A[med]:
            return med
        if A[med] >= front:
            start = med + 1
        else:
            end = med - 1

def main():
    A = [11, 12, 1, 2, 3, 4]
    print rotations(A), "rotations"
    return

main()