# -*- coding: utf-8 -*-
'''
Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит
её отсортированной в порядке возрастания.
'''

def sort_numbers(text):
    '''
    If text contain elements which is not numbers, error occurres. These elements wouldn't be handled.
    :param text: Text input
    :return: Sorted sequence of numbers.
    '''
    _digits = []
    output_seq = 'Your sorted numbers: '
    errors = ''
    for d in str(text).split(','):
        try:
            _digits.append(float(d))
        except ValueError, e:
            errors += e.message + '\n'
    print _digits
    last_el = 0
    for el in sorted(_digits, key=float):
        last_el += 1
        if last_el >= len(_digits):
            output_seq += '%s. ' % el
        else:
            output_seq += '%s, ' % el
    if errors:
        output_seq += '\nErrors occurred during handling sequence of numbers:'+'\n' + errors
    return output_seq

if __name__ == '__main__':
    print 'Type "q" to exit'
    while True:
        seq = raw_input('Enter your numbers:')
        if seq == 'q':
            break
        else:
            print sort_numbers(seq)
