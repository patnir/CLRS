# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:20:39 2016

@author: Rahul Patni
"""

# 21 Permutations of a string [AGAIN]

def swap(word, a, b):
    word[a], word[b] = word[b], word[a]

def permutations(word, s, e):
    if e - s == 1:
        print "".join(word)
        swap(word, s, e)
        print "".join(word)
        swap(word, s, e)
        return
    for i in range(s, e + 1):
        #permutations(word, i, e)
        swap(word, s, i)
        permutations(word, s + 1, e)
        swap(word, s, i)
        
    return
    
def main():
    word = "dog"
    word = list(word)
    print word
    permutations(word, 0, len(word) - 1)
    
main()