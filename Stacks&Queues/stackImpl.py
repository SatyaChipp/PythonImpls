# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:08:40 2018

@author: Jen
"""
class Stack:#LIFO
    def __init__(self):
        self.items=[] #stack impl as array
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self): #look at the top of stack without poppin it
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    def print_stack(self):
        for item in self.items:
            print(item)
    def reverse_stack(self):
        ##reverse stack
        self.revItems = self.items.reverse()
        ##or
        newlist = [item for item in reversed(self.items)]
        ##or as below
        for i in range(self.size()):
            print(self.items[self.size()-i-1])

if __name__ == "__main__":
    st = Stack()
    print(st.isEmpty())
    st.push(5)
    st.push('CA')
    st.push(True)
    st.push(6.7)
    print(st.peek())
    print(st.size())
    print(st.isEmpty())
    print(st.pop())
    st.print_stack()
    print("`````")
    st.reverse_stack()
        
