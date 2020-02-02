#!/usr/bin/env python
# coding: utf-8

# In[7]:


# stack
class stack:
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
            return self.items.pop()
    def size(self):
        return len(self.items)
    def top(self):
        if not self.items:
            return -1
        else: 
            return self.items[-1]
num = int(input())
answer = []
list = []
for i in range(num):
    list.append(input())
for i in range(num):
    answer.append('YES')
for k in range(len(list)):
    stk = stack()
    for j in range(len(list[k])):
        if list[k][j] == ')':
            if stk.pop() == -1:
                answer[k] = 'NO'
        else:
            stk.push('(')
    if not stk.empty():
        answer[k] = 'NO'

for i in range(num):
    print(answer[i])
    
        

