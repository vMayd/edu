# -*- coding: utf-8 -*-
'''
Задание 1
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.
'''

import random

numbers = [random.randint(-100000,100000) for n in range(0,10000)]
with open('numbers.txt', 'w') as f:
    for n in numbers:
        f.write(str(n)+'\n')
