#!/usr/bin/env python3

'''
A module that defines the to_kv function.
'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    a type-annotated function to_kv
    that takes a string k and an int OR
    float v as arguments and returns a tuple.
    '''
    my_tuple: Tuple[str, float] = (k, v ** 2)
    return my_tuple
