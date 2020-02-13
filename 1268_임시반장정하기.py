#!/usr/bin/env python
# coding: utf-8

# In[5]:


def divide_list(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
    
    
        
student_num = int(input())
student_ban = []
reverse = []
answer = []
max_ele = 0
for i in range(student_num):
    answer.append(0)

for i in range(student_num):
    student_ban.append(list(input().split()))
for i in range(5):
    for k in range(student_num):
        reverse.append(student_ban[k][i])
reverse = list(divide_list(reverse,student_num))
for i in range(5):
    for k in range(student_num):
        if reverse[i].count(reverse[i][k])>1:
            answer[k] += 1
max_ele = max(answer)
print(answer.index(max_ele)+1)
       


    
        


# In[ ]:




