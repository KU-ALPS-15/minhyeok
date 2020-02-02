#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

msg_num = int(input())
if msg_num >10:
        sys.exit()
msg = input()
msg_list = []
answer = []
for i in range(msg_num):
        msg_list.append(msg[6*i:6*i+6])
for i in range(msg_num):
        if msg_list[i] == '000000'or'000001'or'000010'or'000100'or'001000'or'010000'or'100000':
            answer.append('A')
        elif msg_list[i] == '001110'or'001101'or'001011'or'000111'or'011111'or'101111'or'001111':
            answer.append('B')
        elif msg_list[i] == '010011'or'110011'or'000011'or'011011'or'010111'or'010001'or'010010':
            answer.append('C')
        elif msg_list[i] == '011100'or'111100'or'001100'or'010100'or'011000'or'011110'or'011101':
            answer.append('D')
        elif msg_list[i] == '100110'or'000110'or'110110'or'101110'or'100010'or'100100'or'100111':
            answer.append('E')
        elif msg_list[i] == '101001'or'001001'or'111001'or'100001'or'101101'or'101011'or'101000':
            answer.append('F')
        elif msg_list[i] == '110101'or'010101'or'100101'or'111101'or'110001'or'110111'or'110100':
            answer.append('G')
        elif msg_list[i] == '111010'or'011010'or'101010'or'110010'or'111110'or'111000'or'111011':
            answer.append('H')
        else:
            answer.append(str(i+1))
for i in range(msg_num):
        print(answer[i],end='')
        

