# -*- coding: utf-8 -*-
'''
Задание 3
Напишите программу, которая вводит с клавиатуры текст и выводит
отсортированные по алфавиту слова данного текста.
'''

def sort_text(text):
    words = text.split(' ')
    print words
    sorted_words = sorted(words, key=str.lower)
    return sorted_words

if __name__ == '__main__':
    while True:
        typed_text = raw_input('Type in your text here:')
        if typed_text == 'quit':
            break
        else:
            for _ in sort_text(typed_text):
                print _


