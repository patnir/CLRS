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
            self.data[i] = 0
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

    def push(self, value, stack):
        if stack > 3 or stack < 1:
            print "error"
            return
        head = stack * 2 - 2
        tail = head + 1
        if self.data[head] - self.data[tail] >= self.length:
            nSize = (self.size - 6) * 3 + 6
            nLength = self.length * 3
            nArray = array.array('i', range(nSize))
            for i in range(nSize):
                nArray[i] = 0
            for i in range(3):
                nArray[i * 2 + 1] = ((self.data[i * 2 + 1] - 6) / self.length) * nLength + (self.data[i * 2 + 1]) % self.length + 6
                nArray[i * 2] = nArray[i * 2 + 1] + self.data[i * 2] - self.data[i * 2 + 1]
            for i in range(6, self.size):
                check = ((i  - 6) / self.length) * nLength + (i - 6) % self.length + 6
                nArray[check] = self.data[i]
            self.data = nArray
            self.size = nSize
            self.length = nLength
        self.data[self.data[head]] = value
        self.data[head] += 1
        
    def pop(self, stack):
        head = stack * 2 - 2
        tail = head + 1
        if self.data[head] == self.data[tail]:
            print "stack is empty"
            return None
        ret = self.data[self.data[head] - 1]
        self.data[self.data[head] - 1] = 0
        self.data[head] -= 1
        return ret

def main():
    s = ThreeStack()
    s.printStack()
    for i in range(5):
        print
        a = random.randint(10, 100)
        print a, 
        stack = random.randint(1, 3)
        print stack
        s.push(a, stack)
    print "popping"
    for i in range(10):
        s.printStack()
        a= random.randint(1, 3)
        print a
        print s.pop(a)
    
main()