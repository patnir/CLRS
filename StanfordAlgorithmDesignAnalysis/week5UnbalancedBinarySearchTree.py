# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 06:04:03 2016

@author: Rahul Patni
"""
import random

# Unbalanced Binary Search Tree

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
    def insert(self, val):
        if val <= self.value:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        
    def search(self, val):
        if val == self.value:
            return True
        if val < self.value:
            if self.left == None:
                return False
            else:
                return self.left.search(val)
        else:
            if self.right == None:
                return False
            else:
                return self.right.search(val)
        return
        
    def postOrder(self):
        if self == None:
            return
        if self.left != None:
            self.left.postOrder()
        if self.right != None:
            self.right.postOrder()
        print self.value,
        return 
        
    def preOrder(self):
        if self == None:
            return
        print self.value,
        if self.left != None:
            self.left.preOrder()
        if self.right != None:
            self.right.preOrder()
        return
        
    def inOrder(self):
        if self == None:
            return
        if self.left != None:
            self.left.inOrder()
        print self.value, 
        if self.right != None:        
            self.right.inOrder()
        return
        
    def goLeft(self):
        if self.left == None:
            return self.value
        else:
            return self.left.goLeft()
            
    def goRight(self):
        if self.right == None:
            return self.value
        else:
            return self.right.goRight()

           
    def pred(self, key, val):
        return key
    
    def succ(self):
        return

class BST():
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root != None:
            self.root.insert(val)
            return
        else:
            self.root = Node(val)
        return
        
    def search(self, val):
        if self.root == None:
            return False
        return self.root.search(val)
        
    def postOrder(self):
        if self.root == None:
            return None
        else:
            self.root.postOrder()
            print "\n"
        return
        
    def preOrder(self):
        if self.root == None:
            return None
        else:
            self.root.preOrder()
            print "\n"
        return
        
    def inOrder(self):
        if self.root == None:
            return None
        else:
            self.root.inOrder()
            print "\n"
        return
    
    def minElement(self):
        if self.root == None:
            return None
        else:
            return self.root.goLeft()
            
    def maxElement(self):
        if self.root == None:
            return None
        else:
            return self.root.goRight()
            
    def pred(self, val):
        if self.root == None:
            return None
        return self.root.pred(None, val)
            
    def succ(self, val):
        if self.root == None:
            return None
        return self.root.succ(val)
        
    def delete(self, val):
        if self.root == None:
            return
        prev = None
        curr = self.root
        while curr != None:
            if val == curr.value:
                break
            prev = curr
            if val > curr.value:
                curr = curr.right
            else:
                curr = curr.left
        if curr == None:
            return False
        if curr.left == None and curr.right == None:
            prev = None
        elif curr.left == None:
            if curr.value < prev.value:
                prev.left = curr.right
            else:
                prev.right = curr.right
        elif curr.right == None:
            if curr.value < prev.value:
                prev.left = curr.left
            else:
                prev.right = curr.left
        else:
            pred = curr.left
            while pred.right != None:
                pred = pred.right
            pred.right = None
            curr.value = pred.value
        return True
        
def main():
    array = []
    for i in range(0, 2):
        number = random.randint(0, 100)
        array.append(number)
        if i == 9:
            key = number
    print array
    tree = BST()
    for i in array:
        tree.insert(i)
    tree.preOrder()
    tree.inOrder()
    #key = tree.maxElement()
    key = tree.minElement()
    print key
    print "key", tree.delete(key), key
    tree.inOrder()

if __name__ == "__main__":
    main()