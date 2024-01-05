#!/usr/bin/python3
""" Python_caching_systems """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO_caching_system """
    def __init__(self):
        """ Initialize_class_instance. """
        super().__init__()

    def put(self, key, item):
        """ Add_an_item _n_the_cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """ Get_an_item_by_key """
        return self.cache_data.get(key)
