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
        
    def preorder(self):
        print self.value,
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
        return        
        
    def inOrderBST(self, array):     
        if self.left != None:
            self.left.inOrderBST(array)
        array.append(self.value)
        if self.right != None:
            self.right.inOrderBST(array)
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
        
    def preOrder(self):
        if self.head == None:
            print "Empty"
            return 
        self.head.preorder()
        
    def checkBST(self):
        if self.head == None:
            return True
        A = []
        self.head.inOrderBST(A)
        return A 
        
def delete(tree, val):
    if tree.head == None:
        print "empty"
        return False
    curr = tree.head
    prev = None
    while curr != None and curr.value != val:
        prev = curr
        if curr.value > val:
            curr = curr.left
        else:
            curr = curr.right 
    if curr == None:
        print "not found"
        return False
    print "found"
    if curr.left == None and curr.right == None:
        print "both none"
        if prev == None:
            tree.head = None
        elif curr.value < prev.value:
            prev.left = None
        else:
            prev.right = None
    elif curr.left != None and curr.right == None:            
        print "right is none"
        if prev == None:
            tree.head = curr.left
        elif curr.value < prev.value:
            prev.left = curr.left
        else:
            prev.right = curr.left
    elif curr.right != None and curr.left == None:
        print "left is none"
        if prev == None:
            tree.head = curr.right
        elif curr.value < prev.value:
            prev.left = curr.right
        else:
            prev.right = curr.right
    else:
        print "both are present"
        toRepPrev = None
        toRep = curr.left
        while toRep.right != None:
            toRepPrev = toRep
            toRep = toRep.right
        if toRepPrev != None:
            toRepPrev.right = toRep.left
        else:
            curr.left = toRep.left
        toRep.left = curr.left
        toRep.right = curr.right
        curr.left = None
        curr.right = None
        if prev != None:
            if curr.value < prev.value:
                prev.left = toRep
            else:
                prev.right = toRep
        else:
            tree.head = toRep
    return True

def main():
    tree = Tree()
    val = 0
    for i in range(0, 14):
        value = random.randint(20, 99)
        print "inserting", value
        if i == 7:
            val = value
        tree.insert(value)
    tree.inOrder()
    print "finding", val
    print delete(tree, val)
    tree.inOrder()
    print
    tree.preOrder()
    return
    
main()