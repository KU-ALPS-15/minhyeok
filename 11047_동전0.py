#!/usr/bin/env python
# coding: utf-8

# In[12]:


soo,hap = map(int,input().split())
money = []
answer = 0
for i in range(soo):
    money.append(int(input()))
money = sorted(money)
for i in range(1,soo+1):
    if money[-1*i] <= hap:
        answer += int(hap/money[-1*i])
        hap %= money[-1*i]
    if hap == 0 :
        break
print(answer)


# In[11]:


16/3

