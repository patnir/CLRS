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
        self.parent = None
        
    def insert(self, val):
        if val <= self.value:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
            self.left.parent = self
        else:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)
            self.right.parent = self
        
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

           
    def pred(self, val):
        return
    
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
            return
        curr = self.root
        while curr != None:
            if val == curr.value:
                break
            if val > curr.value:
                curr = curr.right
            else:
                curr = curr.left
        if curr == None:
            return None
        if curr.left != None:
            curr = curr.left
            print "has a left branc"
            while curr.right != None:            
                curr = curr.right
            return curr.value
        else:
            print "does not have a left branch"
            curr = curr.parent
            while curr != None and curr.value > val:
                curr = curr.parent
            if curr == None:
                print "not found"
                return None
            return curr.value
        return "oops"
            
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
            print "not found"
            return False
        if curr.left == None and curr.right == None:
            print "both are none"
            if prev.right != None and prev.right.value == val:
                prev.right = None
            else:
                prev.left = None
            curr = None
        elif curr.left == None:
            print "left is none"
            if curr.value < prev.value:
                prev.left = curr.right
            else:
                prev.right = curr.right
        elif curr.right == None:
            print "right is none"
            if curr.value < prev.value:
                prev.left = curr.left
            else:
                prev.right = curr.left
        else:
            print "both are present"
            follow = curr
            pred = follow.left
            while pred.right != None:
                follow = pred
                pred = follow.right
            print pred.right, follow.right.value
            print pred.left
            curr.value = pred.value
            if follow.right.value != pred.value:
                print "not equal"
                curr.left = curr.left.left
            elif pred.left != None:
                print "left is none"
                follow.right = follow.right.left
            else:
                print "equal"
                follow.right = None
                pred = None
        return True
        
def main():
    array = []
    for i in range(0, 10):
        number = random.randint(0, 100)
        array.append(number)
        if i == 3:
            key = number
    print array
    tree = BST()
    for i in array:
        tree.insert(i)
    tree.preOrder()
    tree.inOrder()
    #key = tree.maxElement()
    key = tree.root.value
    print key
    print tree.pred(key)
    tree.inOrder()

if __name__ == "__main__":
    main()