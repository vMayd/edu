# -*- coding: utf-8 -*-

'''
Задание 2
Напишите программу-калькулятор, которая поддерживает следующие операции: сложение,
вычитание, умножение, деление и возведение в степень. Программа должна выдавать
сообщения об ошибке и продолжать работу при вводе некорректных данных, делении на
ноль и возведении нуля в отрицательную степень.
'''


class Calculator(object):
    """
    Calculator with exception handling
   """
    @staticmethod
    def add(num1, num2):
        try:
            result = num1 + num2
        except TypeError, e:
            print 'Error occurred: '+ e.message
        except ValueError, e:
            print 'Error occurred: '+ e.message
        else:
            return result

    @staticmethod
    def power(num, power):
        try:
            if num == 0 and power<0:
                raise TypeError('Impossible to raise  zero to the zero power ')
            else:
                result = num**power
        except TypeError, e:
            print 'Error occurred: ' + e.message
        else:
            return result


if __name__ == '__main__':

    print Calculator.add(33,4), Calculator.power(34,'we')

    while True:
        do = raw_input('Enter the operation -->')
        if do == 'quit':
            break
        else:
            try:
                result = eval(do)
            except TypeError, e:
                print 'Error: ' + e.message
            except ValueError, e:
                print 'Error: ' + e.message
            except ZeroDivisionError, e:
                print 'Error: ' + e.message
            except NameError,e:
                print 'Error: ' + e.message
            else:
                print 'Result: ', result
