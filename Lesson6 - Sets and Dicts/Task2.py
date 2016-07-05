# -*- coding: utf-8 -*-
'''
Задание 2
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок.
Должна быть реализована возможность ввода изначальной ссылки и короткого
названия и получения изначальной ссылки по её названию.
'''

if __name__ == '__main__':
    end = False
    ref_holder = {}
    keys = []
    values =[]
    print 'Ok. Lets make it ease to read!'

    for n in range(0,2):
        key = raw_input('Enter short name: ')
        value = raw_input('Enter full name of reference: ')
        if n == len(range(0, 2))-1:
            end = True
        keys.append(key)
        values.append(value)
        if end:
            pack = zip(keys,values)
            ref_holder = dict(pack)
            print ref_holder

    print 'Now, lets retrieve some full references:'
    for n in range(0,2):
        key = raw_input('Enter short name: ')
        print ref_holder.get(key, 'Reference not found')
