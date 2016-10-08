# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 16:56:30 2016

@author: Rahul Patni
"""

# tree traversal stack inorder

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (thevalue of the node)
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.n = None

class Stack():
    def __init__(self):
        self.head = None
    
    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            return 
        node.n = self.head
        self.head = node
        return
    
    def pop(self):
        if self.head == None:
            return Node
        toRet = self.head
        self.head = self.head.n
        toRet.n = None
        return toRet
    
    def stackTop(self):
        if self.head == None:
            return None
        node = Node(self.head.val)
        return node
        
            

def inOrder(root):
    #Write your code here
    curr = Node(root, root.data)
     
    stack = Stack()
    
    print stack.stackTop()
    
    stack.push(curr)
    while stack.stackTop() == None:
        return
        
    
