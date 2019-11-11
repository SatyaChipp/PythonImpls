# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:13:51 2018

@author: Jen
"""

class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class doubleLinkedLists(object):
    head=None
    tail=None
    
    def size(self):
        current = self.head
        count=0
        while current:
            count+=1
            current = current.next
        return count
        
    def insert(self, data, pos=None):
        new_node = Node(data)
        print("count {}".format(self.size()))
        if pos is None and self.head is None:
            self.head = self.tail =new_node #empty list
            #both pointers point to none
        elif pos == self.size(): #insert at tail
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        elif pos == 0 and self.head: #at head
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        elif pos!=0  and pos < self.size():
            current = self.head
            count=0
            while current.next and count<pos:
                count+=1
                current=current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            print("implt here")
        
        print("count {}".format(self.size()))
    
    def pop(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev is not None: #not head
                    current.prev.next = current.next
                    current.next.prev = current.prev.prev
                else:#head
                    current.next.prev = None
                    self.head = current.next
            current = current.next
                
    
    def printLL(self):
        print("show data")
        current =self.head
        while current:
            print(current.prev.data if hasattr(current.prev, "data") else None)
            print(current.data)
            print(current.next.data if hasattr(current.next, "data") else None)
            current=current.next
        
        
if __name__ == "__main__":
    dll = doubleLinkedLists()
    dll.insert(5)
    dll.insert(6, 0)
    dll.insert(7, 0)
    dll.insert(8, 0)
    dll.printLL()
        
        
    
    


