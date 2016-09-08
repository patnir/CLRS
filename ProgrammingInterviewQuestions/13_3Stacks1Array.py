# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 23:26:07 2016

@author: Rahul Patni
"""

import random

import array

class ThreeStack():
    def __init__(self):
        self.data = array.array('i', range(12))
        self.size = 12
        self.length = (self.size - 6) / 3
        for i in range(6, self.size):
            self.data[i] = -1
        self.data[0] = (self.size - 6) / 3 + 6 - self.length
        self.data[1] = self.data[0]
        self.data[2] = (self.size - 6) * 2 / 3 + 6 - self.length
        self.data[3] = self.data[2]
        self.data[4] = self.size - self.length
        self.data[5] = self.data[4]
        
    def printStack(self):
        for i in range(self.size):
            print self.data[i],
        print
        return

    def insert(self, value, stack):
        if stack > 3 or stack < 1:
            print "error"
            return
        length = (self.size - 6) / 3
        head = stack * 2 - 2
        tail = head + 1
        if self.data[head] - self.data[tail] < length:
            self.data[self.data[head]] = value
            self.data[head] += 1
        else:
            print "overload"
                

def main():
    s = ThreeStack()
    s.printStack()
    for i in range(20):
        print
        a = random.randint(0, 20)
        print a, 
        stack = random.randint(1, 3)
        print stack
        s.insert(a, stack)
        s.printStack()
    
    
main()