# -*- coding: utf-8 -*-

"""
Binary trees traversal
3 types: 
    Preorder:
        parent-left-right
    InOrder:
        Left-parent-right
    PostOrder:
        right-parent-left
"""
class BTNode:
    def __init__(self, value):
        self.left=None
        self.right=None
        self.val = value

class binaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self, value):
        self.root = value
    def getNodeValue(self):
        return self.root
    def insertRight(self, newNode):
        if not self.right:
            self.right = binaryTree( newNode)
        else:
            tree =

        
        
    
    
#    def inorderTraversal(self, root):
#        if root:
#            self.inorderTraversal(root.left)
            
            
if __name__ == '__main__':
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.right.left = BTNode(5)
    root.left.right = BTNode(6)
    print(root)
    




"""
Binary Search Tree
    Properties:
        -left subtree of a node contains only nodes with lesser keys than nodeskey
        -right subtreee pf a node has nodes with keys only greater than nodes key
        -left and right subtree each must also be a bst
        -no duplicate nodes allowed    
"""

#Search a key
