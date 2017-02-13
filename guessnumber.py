# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:10:16 2017

@author: wyd
"""

import random
number =['0','1','2','3','4','5','6','7','8','9']
numbers =['0','1','2','3','4','5','6','7','8','9']
a1 = numbers.pop(random.randint(0,9))
a2 = numbers.pop(random.randint(0,8))
a3 = numbers.pop(random.randint(0,7))
a4 = numbers.pop(random.randint(0,6))
b=[]
b.append(a1)
b.append(a2)
b.append(a3)
b.append(a4)

print('猜一个四位数，四个数字不同，数和位置都对的个数是A，数对位置不对的个数为B')
print('现在输入四位数吧')

def cha_c():
    c=raw_input(">")
    while not(len(c)== 4 and c[0] in number and c[1] in number and c[3] in number):
        print ('别闹，输入四个数字')
        c=raw_input(">")
    return c
    print c
    
d=cha_c()

def compare(d,b):
    A=0
    B=0
    for i in range(0,4):
        if d[i]==b[i]:
            A = A + 1
    for i in range(0,4):
        if d[i] == b[0] or d[i] == b[1] or d[i] == b[2] or d[i] == b[3]:
            B = B + 1
    B = B-A
    print 'A = %s , B = %s'%(A,B)
    return A,B
    
[A,B] = compare(d,b)
num = 9
while A!=4 and num>0:
    print('还有%s次机会' % num)
    num = num-1
    d = cha_c()
    [A , B] = compare(d , b)
b = int(b[0] + b[1] + b[2] +b[3])
if A!=4:
    print('没猜出来吧，答案是%s' %b)
else:
    print('猜对了，那个数就是%s' %b)
    
