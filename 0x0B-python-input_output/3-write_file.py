#!/usr/bin/python3
""" contains the write_file function """


def write_file(filename="", text=""):
    """ write a string to a text file and return num of char written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
