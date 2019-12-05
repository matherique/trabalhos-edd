#!/usr/bin/env python3
class Node:
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value
        self.ifLeftChild = False
        self.black = False

class RBD:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, key, value):
        node = Node(key, value)

        if self.root == None:
            self.root = node
            self.root.black = True
            self.size += 1
            return 

        add(root, node)

    def add(self, parent, newNode):
        if parent.key == newNode.key:
            if parent.right == None:
                parent.right = newNode
                newNode.parent = parent
                newNodee.ifLeftChild = False

                return

            return add(parent.right, newNode)

        if parent.left == None:
            parent.left = newNode
            newNode.parent = parent
            newNodee.ifLeftChild = True 
            return

        checkColor(newNode)    
        return add(parent.left, newNode)

    def checkColor(self, node):
        if node == self.root:
            return

        if not node.black and not node.parent.black:
            correct(node)
            
        checkColor(node.parent)

    def corrent(self, node):
        if node.parent.isLeftChild:
            if node.parent.parent.right == None or node.parent.parent.right.black:
                return rotation(node)
            
            if node.parent.parent.right != None:
                node.parent.parent.right.black = True

            node.parent.parent.black = False
            node.parent.black = True

            return

        if node.parent.parent.left == None or node.parent.parent.left.black:
            return rotation(node)
            
        if node.parent.parent.left != None:
            node.parent.parent.left.black = True

        node.parent.parent.black = False
        node.parent.black = True

        return

    
    def rotation(self, node):
        if node.isLeftChild:
            if node.parent.isLeftChild:
                rightRotation(node.parent.parent)
                node.black = False
                node.parent.black = True

                if node.parent.right != None:
                    node.parent.right.black = False

                return 
            rightLeftRotation(node.parent.parent)
            node.black = True
            node.right.black = False
            node.left.black = False

            return 


        if not node.parent.isLeftChild:
            leftRotation(node.parent.parent)
            node.black = False
            node.parent.black = True

            if node.parent.right != None:
                node.parent.right.black = False

            return 
        leftRightRotation(node.parent.parent)

        node.black = True
        node.right.black = False
        node.left.black = False

        return 


    def leftRotation(self, node):
        temp = node.right
        node.right = temp.left
        
        if node.right != None:
            node.right.parent = node
            node.right.isLeftChild = False

        if node.parent == None:
            self.root = temp
            temp.parent = None
        else:
            temp.parent = node.parent
            if node.isLeftChild:
                temp.isLeftChild = True
                temp.parent.left = temp
            else:
                temp.isLeftChild = False 
                temp.parent.right = temp 


        temp.left = node
        node.isLeftChild = True
        node.parent = temp


if __name__ == '__main__':
    print("ola mundo")
