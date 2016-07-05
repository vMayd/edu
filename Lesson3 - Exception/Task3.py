# -*- coding: utf-8 -*-
'''
Задание 3
Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия,
отдел и год поступления на работу. Конструктор должен генерировать исключение,
если заданы неправильные данные. Введите список работников с клавиатуры. Выведите
всех сотрудников, которые были приняты после заданного года.
'''


class Employee(object):

    def __init__(self, first_name, second_name, department, year):
        if type(first_name) == str:
            if str(first_name)[0].isupper():
                self.first_name = first_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('First name cannot contain any digits')

        if type(second_name) == str:
            if str(second_name)[0].isupper():
                self.second_name = second_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('Second name cannot contain any digits')
        self.department = department
        if type(int(year)) == int:
            if int(year) > 2000:
                self.year = int(year)
            else:
                raise ValueError('Company establishing date is 2001')
        else:
            raise ValueError('Year should be type of int')

    def __str__(self):
        return '%s %s from %s department. Employed at %s' % (self.first_name,
                                                             self.second_name,
                                                             self.department,
                                                             self.year)

if __name__ == '__main__':
    e_list =[]
    e_list.append('you')
    for i in range(2):
        print 'Enter new employee'
        f_name = raw_input('First')
        s_name = raw_input('Second')
        dept = raw_input('Dept')
        year = raw_input('Year')
        emp = Employee(f_name, s_name, dept, year)
        e_list.append(emp)

    for e in e_list:
        try:
            if e.year > 2002:
                print e
        except AttributeError, e:
            print e.message



    '''
    jl = Employee('John', 'Lippman', 'Technical', 2004)
    all.append(jl)
    js = Employee('John', 'Steward', 'Technical', 2003)
    all.append(js)
    ls = Employee('Larry', 'Steward', 'Management', 2001)
    all.append(ls)

    for e in all:
        if e.year > 2001:
            print e
    '''

