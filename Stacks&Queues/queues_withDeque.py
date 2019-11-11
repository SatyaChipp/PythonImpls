# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:56:38 2018

@author: Jen
"""
from collections import deque

if __name__ == '__main__':
    queue = deque([1, 2, 4, 6])
    queue.append(9) ##for enqueuing
    queue.append(12)
    
    print(queue)
    
    queue.popleft()#for dequeuing
    queue.popleft()
    
    print(queue)
    
        
