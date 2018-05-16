#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ reads a n lines of a text file and prints them to stdout """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    with open(filename) as f:
        if 0 < nb_lines < count:
            for i in range(nb_lines):
                print(f.readline(), end="")
                i += 1
        else:
            for line in f:
                print(line, end="")
