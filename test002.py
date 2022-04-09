# -*- coding = UTF-8 -*-
# @Time: 2020/6/29 16:09
# @Author: sudo
# @Site: 
# @File: test002.py
# @Software: PyCharm

import random

a = random.randint(0, 9)
b = random.randint(0, 9)
# print("%d\n" % a)
# print("%d\n" % b)
print(a)
print(b)
print(a * b)
print('-' * 50 + '乘法口诀表' + '-' * 50)
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print('%d X %d = %d' % (j, i, j * i), end='\t')
    print()
print('\n' + '-' * 50 + '字符分割' + '-' * 50)
name = 'alligator'
for x in name:
    print(x, end='\t')
print('\n' + '-' * 50 + '数组' + '-' * 50)
arr1 = ['pip3', 'install', 'pycrypto']

for x in range(len(arr1)):
    print(x, arr1[x], end='\t')
print('\n' + '-' * 50 + 'while' + '-' * 50)
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 1
print(sum)

i = 0
while i < 10:
    i += 1
    print('-' * 30)
    if i == 5:
        continue
    elif i == 10:
        break
    print(i)
print('-' * 50 + 'while循环实现乘法口诀表' + '-' * 50)
m = 0
n = 1
while m < 9:
    m += 1
    while n <= m:
        print('%d X %d = %d' % (n, m, n * m), end='\t')
        n += 1
    n = 1
    print()
