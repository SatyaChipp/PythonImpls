# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:05:23 2018

@author: Jen
"""

class Node:
    def __init__(self, data):
        self.data =data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            
        else:#stack -- insert at head - cant insert 
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def pp(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        
if __name__ == '__main__':
    st = Stack()
    st.push(45)
    st.push(56)
    st.push(90)
    st.push(67)
    st.pp()
    print(st.pop())
    st.pp()
    
    
    
    
