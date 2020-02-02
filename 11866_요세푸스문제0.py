#!/usr/bin/env python
# coding: utf-8

# In[9]:


class que:
    def __init__(self):
        self.items = []
    def empty(self):
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            return -1
        else: 
            return self.items.pop(0)
    def size(self):
        return len(self.items)
    def front(self):
        if not self.items:
            return -1
        else: 
            return self.items[0]
    def back(self):
        if not self.items:
            return -1
        else: 
            return self.items[-1]
N,K = map(int,input().split())
q = que()
answer = []
for i in range(1,N+1):
    q.push(i)
while True:
    for i in range(K-1):
        q.push(q.pop())
    answer.append(q.pop())
    if q.empty():
        break
print('<'+','.join(map(str,answer))+'>')

    
        
    

