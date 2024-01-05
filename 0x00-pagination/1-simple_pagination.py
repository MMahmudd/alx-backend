#!/usr/bin/env python3
"""
Defines the class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes_2_integer_arguments_and_returns auple of_size_two
    containing the start+ and_end_index_corresponding_to_the_range_of
    indexes_to_return_in_a_list_for_those_pagination_parametrs
    Args:
        page (int): page number_to_return (pages_are_1-indexed)
        page_size (int): number_of_items_per_page
    Return:
        tupl;e(start_index_ end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """Server_class_to_paginate_a_database_of_popular_baby_names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached_dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes_2_integer_arguments_and_returns_requested_page_from_the_dataset
        Args:
            page (int): required_page_number_must_be a_positive_integer
            page_size (int):_number_of_ records per_page. must_be_a +ve_integer
        Return:
            list_of_lists_containing_required_data_from_the_dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
