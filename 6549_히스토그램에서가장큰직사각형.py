#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    N, *l=list(map(int, input().split()))
    l.append(0)
    if N == 0: break
    s=[]
    a=0
    for i,h in enumerate(l):
        while s and l[s[-1]]>h:
            ih=l[s.pop()]
            w=i-s[-1]-1 if s else i
            if a<w*ih: a=w*ih
        s.append(i)
    print(a)

