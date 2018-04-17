#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        aa = 0
        ab = 0
    elif len(tuple_a) == 1:
        aa = tuple_a[0]
        ab = 0
    else:
        aa = tuple_a[0]
        ab = tuple_a[1]
    if len(tuple_b) == 0:
        ba = 0
        bb = 0
    elif len(tuple_b) == 1:
        ba = tuple_b[0]
        bb = 0
    else:
        ba = tuple_b[0]
        bb = tuple_b[1]
    a = aa + ba
    b = ab + bb
    new_tuple=(a, b)
    return new_tuple
