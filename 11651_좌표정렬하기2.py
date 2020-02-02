#!/usr/bin/env python
# coding: utf-8

# In[ ]:


coord_num = int(input())

coord_list = []
for _ in range(coord_num):
    coord_list.append(list(map(int, input().split())))
coord_list = sorted(coord_list, key = lambda x : (x[1], x[0]))

for coord in coord_list:
    print(*coord)

