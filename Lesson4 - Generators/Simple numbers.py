# -*- coding: utf-8 -*-
'''
Напишите функцию-генератор для получения n первых простых чисел.
'''
def simple_number_generator(amount):
    """
    Function realizes Sieve of Sundaram algorithm
    :param amount: Amount of first n members of sequence
    :return: Sequence of first n simple numbers
    """
    n = amount*10
    num = []
    r = xrange(1, n+1)
    for i in xrange(1, n):
        for j in xrange(i, n):
            a = i+j+2*i*j
            if a <= n and a not in num:
                num.append(a)
    m = set(num).symmetric_difference(set(r))
    l = list(m)
    for v in range(amount):
        yield 2*l[v] + 1

def _simple_number_generator(n):
    """
    Function realize Sieve of Sundaram algorithm
    :param n: Higher limit of N numbers sequence
    :return: Sequence of  simple numbers
    """
    num = []
    r = xrange(1, n+1)
    for i in xrange(1, n):
        for j in xrange(i, n):
            a = i+j+2*i*j
            if a <= n and a not in num:
                num.append(a)
    m = set(num).symmetric_difference(set(r))
    l = list(m)
    for v in l:
        yield 2*v + 1

if __name__ == '__main__':
    h = simple_number_generator(5)
    for b in h:
        print b
    print 40 *'-'
    lk = _simple_number_generator(10)
    for b in lk:
        print b








