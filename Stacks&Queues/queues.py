# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:24:08 2018

@author: Jen
"""

class queue: #insert at end.. pop at front 
    def __init__(self):
        self.items = []
    
    def push(self, data):#push at back
        self.items.append(data)
    
    def pop(self):#pop at front
        self.items.pop(0) #pop at front 
    
    def rear(self):
        if len(self.items) !=0:
            return self.items[len(self.items)-1]
        else:
            return 'empty list'
    
    def front(self):
        if len(self.items) !=0:
            return self.items[0]
        else:
            return 'empty list'
        
    def printQ(self):
        for item in self.items:
            print(item)
    
    def minElem(self):
        #check if all items in list are of the same type
        if all(isinstance(x,(int, long, float)) for x in self.items)):
            print(sorted(self.items)) #to sort items in queue
            print(min(self.items))
        elif all(isinstance(x,(str)) for x in self.items)):
            print(sorted(self.items)) #to sort items in queue
            print(min(self.items))
        else:
            print("list has incompatible type")
            
    
    def do_smthng_items_queue(self, item):
        print( item + ' ')
        
        
if __name__ == '__main__':
    q = queue()
    q.push(567)
    q.push(789)
    q.push(235)
    q.push(456)
#    q.printQ()
    q.pop()
#    q.printQ()
    q.minElem()
    
        
        
        
