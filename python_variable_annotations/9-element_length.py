#!/usr/bin/env python3

'''
A module that defines the element_length function.
'''


from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    A given function that return a list.
    '''
    return [(i, len(i)) for i in lst]
