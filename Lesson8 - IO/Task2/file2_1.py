# -*- coding: utf-8 -*-
'''
Задание 2
Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными файлами.
'''
import os.path
import array

filename = 'numbers.bin'
filesize = os.path.getsize(filename)
print filesize
count = filesize//array.array('i').itemsize
# Fill in with zeros
numbers = array.array('i',(0 for i in range(count)))
with open (filename,'rb') as f:
    f.readinto(numbers)
print numbers

total = 0
for n in numbers:
    total += int(n)
print total

