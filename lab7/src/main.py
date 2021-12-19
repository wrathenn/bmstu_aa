#!/usr/bin/env python3

import csv
import random
import time
from matplotlib import pylab

import search

_REPEATS = 100

def read_data():
    phones_dict = {}
    with open('phone_models_dict.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phones_dict[row['model']] = 'successfully found'
    return phones_dict


def sort(_dict: dict[str, str]) -> dict[str, str]:
    return dict(sorted(_dict.items()))


def get_time(func, arg):
    _sum = 0
    for i in range(_REPEATS):
        start = time.time()
        if arg:
            func(arg)
        else:
            func()
        _sum += (time.time() - start)
    return round(_sum / _REPEATS, 6)


def get_time_search(searcher: search.BaseSearcher, _key):
    _sum = 0
    for i in range(_REPEATS):
        start = time.time()
        searcher.search(_key)
        _sum += (time.time() - start)
    return _sum / _REPEATS

def get_time_search_random(searcher: search.BaseSearcher, _dict: dict[str, str]):
    _sum = 0
    for i in range(_REPEATS):
        start = time.time()
        rand = random.choice(list(_dict.keys()))
        searcher.search(rand)
        _sum += (time.time() - start)
    return _sum / _REPEATS


def test_time(_dict: dict, sorted_dict,
              simple_searcher: search.SimpleSearcher,
              binary_searcher: search.BinarySearcher,
              combined_searcher: search.CombinedSearcher):
    regular_dict_keys: [str] = list(_dict.keys())
    regular_first_key: str = regular_dict_keys[0]
    regular_last_key: str = regular_dict_keys[-1]

    sorted_dict_keys: [str] = list(sorted_dict.keys())
    sorted_first_key: str = sorted_dict_keys[0]
    sorted_center_key: str = sorted_dict_keys[(len(sorted_dict_keys) - 1) // 2]
    sorted_last_key: str = sorted_dict_keys[-1]

    # -------------------------------------------------
    print("Лексикографическая сортировка ", get_time(sort, _dict), "cекунд")
    print("Частотный анализ и лексикографическая сортировка ",
          get_time(lambda: combined_searcher.frequency_analysis(), None), "cекунд")

    print("\nПоиск ключа при лучшем случае")
    print(f"Полный перебор {get_time_search(simple_searcher, regular_first_key):6f} cекунд")
    print(f"Бинарный поиск {get_time_search(binary_searcher, sorted_center_key):6f} секунд")
    print(f"Комбинированный алгоритм {get_time_search(combined_searcher, 'OT 153 --- Mitsubishi'):6f} секунд")

    print("\nПоиск ключа при худшем случае")
    print(f"Полный перебор {get_time_search(simple_searcher, regular_last_key):6f} cекунд")
    print(f"Бинарный поиск {get_time_search(binary_searcher, sorted_last_key):6f} секунд")
    print(f"Комбинированный алгоритм {get_time_search(combined_searcher, 'm21i --- Ericsson'):6f} секунд")

    print("\nПоиск несуществующего ключа")
    print(f"Полный перебор {get_time_search(simple_searcher, '0'):6f} cекунд")
    print(f"Бинарный поиск {get_time_search(binary_searcher, '0'):6f} секунд")
    print(f"Комбинированный алгоритм {get_time_search(combined_searcher, '0'):6f} секунд")

    print("\nПоиск случайного ключа")
    print(f"Полный перебор {get_time_search_random(simple_searcher, _dict):6f} cекунд")
    print(f"Бинарный поиск {get_time_search_random(binary_searcher, _dict):6f} секунд")
    print(f"Комбинированный алгоритм {get_time_search_random(combined_searcher, _dict):6f} секунд")

    time_simple = []
    time_bin = []
    time_combined = []

    x_list = [i for i in range(len(_dict.keys()))]
    for d in list(_dict.keys()):
        time_simple.append(get_time_search(simple_searcher, d))
        time_bin.append(get_time_search(binary_searcher, d))
        time_combined.append(get_time_search(combined_searcher, d))

    pylab.xlabel('Индекс ключа')
    pylab.ylabel('Время, секунды')
    pylab.plot(x_list, time_simple, 'r--', label='Полный перебор')
    pylab.plot(x_list, time_bin, color='yellow', label='Бинарный поиск')
    pylab.plot(x_list, time_combined, 'b-.', label='Комбинированный')
    pylab.legend(loc='upper left')
    pylab.show()

    x1_list = []
    time_simple1 = []
    time_bin1 = []
    time_combined1 = []

    for i in range(len(x_list)):
        if i % 15 == 0:
            x1_list.append(i)
            time_simple1.append(time_simple[i])
            time_bin1.append(time_bin[i])
            time_combined1.append(time_combined[i])

    pylab.xlabel('Индекс ключа')
    pylab.ylabel('Время, секунды')
    pylab.plot(x1_list, time_simple1, 'r--', label='Полный перебор')
    pylab.plot(x1_list, time_bin1, color='yellow', label='Бинарный поиск')
    pylab.plot(x1_list, time_combined1, 'b-.', label='Комбинированный')
    pylab.legend(loc='upper left')
    pylab.show()

    print("\nПолный перебор ")
    print(f"Максимальное время = {max(time_simple):6f}", )
    print(f"Минимальное время = {min(time_simple):6f}", )
    print(f"Среднее время = {sum(time_simple) / len(time_simple):6f}")

    print("\nБинарный поиск ")
    print(f"Максимальное время = {max(time_bin):6f}")
    print(f"Минимальное время = {min(time_bin):6f}")
    print(f"Среднее время = {sum(time_bin) / len(time_bin):6f}")

    print("\nКомбинированный алгоритм ")
    print(f"Максимальное время = {max(time_combined):6f}")
    print(f"Минимальное время = {min(time_combined):6f}")
    print(f"Среднее время = {sum(time_combined) / len(time_combined):6f}")
#
# def test_simple_searcher(searcher: search.SimpleSearcher, _dict: dict[str, str]):
#     time_simple = []
#
#     x_list = [i for i in range(len(_dict.keys()))]
#     for d in list(_dict.keys()):
#         time_simple.append(get_time_search(searcher, d))
#
#     pylab.xlabel('Индекс ключа')
#     pylab.ylabel('Количество сравнений')
#     pylab.plot(x_list, time_simple, 'r--', label='Полный перебор')
#     pylab.legend(loc='upper left')
#     pylab.show()

if __name__ == "__main__":
    phones_dict = read_data()
    phones_sorted = sort(phones_dict)

    simple_searcher = search.SimpleSearcher(phones_dict)
    binary_searcher = search.BinarySearcher(phones_sorted)
    combined_searcher = search.CombinedSearcher(phones_dict)

    key = input("Введите ключ: ")

    print("Результат работы алгоритма полного перебора: ")
    t = simple_searcher.search(key)
    if not t:
        print("Ключ не найден")
    else:
        print(t)

    print("Результат работы алгоритма бинарного поиска: ")
    t = binary_searcher.search(key)
    if not t:
        print("Ключ не найден")
    else:
        print(t)

    print("Результат работы комбинированного алгоритма: ")
    t = combined_searcher.search(key)
    if not t:
        print("Ключ не найден")
    else:
        print(t)

    test_time(phones_dict, phones_sorted, simple_searcher, binary_searcher, combined_searcher)
