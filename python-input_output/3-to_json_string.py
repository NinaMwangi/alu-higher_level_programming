#!/usr/bin/python3
'''Task 3 module'''
import json


def to_json_string(my_obj):
    '''Return the JSON representaion of a (obj)string'''
    return json.dump(my_obj)
