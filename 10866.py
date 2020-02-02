#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class deque:
    def __init__(self):
        self.items = []
    def empty(self):
        return not self.items
    def push_back(self, item):
        self.items.append(item)
    def push_front(self, item):
        self.items.insert(0,item)
    def pop_front(self):
        if not self.items:
            return -1
        else: 
            return self.items.pop(0)
    def pop_back(self):
        if not self.items:
            return -1
        else: 
            return self.items.pop()
    def size(self):
        return len(self.items)
    def front(self):
        if not self.items:
            return -1
        else: 
            return self.items[0]
    def back(self):
        if not self.items:
            return -1
        else: 
            return self.items[-1]
num = int(input())
dq = deque()
for i in range(num):
    cmd = input()
    if cmd == 'push_back':
        dq.push_back(input())
    elif cmd == 'push_front':
        dq.push_front(input())
    elif cmd == 'front':
        print(dq.front())
    elif cmd == 'back':
        print(dq.back())
    elif cmd == 'size':
        print(dq.size())
    elif cmd == 'empty':
        print(dq.empty())
    elif cmd == 'pop_front':
        print(dq.pop_front())
    elif cmd == 'pop_back':
        print(dq.pop_back())

