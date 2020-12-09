# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:56:24 2020

@author: tugce
"""
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((5,6))
pq.put((6,6))
pq.put((8,6))

print(pq.queue)
pq.get()
print(pq.queue)