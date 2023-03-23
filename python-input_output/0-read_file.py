#!/usr/bin/python3
'''Module task 0'''


def read_file(filename=""):
    '''Reading the file contents & printing to stdout'''
    with open(filename, 'r') as f:
        print(f.read(), end="")
