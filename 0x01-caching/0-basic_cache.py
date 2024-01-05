#!/usr/bin/python3
""" Python_caching _ystems """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Dict_caching_system """
    def put(self, key, item):
        """ Add_an_item_in_the_cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get_an_item_by_key """
        return self.cache_data.get(key)
