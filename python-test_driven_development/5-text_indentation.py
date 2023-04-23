#!/usr/bin/python3
'''Text indentation module'''


def text_indentation(text):
    '''prints a text with two lines after these characters .?:'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
