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
    first_duration = None

    for i in range(count):
        len_data = {'key': '0' * i}

        start = timeit.default_timer()
        for _ in range(repeat):
            json_dumps(len_data)
        duration = timeit.default_timer() - start

        if first_duration is None:
            first_duration = duration
            continue

        delta = (duration - first_duration) / i

        print(f'{i:>3} : {duration} : {delta}')


def len_loads(count, repeat):
    first_duration = None

    for i in range(count):
        len_data = {'key': '0' * i}
        json_data = json_dumps(len_data)

        start = timeit.default_timer()
        for _ in range(repeat):
            json_loads(json_data)
        duration = timeit.default_timer() - start

        if first_duration is None:
            first_duration = duration
            continue

        delta = (duration - first_duration) / i

        print(f'{i:>3} : {duration} : {delta}')


def item_dumps(count, repeat):
    item_data = {}
    first_duration = None

    for i in range(count):
        item_data[f'key{i}'] = '0' * 40

        start = timeit.default_timer()
        for _ in range(repeat):
            json_dumps(item_data)
        duration = timeit.default_timer() - start

        if first_duration is None:
            first_duration = duration
            continue

        delta = (duration - first_duration) / i

        print(f'{i:>2} item : {duration} : {delta}')


def item_loads(count, repeat):
    item_data = {}
    first_duration = None

    for i in range(count):
        item_data[f'key{i}'] = '0' * 40
        json_data = json_dumps(item_data)

        start = timeit.default_timer()
        for _ in range(repeat):
            json_loads(json_data)
        duration = timeit.default_timer() - start

        if first_duration is None:
            first_duration = duration
            continue

        delta = (duration - first_duration) / i

        print(f'{i:>2} item : {duration} : {delta}')


def main():
    print("measure len_dumps start")
    len_dumps(100, 100000)
    print("measure len_dumps end")

    print('-' * 100)

    print("measure len_loads start")
    len_loads(100, 100000)
    print("measure len_loads end")

    print('-' * 100)

    print("measure item_dumps start")
    item_dumps(100, 10000)
    print("measure item_dumps end")

    print('-' * 100)

    print("measure item_loads start")
    item_loads(100, 10000)
    print("measure item_loads end")


if __name__ == '__main__':
    main()
