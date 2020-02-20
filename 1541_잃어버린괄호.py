#!/usr/bin/env python
# coding: utf-8

# In[25]:


ip = input().split('-')
temp = []

ip_len = len(ip)
for i in range(ip_len):
    t = '0'
    ip[i]=ip[i].split('+')
    ip[i] = list(map(int,ip[i]))
    ip[i] = sum(ip[i])
answer = ip[0]
for i in range(len(ip)-1):
    answer -= ip[i+1]
print(answer)

