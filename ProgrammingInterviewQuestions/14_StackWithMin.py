# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 02:08:26 2016

@author: Rahul Patni
"""

# stack with min

import random

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        return
        
    def push(self, val):
        nNode = Node(val)
        if self.head == None:
            self.head = nNode
            return
        nNode.next = self.head
        self.head = nNode
        return
    
    def pop(self):
        if self.head == None:
            return
        nNode = self.head
        self.head = nNode.next
        nNode.next = None
        return nNode

    def printStack(self):
        curr = self.head
        while curr != None:
            print curr.value,
            curr = curr.next
        print "empty"
        return

    def sMin():
        return
        

def main():
    s = Stack()
    for i in range(10):    
        a = random.randint(10, 100)
        s.push(a)
        s.printStack()
        
    for i in range(20):
        v = s.pop()
        if v != None:
            print v.value
        s.printStack()
    
    
main()