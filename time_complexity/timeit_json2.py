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

# def measure_time():
#     start = timeit.default_timer()
#     for i in range(1, 101):
#
#     end = timeit.default_timer()

# def measure_time(func):
#     if func == len_dumps:
#         for i in range(1, 101):
#             start = timeit.default_timer()
#             for j in range(1, 1000):
#                 func(j)
#             end = timeit.default_timer()
#             print('key[%3s] : %s' % (i, end - start))

    # elif func == len_loads:
    #     for i in range(1, 101):
    #         start = timeit.default_timer()
    #         for j in range(1, 10000):
    #             func(j)
    #         end = timeit.default_timer()
    #         print('key[%3s] : %s' % (i, end - start))
    #
    # elif func == item_dumps:
    #     for i in range(1, 51):
    #         start = timeit.default_timer()
    #         for j in range(1, 100):
    #             func(j)
    #         end = timeit.default_timer()
    #         print('%2s item : %s' % (i, end - start))
    #
    # else:
    #     for i in range(1, 51):
    #         start = timeit.default_timer()
    #         for j in range(1, 1000):
    #             func(j)
    #         end = timeit.default_timer()
    #         print('%2s item : %s' % (i, end - start))


def len_dumps():
    for i in range(1, 101):
        len_data = {
                'key': '0' * i
        }
        print(json_dumps(len_data))
        start = timeit.default_timer()
        for j in range(1, 100000):
            json_dumps(len_data)
        end = timeit.default_timer()
        print('%3s : %s' % (i, end - start))

# def len_loads(i):
#     len_data = {
#         'key': '0' * i
#     }
#     json_dumps(len_data)
#
#
# def item_dumps(i):
#     item_data['key[%s]' % i] = '0' * 40
#     json_dumps(item_data)
#
#
# def item_loads(i):
#     item_data['key[%s]' % i] = '0' * 40
#     json_dumps(item_data)

len_dumps()
# measure_time(len_dumps)

print('-' * 100)

# item_data = {}
# measure_time(item_dumps)
#
# print('-' * 100)
#
# measure_time(len_loads)
#
# print('-' * 100)
#
# measure_time(item_loads)