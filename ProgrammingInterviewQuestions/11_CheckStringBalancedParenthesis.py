# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:56:31 2016

@author: Rahul Patni
"""

# checking is string has balanced parenthesis

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None        
        
    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.size == 1:
            self.head = new_node
            return
        temp = self.head
        new_node.next = temp
        self.head = new_node
        return
        
    def printStack(self):
        if self.size == 0:
            return None
        temp = self.head
        while temp != None:
            print temp.value,
            temp = temp.next
        return
        
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1

        ret_node = self.head
        self.head = self.head.next
        ret_node.next = None
        return ret_node
        


def isBalanced(expression):
    array = list(expression)
    opening = ['{', '(', '[']
    closing = ['}', ')', ']']
    s = Stack()
    for i in array:
        if i in opening:
            s.push(i)
        elif i in closing:
            ret = s.pop()
            if ret == None or opening.index(ret.value) != closing.index(i):
                return False
    if s.size == 0:
        return True
    return False
    
def main():
    print isBalanced("[(])")
    return
    
main()