# -*- coding: utf-8 -*-
__author__ = 'osboxes'
'''
Задание 3
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий
задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной
шкале, а получены в другой.
'''


class Temperature:

    def __init__(self):
        pass

    @property
    def celsius_temp(self):
        return (self.fahrenheit_temp - 32)*5/9

    @celsius_temp.setter
    def celsius_temp(self, value):
        self.celsius_temp = value

    @property
    def fahrenheit_temp(self):
        return (self.celsius_temp * 9/5) + 32

    @fahrenheit_temp.setter
    def fahrenheit_temp(self,value):
        self.fahrenheit_temp = value

temp = Temperature()
temp.celsius_temp = 40.0


print temp.celsius_temp
print temp.fahrenheit_temp







