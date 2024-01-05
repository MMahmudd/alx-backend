#!/usr/bin/python3
""" Python_caching_systems """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU_caching_system
    Use_of_OrderedDict which_keep_order of_insertion of_keys
    The_order_shows_how_recently they_were_used.
    In_the_beginning_is_the_least_recently_used_and_in_the_end,
    the_most_recently_used.
    Any_update_OR_query_made_to_a_key_moves _o_the_end_(most_recently_used).
    If_anything_is_included,_it_is_added_at_the_end_(most_recently_used/added).
    All_operations_have_O(1)_time_complexity.
    """
    def __init__(self):
        """ Initialize_class_instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        First, add/ update the key by conventional methods.
        And also move the key to the end to show that it was recently used.
        But_here_we_will_also_check_if_the_length_of_our_dictionary
        has_exceeded_our_capacity.
        If_so_remove_the_first_key (least_recently_used)
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """ Get_an_item_by_key
        Return_the_value of_the_key that_is_queried_in O(1)
        and_return -1_if_the_key_is_not_found.
        And_also_move_the_key_to_the_end to show_that it_was_recently_used
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
