#!/usr/bin/env python3

'''
A module that defines the sum_list function.
'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    a type-annotated function sum_list which takes
    a list input_list of floats as argument and
    returns their sum as a float.
    '''
    result = 0.0
    for num in input_list:
        result += num
    return result
