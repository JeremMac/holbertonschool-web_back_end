#!/usr/bin/env python3
'''
A module that define index_function
and contains Server class.
'''


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        A method named get_page that takes two
        integer arguments page with default value 1
        and page_size with default value 10.

        Return the result of the indexed pages.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_index: tuple = index_range(page, page_size)
        data = self.dataset()

        result_page = data[page_index[0]:page_index[1]]
        return result_page
