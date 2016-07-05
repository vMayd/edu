# -*- coding: utf-8 -*- 
'''
Задание
Создайте обычную функцию умножения двух чисел. Частично примените её к одному аргументу.
Создайте каррированную функцию умножения двух чисел. Частично примените её к одному аргументу.
'''
__author__ = 'osboxes'
from functools import partial


def mul_curr(x):
    """
    Currying multiplication function
    """
    def mul_y(y):
        return x + y
    return mul_y


def mul(x, y):
    return x * y

#Partial  using of currying function
print mul_curr(5)(10)
#Partial using of function with functools.partial
add_to_nine = partial(mul, 9)
print add_to_nine(10)
print add_to_nine(88)



