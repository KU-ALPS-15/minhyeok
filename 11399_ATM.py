#!/usr/bin/env python
# coding: utf-8

# In[9]:


soo = int(input())
person = input().split()
person = sorted(person)
waiting = 0
answer = 0
for i in range(soo):
    waiting += int(person[i])
    answer += waiting
print(answer)

