# -*- coding: utf-8 -*-
__author__ = 'osboxes'
import refhandler


def run():

    ref_handler = refhandler.ReferenceHandler()

    while True:
        print('A = Add link')
        print('G =  Get link')
        print('E = Exit')

        choice = raw_input('> ')
        if choice == 'A':
            ref_handler.add_reference()
        elif choice == 'G':
            ref_handler.get_reference()
        elif choice == 'E':
            break
        else:
            print 'Incorrect input'
        print

