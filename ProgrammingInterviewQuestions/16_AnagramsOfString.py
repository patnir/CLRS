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
      
def swap(n, start, end):
    temp = n[start]
    n[start] = n[end]
    n[end] = temp
    return       

def anagram(word, start, end):
    if end - start < 2:    
        print word
        swap(word, start, end)
        print word
        swap(word, start, end)
        return
    for i in range(start, end + 1):
        swap(word, start, i)
        anagram(word, start + 1, end)
        swap(word, start, i)
    return
    
    
def main():
    word = "dog"
    word = list(word)
    print word
    print "calling function"
    anagram(word, 0, len(word) - 1)
    
    
    
main()