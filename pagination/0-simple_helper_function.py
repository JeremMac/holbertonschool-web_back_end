#!/usr/bin/env python3


'''
A module that defines the index_range function.
'''

import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    '''
    A function named index_range that takes two
    integer arguments page and page_size.

    Returns a tuple of size two containing a start
    index and an end index corresponding to the
    range of indexes
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
