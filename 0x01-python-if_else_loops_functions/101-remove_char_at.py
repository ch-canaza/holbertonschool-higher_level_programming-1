#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for char in str:
        i++
        if i == n:
            continue
        else:
            str += char
    return char
