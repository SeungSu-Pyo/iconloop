import json
import timeit
from typing import Any


def json_dumps(obj: Any, **kwargs) -> str:
    """
    Converts a python object `obj` to a JSON string
    :param obj: a python object to be converted
    :param kwargs: json options (see https://docs.python.org/3/library/json.html#json.dumps)
    :return: json string
    """
    return json.dumps(obj, **kwargs)


def json_loads(src: str, **kwargs) -> Any:
    """
    Parses a JSON string `src` and converts it to a python object
    :param src: a JSON string to be converted
    :param kwargs: kwargs: json options (see https://docs.python.org/3/library/json.html#json.loads)
    :return: a python object
    """
    return json.loads(src, **kwargs)


def len_dumps(count, repeat):
    for i in range(count):
        len_data = {
            'key': '0' * (i+1)
            }
        start = timeit.default_timer()
        for _ in range(repeat):
            json_dumps(len_data)
        end = timeit.default_timer()
        print('%3s : %s' % (i+1, end - start))


def len_loads(count, repeat):
    for i in range(count):
        len_data = {
            'key': '0' * (i+1)
            }
        json_data = json_dumps(len_data)
        start = timeit.default_timer()
        for _ in range(repeat):
            json_loads(json_data)
        end = timeit.default_timer()
        print('%3s : %s' % (i+1, end - start))


def item_dumps(count, repeat):
    item_data = {}
    for i in range(count):
        item_data['key[%s]' % (i+1)] = '0' * 40
        start = timeit.default_timer()
        for _ in range(1, repeat):
            json_dumps(item_data)
        end = timeit.default_timer()
        print('%2s item : %s' % (i+1, end - start))


def item_loads(count, repeat):
    item_data = {}
    for i in range(count):
        item_data['key[%s]' % (i+1)] = '0' * 40
        json_data = json_dumps(item_data)
        start = timeit.default_timer()
        for _ in range(1, repeat):
            json_loads(json_data)
        end = timeit.default_timer()
        print('%2s item : %s' % (i+1, end - start))


print("measure len_dumps start")
len_dumps(101, 100000)
print("measure len_dumps end")

print('-' * 100)

print("measure len_loads start")
len_loads(101, 100000)
print("measure len_loads end")

print('-' * 100)

print("measure item_dumps start")
item_dumps(51, 10000)
print("measure item_dumps end")

print('-' * 100)

print("measure item_loads start")
item_loads(51, 10000)
print("measure item_loads end")