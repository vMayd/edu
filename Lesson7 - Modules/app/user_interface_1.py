# -*- coding: utf-8 -*-
__author__ = 'osboxes'
import refhandler


def run():

    ref_handler = refhandler.ReferenceHandler()

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = raw_input('> ')
        if choice == '1':
            ref_handler.add_reference()
        elif choice == '2':
            ref_handler.get_reference()
        elif choice == '3':
            break
        else:
            print 'Incorrect input'
        print

