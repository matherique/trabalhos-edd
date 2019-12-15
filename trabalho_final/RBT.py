#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

    def __str__(self):
        return f"{self.value}"

    

class Tree:
    
    def __init__(self):
        self.root = None
        self.space = 0

    def add(self, value):
        # tree is empty
        if self.root == None:
            self.root = Node(value)
            return 
        
        if value > self.root.value:
            self.root.right = Node(value)
            return 
        self.root.left = Node(value)

    def __str__(self):
        

if __name__ == '__main__':
    t = Tree()
    t.add(10)
    t.add(12)
    t.add(5)
    print(f"{t}")
