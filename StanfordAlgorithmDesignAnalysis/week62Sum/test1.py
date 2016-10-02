# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 09:15:33 2016

@author: Rahul Patni
"""

# test

    if len(num) == 1:
        return num[0]
    num.sort()
    cost = []
    cost.append(num[0] + num[1])
    total = long(num[0] + num [1])
    prev = 0
    for i in range(2, len(num)):
        if i < len(num) - 1 and cost[prev] > num[i + 1]:
            cost.append(num[i + 1] + num[i])
            total += long(num[i + 1] + num[i])
            
        else:
            cost.append(cost[prev] + num[i])
            total += long(cost[prev] + num[i])
        prev += 1
    return total