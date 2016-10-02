# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 12:57:22 2016

@author: Rahul Patni
"""

# recursion print

def Seq(n):
    assert(n > 0)
    if n == 1:
        return "1 "
    if n == 2:
        return "1 2 1 "
    s1 = Seq(n - 1)
    s2 = Seq(n - 2)
    
    return s1 + s2 + str(n) + " " + s2 + s1
    
    
def main():
    n = 3
    print Seq(n)
    
    
main()