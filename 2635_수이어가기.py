#!/usr/bin/env python
# coding: utf-8

# In[35]:


import copy

first = int(input())
max_num = 0
num_list = [first]
answer_list = []
for i in range(int(first*0.6),int(first*0.7)):
    num_list.append(i)
    for k in range(3000):
        temp = num_list[k]-num_list[k+1]
        
        if temp >=0:
            num_list.append(temp)
        else:
            break
    if max_num < len(num_list):
        max_num = len(num_list)
        answer_list = copy.deepcopy(num_list)
    
    del num_list[:]
    num_list.append(first)
print(max_num)
print(answer_list)

