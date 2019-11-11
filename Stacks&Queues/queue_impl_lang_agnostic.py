# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:56:38 2018

@author: Jen
"""
    
class Queue: #language agnostic approach
    def __init__(self):
        self.queue = []
        self.maxSize = 3
        self.head = 0
        self.tail = 0
        
    def enqueue(self, data):
        #check if queue is full
        if self.size() >= self.maxSize:
            return ("queue fuul!")
        self.queue.append(data)
        self.tail +=1
        return True
    
    def dequeue(self):
        if self.size() <=0:
            self.resetQue()
            return ("Resetting Q..que empty")
        data =self.queue[self.head]
        self.head+=1
        return data
    
    def size(self):
        return self.tail - self.head
    
    def resetQue(self):
        self.tail=0
        self.head=0
        self.queue = []

from collections import deque

if __name__ == '__main__':
    
    qq = Queue()
    print(qq.enqueue(1))
    print(qq.enqueue(2))
#    print(qq.enqueue(34))
#    print(qq.enqueue(23))
    print(qq.size())
    
    print(qq.dequeue())
    print(qq.dequeue())
    print(qq.dequeue())
    
    
