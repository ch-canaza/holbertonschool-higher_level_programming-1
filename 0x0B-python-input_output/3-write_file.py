#!/usr/bin/python3
def write_file(filename="", text=""):
    """ write a string to a text file and return num of char written"""
    with open(filename, 'r+') as f:
        return f.write(text)
