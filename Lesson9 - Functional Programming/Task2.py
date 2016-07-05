# -*- coding: utf-8 -*-
'''
Задание 2
Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.
'''

import random

numbers = [random.randint(10,1000) for n in range(0,1000)]
print numbers
print len(numbers)
filtered = filter(lambda x: x % 2 != 0, numbers)
num_sq = map(lambda y: y**2, filtered)
print '*'*20
print num_sq
print len(num_sq)
