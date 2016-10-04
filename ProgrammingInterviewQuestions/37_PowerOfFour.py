# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 22:58:56 2016

@author: Rahul Patni
"""

# bit manipulation power of 4

def powerOfFour(number):
    if number == None:
        return False
    i = 1
    while i < number:
        i = i << 2
    if i == number:
        return True
    return False
        
    
def main():
    print powerOfFour(64)
    return
    
main()