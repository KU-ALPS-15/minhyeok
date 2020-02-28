#!/usr/bin/env python
# coding: utf-8

# In[2]:


N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_count = {}
for n in N_list:
    try:
        N_count[n] += 1
    except:
        N_count[n] = 1

answer = []
for m in M_list:
    try: 
        answer.append((N_count[m]))
    except:
        answer.append(0)

for i in answer:
    print(i, end = ' ')

