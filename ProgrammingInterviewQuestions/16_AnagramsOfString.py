# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 10:32:23 2016

@author: Rahul Patni
"""

# anagrams of a string

import numpy

def comp(word):
    s = list(word)
    uniqueS = []
    for i in s:
        if i not in uniqueS:
            uniqueS.append(i)
    occ = numpy.zeros(len(uniqueS), int)
    for i in s:
        occ[uniqueS.index(i)] += 1
    return occ, uniqueS

def checkAnagram(T, occ, uniq):
    for i in T:
        if i not in uniq:
            return False
        if occ[uniq.index(i)] == 0:
            return False
        occ[uniq.index(i)] -= 1
    s = sum(occ)
    if s != 0: 
        return False
    return True
        
    
def main():
    word = "asdfa"
    a , b = comp(word)
    print checkAnagram("aasdf", a, b)
    
    
main()