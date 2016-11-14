# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 05:28:44 2016

@author: Rahul Patni
"""

# tree traversal iteration

class sNode():
    def __init__(self, val):
        self.info = val
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
    
    def push(self, val):
        if val == None:
            return 
        n = sNode(val)
        if self.head == None:
            self.head = n
            return
        n.next = self.head
        self.head = n
        
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def printStack(self):
        if self.isEmpty():
            print "empty"
            return
        curr = self.head
        while curr != None:
            print curr.info, "->",
        print 
        
    def pop(self):
        if self.isEmpty():
            print "canont remove"
            return
        curr = self.head
        self.head = self.head.next
        curr.next = None
        #print "node being removed", curr.info
        return curr

class Node():
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None

def recursionPreorder(node):
    if node == None:
        return
    print node.info
    recursionInorder(node.left)
    recursionInorder(node.right)
    
def iterationPreorder(node):
    if node == None:
        return 
    s = Stack()
    s.push(node)
    while s.isEmpty() == False:
        curr = s.pop()
        print curr.info.info
        s.push(curr.info.right)
        s.push(curr.info.left)
    return
    
    
def recursionInorder(node):
    if node == None:
        return
    recursionInorder(node.left)
    print node.info
    recursionInorder(node.right)

def iterationInorder(node):
    if node == None:
        return
    s = Stack()
    curr = sNode(node)
    while curr.info != None or s.isEmpty() == False:
        while curr.info != None:
            s.push(curr.info)
            curr.info = curr.info.left
        n = s.pop()
        print n.info.info
        curr.info = n.info.right
        
        
def  recursionPostorder(node):
    if node == None:
        return
    recursionPostorder(node.left)
    recursionPostorder(node.right)
    print node.info

def interationPostorder(node):
    if node == None:
        return
    s1 = Stack()
    s2 = Stack()
    curr = node
    s1.push(curr)
    while s1.isEmpty() == False:
        pop = s1.pop()
        s2.push(pop.info)

        s1.push(pop.info.left)

        s1.push(pop.info.right)
    curr = s2.pop()
    while curr != None:
        print curr.info.info
        curr = s2.pop()
    
    return

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    root.right.left = Node(8)
    print "recursion"
    recursionPreorder(root)
    print "iteration"
    iterationPreorder(root)
    print "inorder recursion"
    recursionInorder(root)
    print "inorder iteration"
    iterationInorder(root)
    print "postorder recursion"
    recursionPostorder(root)
    print "postorder iteration"
    interationPostorder(root)
    return
    
main()
        