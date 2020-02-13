#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())

def fibo3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b%1000000, (a+b)%1000000

    return a 

print(fibo3(n%(15*(10**5))))

