import time
from multiprocessing import Process, Manager, freeze_support
import random
# import numpy as np/
import matplotlib.pyplot as plt
import numpy as np


class Matrix:
    mult: int = 0
    size: int = 0
    matrix: list[float][float] = []

    def __init__(self, size, mult=1, matrix=None):
        self.mult = mult
        self.size = size
        if matrix is not None:
            self.matrix = matrix
        else:
            self.matrix = [[0 for _ in range(self.size)] * self.size]

    def __str__(self):
        return f'size = {self.size}, mul = {self.mult}, matrix = {self.matrix}'

    def randomize(self):
        self.matrix = []
        self.mult = 1

        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                self.matrix[-1].append(random.randint(-1000, 1000))

        print(f'Generated matrix  {self.matrix}')
        return self


def calculateDet(m: Matrix):
    s = 0
    if m.size == 2:
        s = (m.matrix[0][0] * m.matrix[1][1] - m.matrix[0][1] * m.matrix[1][0]) * m.mult
    else:
        for i in range(m.size):
            mul = m.matrix[0][i] * m.mult
            if i % 2 == 1:
                mul *= -1

            size = m.size - 1
            matrix = []

            for j in range(1, m.size):
                matrix.append([])
                for k in range(m.size):
                    if k != i:
                        matrix[-1].append(m.matrix[j][k])

            s += calculateDet(Matrix(size, mul, matrix))
    return s


def calculateDetThreading(matrixes, returnList: list):
    s = 0
    for m in matrixes:
        s += calculateDet(m)

    returnList.append(s)


class Solver:
    def __init__(self, size: int = 0, matrix: Matrix = None):
        self.m: Matrix = matrix
        if size == 0: size = 9
        if self.m is None:
            self.m = Matrix(size).randomize()
        self.threadCount = 1
        self.threadManager = Manager()
        self.returnList = self.threadManager.list()

    def solve(self):
        activeThreads = []
        allMatrixes = []
        matrixPerThread = self.m.size / self.threadCount

        for i in range(self.m.size):
            mul = self.m.matrix[0][i] * self.m.mult
            if i % 2 == 1:
                mul *= -1
            size = self.m.size - 1
            matrix = []
            for j in range(1, self.m.size):
                matrix.append([])
                for k in range(self.m.size):
                    if k != i:
                        matrix[-1].append(self.m.matrix[j][k])
            allMatrixes.append(Matrix(size, mul, matrix))

        startIndex = 0
        threadTasksCount = []

        for i in range(self.threadCount):
            endIndex = round(matrixPerThread * (i + 1))
            if i == self.threadCount - 1:  # последний thread
                threadMatrixes = allMatrixes[startIndex:]
            else:
                threadMatrixes = allMatrixes[startIndex:endIndex]

            startIndex = endIndex
            activeThreads.append(
                Process(target=calculateDetThreading, args=(threadMatrixes, self.returnList,)))
            threadTasksCount.append(len(threadMatrixes))

        for thread in activeThreads:
            thread.start()

        for thread in activeThreads:
            thread.join()

        result = sum(self.returnList)
        self.returnList = self.threadManager.list()

        return result


def inputMatrix():
    try:
        print("Input square matrix size (one int digit): ", end="")
        size1 = int(input())
        mat1 = np.zeros((size1, size1), dtype=float)

        print("Input matrix: ")
        for i in range(size1):
            line = [float(num) for num in input().split(" ")]
            if len(line) != size1:
                raise ValueError
            for j in range(size1):
                mat1[i][j] = line[j]
    except ValueError:
        raise Exception("Wrong input!")

    return Matrix(matrix=mat1.tolist(), size=size1)


def ui():
    print(f'Type anything for input size, press enter for input matrix: ')
    a = input()

    if a != '':
        print(f'Input matrix size: ', end='')
        size = int(input())
        a = Solver(size=size)
    else:
        a = Solver(matrix=inputMatrix())

    t = time.time()
    print('True det', calculateDet(a.m))
    print(f'No threads, time = {time.time() - t}')

    threadCount = 1
    while threadCount <= 8:
        a.threadCount = threadCount
        t = time.time()
        res = a.solve()
        print(f'Threads {threadCount}, time = {time.time() - t}, result = {res}')
        threadCount *= 2


def tests():
    threadCount = 1
    sizes = []
    minMatrixSize = 8
    maxMatrixSize = 9
    maxThreadsCount = 8
    repeatCount = 8

    for i in range(minMatrixSize, maxMatrixSize + 1):
        sizes.append(i)

    while threadCount <= maxThreadsCount:
        print('threads', threadCount)
        timeResults = []
        a = Solver()
        a.threadCount = threadCount

        for i in range(minMatrixSize, maxMatrixSize + 1):
            t = 0
            for j in range(repeatCount):
                a.m = Matrix(size=i).randomize()

                tt = time.time()
                a.solve()
                t += time.time() - tt
            timeResults.append((t) * 1000 / repeatCount)
        plt.plot(sizes, timeResults, label=f'{threadCount} поток(ов)')
        threadCount *= 2

    plt.legend(loc='upper left')
    plt.xlabel('Размерность')
    plt.ylabel('Время работы (мс)')
    plt.title('Зависимость времени работы от размерности матрицы и количества потоков')
    plt.show()


if __name__ == '__main__':
    freeze_support()
    ui()
    # tests()