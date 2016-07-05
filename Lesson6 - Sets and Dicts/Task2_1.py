# -*- coding: utf-8 -*-
'''
Задание 2
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок.
Должна быть реализована возможность ввода изначальной ссылки и короткого
названия и получения изначальной ссылки по её названию.
'''

class ReferenceHandler(object):
    """

    """
    def __init__(self):
        self.storage = {}

    def add_reference(self):
        original_ref = raw_input("Enter original reference : ")
        short_ref = None
        while not short_ref or short_ref in self.storage:
            short_ref = raw_input("Enter short name of the reference:")
            if short_ref in self.storage:
                print 'This name already exist \n (url: {})'.format(self.storage[short_ref])
        self.storage[short_ref] = original_ref

    def get_reference(self):
        name = raw_input('Enter reference name: ')
        url = self.storage.get(name, None)
        if url:
            print url
        else:
            print('Link does not exist')


def main():
    ref_handler = ReferenceHandler()

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = input('> ')
        if choice == 1:
            ref_handler.add_reference()
        elif choice == 2:
            ref_handler.get_reference()
        elif choice == 3:
            break
        else:
            print 'Incorrect input'
        print


if __name__ == '__main__':
    main()