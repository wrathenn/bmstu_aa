import time
from multiprocessing import Process, Manager, freeze_support
import random


class Matrix:
    mult = 0
    size = 0
    matrix = []

    def __init__(self, size, mult=None, matrix=None):
        self.mult = mult
        self.size = size
        self.matrix = matrix

    def __str__(self):
        return f'size = {self.size}, mul = {self.mult}, matrix = {self.matrix}'

    def randomize(self):
        self.matrix = []
        self.mult = 1
        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                self.matrix[-1].append(random.randint(-10, 10))
        print(self.matrix)
        return self


def calculateSum(m: Matrix):
    s = 0
    if m.size == 2:
        return (m.matrix[0][0] * m.matrix[1][1] - m.matrix[0][1] * m.matrix[1][0]) * m.mult

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

        s += calculateSum(Matrix(size, mul, matrix))
    return s

def calculateSumThreading(matrixes, returnList: list):
    t = time.time()
    s = 0

    for m in matrixes:
        if m.size == 2:
            returnList.append((m.matrix[0][0] * m.matrix[1][1] - m.matrix[0][1] * m.matrix[1][0]) * m.mult)
            continue

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

            s += calculateSum(Matrix(size, mul, matrix))
            # allMatrixes.append(Matrix(size, mul, matrix))

    returnList.append(s)
    # print(f'process {getpid()}, time {time.time() - t}')

class Solver:
    def __init__(self, matrix: Matrix = None):
        self.m = matrix
        if self.m is None:
            self.m = Matrix(10).randomize()

        self.threadCount = 1
        self.threadManager = Manager()
        self.returnList = self.threadManager.list()


    def solve(self):
        activeThreads = []
        matrixPerThread = self.m.size / self.threadCount
        allMatrixes = []

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

        startMatrix = 0
        threadTasksCount = []

        for i in range(self.threadCount):
            endMatrix = round(matrixPerThread * (i+1))
            # if endMatrix == startMatrix: break
            if i == self.threadCount - 1: #последний
                threadMatrixes = allMatrixes[startMatrix:]
            else:
                threadMatrixes = allMatrixes[startMatrix:endMatrix]
            startMatrix = endMatrix
            activeThreads.append(
                Process(target=calculateSumThreading, args=(threadMatrixes, self.returnList,)))
            threadTasksCount.append(len(threadMatrixes))

        # print(f'threads - {len(activeThreads)}, tasks -', threadTasksCount)
        for thread in activeThreads:
            thread.start()
        for thread in activeThreads:
            thread.join()
        self.returnList = self.threadManager.list()

        return sum(self.returnList)


if __name__ == '__main__':
    freeze_support()

    a = Solver()
    t = time.time()

    print('true det', calculateSum(a.m))
    print(f'Threads 0, time = {time.time() - t}')

    for i in range(1, 8):
        a.threadCount = i
        t = time.time()

        for _ in range(10):
            a.solve()

        print(f'Threads {i}, time = {time.time() - t}')