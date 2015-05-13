import json
import os


class Statistics(object):
    """Dict-like container for statistics

    Instead of just setting values, it remembers how many each value was set
    for any particular field
    """


def is_nested(value):
    """Returns true if value has other values inside"""
    return isinstance(value, (dict, list))


def get_type(value):
    """Returns string indicating type of the field"""
    if isinstance(value, None):
        return 'null'
    if isinstance(value, int):
        return 'int'
    if isinstance(value, basestring):
        return 'string'


def iterate_over(value):
    if isinstance(value, list):
        pass
    elif isinstance(value, dict):
        pass
    # value_type = get_type(value)


JSON_DIR = 'data'
objs = []
for filename in os.listdir(JSON_DIR):
    with open('jsons/%s' % filename, 'r') as f:
        objs.append(json.load(f))
