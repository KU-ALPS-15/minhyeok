#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
str = []
answer = []
for i in range(100):
    str.append(input())
    if str[i] == '.':
        break
num = len(str)
for i in range(num-1):
    answer.append('yes')
for i in range(num-1):
    stk = stack()
    #if not str[i][-1] == '.':
     #   answer[i] = 'no'
      #  continue
    for k in range(len(str[i])):
        if str[i][k] == '(':
            stk.push('(')
        elif str[i][k] == '[':
            stk.push('[')
           
        elif str[i][k] == ')':
            if not stk.pop() == '(':
                answer[i] = 'no'
               
        elif str[i][k] == ']':
            if not stk.pop() == '[':
                answer[i] = 'no'
               
    if not stk.empty():
        answer[i] = 'no'
for i in range(num-1):
    print(answer[i])
        
            
    
    


# In[ ]:




