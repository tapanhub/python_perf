#!/usr/bin/env python
"""using timeit"""

from timeit import timeit

items = {
    'a':1,
    'b':2,
}
default = -1


def use_catch(key):
    """Use try/cache to get a key with default"""
    try:
        return items[key]
    except KeyError:
        return default

def use_get(key):
    """use dict.get()"""
    return items.get(key, default)

if __name__ == '__main__':
    print("key is in dict")
    print('catch', timeit('use_catch("a")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("a")', 'from __main__ import use_get'))
    print("key is  missing")
    print('catch', timeit('use_catch("x")', 'from __main__ import use_catch'))
    print('get', timeit('use_get("x")', 'from __main__ import use_get'))
    import cProfile
    cProfile.run('use_catch("x")')

