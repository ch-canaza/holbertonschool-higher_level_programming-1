#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        new = dict()
        for k, v in a_dictionary.items():
            if v != value:
                new[k] = v
        return new
