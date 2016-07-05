# -*- coding: utf-8 -*-
'''
Задание 2
Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными файлами.
'''
import random
import array
numbers = [random.randint(-100000,100000) for n in range(0,10000)]
number_array = array.array('i', numbers)
with open ('numbers.bin','wb') as binary_file:
    binary_file.write(number_array)
print 'Done'
