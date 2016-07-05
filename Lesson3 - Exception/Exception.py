# -*- coding: utf-8 -*-
'''
Задание
Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать
данное исключение, если пользователь введёт определённое значение, и перехватите
это исключение при вызове функции.
'''


class BannedWordException(Exception):

    def __init__(self, word):
        self.word = word
        self.message = 'You are trying to use banned word "%s"!!!' % self.word

if __name__ == '__main__':

    while True:
        word = raw_input("Let's check the word: ")
        if word == 'b_w':
            with open('swearWords.txt', 'r') as banned_words:
                for w in banned_words:
                    print w
        else:
            with open('swearWords.txt', 'r') as file:
                try:
                    banned_words = [w.replace('\r\n', '').lower() for w in file.readlines()]
                    if word.lower() in banned_words:
                        raise BannedWordException(word)
                except BannedWordException, e:
                    print e.message
                else:
                    print 'This is permitted word. You can use it'
