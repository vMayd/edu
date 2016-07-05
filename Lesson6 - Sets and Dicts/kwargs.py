# -*- coding: utf-8 -*-
'''
Задание
Создайте словарь с ключами-строками и значениями-числами. Создайте функцию,
которая принимает произвольное количество именованных параметров. Вызовите её
с созданным словарём и явно указывая параметры.
'''

dictionary = {'one': 1, 'two': 2, 'three': 3,'hundred':100 }


def kwarg_handler(**kwargs):
    for key in kwargs:
        print 'Key = {0}, value = {1}'.format(key, kwargs[key])
if __name__ == '__main__':
    kwarg_handler(**dictionary)
    kwarg_handler(twenty=20, seven=7)
