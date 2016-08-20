# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:23:21 2016

@author: Rahul Patni
"""

# Print elements of linked list and forward and reverse direction

import random

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        
    def printReverse(self):
        if self.next == None:
            print self.value, 
            return
        self.next.printReverse()
        print self.value, 
        
    def printForward(self):
        if self.next == None:
            print self.value, 
            return
        print self.value, 
        self.next.printForward()

class LinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
            
    def push(self, val):
        node = Node(val)
        self.size += 1
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head = node
    
    def pop(self):
        toReturn = None
        if self.head == None:
            return toReturn
        toReturn = self.head
        self.head= self.head.next
        toReturn.next = None
        self.size -= 1
        return toReturn
        
    def printReverse(self):
        if self.head == None:
            return
        self.head.printReverse()
        return
        
    def printForward(self):
        if self.head == None:
            return
        self.head.printForward()
        return

def main():
    l = LinkedList()
    for i in range(5):
        val = random.randint(10, 50)
        print val
        l.push(val)
    l.printForward()
    return
    
    
main()