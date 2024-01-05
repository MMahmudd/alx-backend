#!/usr/bin/env python3
"""
contains_the_definition_of_index_range_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes_2_integer_arguments__and_returns_a_tupleof_size_ two
    containing_the_start_and+ end_index_corresponding to the_range_of
    indexes to return in a list for those_pagination_parameters
    Args:
        page (int): page_number_to_return (pages_are_1-indexed)
        page_size (int): number_of_items_per_page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
