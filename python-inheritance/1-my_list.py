#!/usr/bin/python3
'''The module for task 1'''


class MyList(list):
    '''This is a subclass of list'''

    def print_sorted(self):
        '''Print a sorted list in ascending order'''
        print(sorted(self))
