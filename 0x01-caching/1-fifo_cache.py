#!/usr/bin/python3
""" Python_cahing_systems """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO_caching_system """
    def __init__(self):
        """ Initialize_class_instance. """
        super().__init__()

    def put(self, key, item):
        """ Add_an_item_in_the_cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ Get_an_item_by_key """
        return self.cache_data.get(key)
