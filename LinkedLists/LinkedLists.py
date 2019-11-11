# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:35:25 2018
@author: Jen
"""
#implement python linked lists
from . import Node
class LinkedList(object):
    def __init__(self, head=None): #set to none - first node none before initiliation
        self.head = head

    def insertatHead(self, data):#time complexity O(1)
        ##insert at head ---simplest
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node #point head to new node

    def insert_atTail(self, head, data): #head may or maynot be given - use class head if not given
        current = self.head
        if current is None:
            current = Node(data)
        while current:
            if current.get_next() is None:
                current.set_next(Node(data))
                return current
            current = current.get_next()

    def insert_afterNode(self, prev_node, data):
        if prev_node is None:
            raise ValueError("not in list")
        new_node = Node(data)
        new_node.set_next(prev_node)
        prev_node.set_next(new_node)

    def insertAfterPosition(self, pos, data):
        node = Node(data)
        if pos==0:
            self.insertatHead(data)
        elif pos>self.size():
            print("out of bounds!")
        elif pos==self.size():
            self.insert_atTail(self.head, data)
        else:
            currPos = 0
            previous=None
            current = self.head
            while(currPos < pos) and current.get_next():
                previous = current
                current = current.get_next()
                currPos +=1
            previous.set_next(node)
            node.set_next(current)
        return head

    def size(self):#time complexity - O(n) - each node visited exactly once
        current = self.head
        count=0
        while current:
            count+=1
            current = current.get_next()
        return count

    def search_traverse(self, data):#time complexity - O(n) worst case
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("not in list")
        return current

    def delete(self, data):
        current = self.head
        found = False
        previous = None
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("not in list")
        if previous is None:
            self.head = current.get_next()#point it last node
        else:
            previous.set_next(current.get_next()) #point previous to currents next.. so current is deleted

    def printRecursivly(self, head):
        if head:
            print(head.get_data())
            self.printRecursivly(head.get_next())
    
    def printReverse(self, head):
        if head:
            self.printReverse(head.get_next())
            print(head.get_data())
        else:
            return
    def reverseLL(self, head): ##check this !
        prev=None
        current = head
        while current:#A B C D
            nextnode = current.get_next() #B
            current.set_next(prev)#A->none
            prev=current#A
            current=nextnode #B
        head=prev


if __name__ == "__main__":
    head = Node(23)
    node2 = Node(45)
    node3 = Node(56)
    head.next_node = node2
    node2.next_node = node3
    ll = LinkedList(head)
    print(ll.printRecursivly(head))
    print(node1.data)
