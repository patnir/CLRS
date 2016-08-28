# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:51:55 2016

@author: Rahul Patni
"""

# Check is binary tree is BST

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print self.value,
        if self.right != None:
            self.right.inorder()
        return
        
class Tree:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        prev = None
        curr = self.head
        while curr != None:
            prev = curr
            if new_node.value <= curr.value:
                curr = curr.left
            else:
                curr = curr.right
        if new_node.value <= prev.value:
            prev.left = new_node
        else:
            prev.right = new_node
        return
    
    def inOrder(self):
        if self.head == None:
            print "Empty"
            return 
        self.head.inorder()
        
def main():
    tree = Tree()
    for i in range(0, 10):
        value = random.randint(0, 100)
        print "inserting", value
        tree.insert(value)
    tree.inOrder()
    return
    
main()