# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 19:41:47 2016

@author: Rahul Patni
"""

# Stack and Tree

import random

class StackNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack():
    def __init__(self):
        self.head = None
        
    def push(self, val):
        node = StackNode(val)
        
        if self.head == None:
            self.head = node
            return
            
        node.next = self.head
        self.head = node
        return
        
    def pop(self):
        if self.head == None:
            return None
        toRet = self.head
        self.head = self.head.next
        toRet.next = None
        
        return toRet
        
    def printStack(self):
        if self.head == None:
            return
        curr = self.head
        while curr != None:
            print str(curr.val) + "->",
            curr = curr.next
            
        print
        
        return
        
    def isEmpty(self):
        if self.head == None:
            return True
        return False
        
def main():
    stack = Stack()
    for i in range(20):
        val = random.randint(-200, 200)
        print val
        stack.push(val)
        
    stack.printStack()
    
    while stack.isEmpty() == False:
        ret = stack.pop()
        print ret.val
        stack.printStack()
    stack.printStack()
    

main()
        