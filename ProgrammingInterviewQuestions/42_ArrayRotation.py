# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:17:11 2016

@author: Rahul Patni
"""

def array_left_rotation(a, n, k):
    k = k  % n
    if k == 0:
        return a
    toMove = n - 1
    tempAdd = toMove - k
    temp = a[tempAdd]
    a[tempAdd] = a[toMove]
    toMove = tempAdd
    for i in range(n):
        tempAdd = toMove - k
        if tempAdd < 0:
            tempAdd = tempAdd + n
        temp, a[tempAdd] = a[tempAdd], temp
        toMove = tempAdd
    return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))