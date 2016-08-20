# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:10:30 2016

@author: Rahul Patni
"""

# Print 2 D array in spiral order


def printSpiral(A, length, breadth):
    currLength = length - 1
    currBreadth = breadth - 1
    row = 0
    col = 0
    offset = 0
    for i in range(length * breadth):
        track = i
        track -= offset
        if (track + 1) == 2 * (currLength + currBreadth):
            offset =  2 * (currLength + currBreadth)
            currLength -= 2
            currBreadth -= 2
            track = 0
        print A[row][col], 
        if currLength == 0 or track / currLength == 0:
            col += 1
        elif (track - currLength) / currBreadth == 0:
            row += 1
        elif (track - currLength - currBreadth) / currLength == 0:
            col -= 1
        elif (track - currLength * 2 - currBreadth) / currBreadth == 0:
            row -= 1
    return
    
def main():
    A = [[2,4,6,8, -2],[5,9,12,16, -4],[2,11,5,9, -6],[3,2,1,8, -8], [41, 42, 43, 44, 56]]
    for i in A:
        print i
    printSpiral(A, len(A[0]), len(A))
    return
    
main()