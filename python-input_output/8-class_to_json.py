#!/usr/bin/python3
'''Task 8 module'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structur'''
    return obj.__dict__
