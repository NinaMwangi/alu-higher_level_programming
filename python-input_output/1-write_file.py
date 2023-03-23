#!/usr/bin/python3
'''Task 1 Module'''


def write_file(filename="", text=""):
    '''Writes a string to text file & returns number of characters'''
    with open(filename) as f:
        return len(f.readline())
