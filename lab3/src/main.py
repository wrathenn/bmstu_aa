import numpy as np
from matplotlib import pyplot as plt

from ShakerSort import ShakerSort
from ShellSort import ShellSort
from SelectionSort import SelectionSort
from resource import getrusage, RUSAGE_SELF
from random import randint
from copy import deepcopy


cnts = 100


def get_time(sort, length, sorting, print_data=True):
    timer = 0.

    for _ in range(cnts):
        array = get_random_array(length, sorting)
        arr = deepcopy(array)
        # l_time = clock_gettime(CLOCK_PROCESS_CPUTIME_ID)

        l_time = getrusage(RUSAGE_SELF)
        sort.sort(arr, length)
        l_time2 = getrusage(RUSAGE_SELF)
        l_time = (l_time2[0] - l_time[0]) + (l_time2[1] - l_time[1])

        # l_time = clock_gettime(CLOCK_PROCESS_CPUTIME_ID) - l_time
        timer += l_time * 10000000
    timer /= cnts

    if print_data:
        print(sort)
        print("CPU time: ", int(timer), " mks")
        print("Result: ", sort.sort(deepcopy(array)))

    return round(timer)


def get_random_array(length, sorting):
    arr = np.random.randint(-length*10, length * 10, length)

    if sorting == 1:
        arr = np.array(sorted(arr))
    elif sorting == 2:
        arr = np.array(sorted(arr, reverse=True))

    return arr


algorithms = []
algorithms.append(ShakerSort())
algorithms.append(SelectionSort())
algorithms.append(ShellSort())

try:
    print("Введите массив: ", end="")
    arr = np.array([float(elem) for elem in input().split(" ")])

    print("Сортируемый массив: ", arr)
    for sort in algorithms:
        get_time(sort, arr)
except ValueError:
    print("Некорректный ввод")
