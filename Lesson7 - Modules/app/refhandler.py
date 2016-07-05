# -*- coding: utf-8 -*-
__author__ = 'osboxes'

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