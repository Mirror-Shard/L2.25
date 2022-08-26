#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import math

"""
Для своего индивидуального задания лабораторной работы 2.23
нужно реализовать вычисление значений в двух функций в отдельных процессах.
"""


# Находим контрольное значение
def control_x(x=0.5):
    return (math.exp(x) + math.exp(-x)) / 2


def control_y(x=math.pi/2):
    return math.pi / 4


def function_1(x):
    CONST_ABSOLUTE = 1e-07
    s = 0
    n = 0
    curr = 0
    while True:
        pre = math.pow(x, 2*n) / math.factorial(2*n)
        n += 1
        if abs(curr - pre) < CONST_ABSOLUTE:
            break
        curr = math.pow(x, 2*n) / math.factorial(2*n)
        s += curr
    return s


def function_2(x):
    CONST_ABSOLUTE = 1e-07
    s = 0
    n = 0
    curr = 0
    while True:
        previous = math.sin(2*n - 1) / 2*n - 1
        n += 1
        if abs(curr - previous) < CONST_ABSOLUTE:
            break
        curr = math.sin(2*n - 1) / 2*n - 1
        s += curr
    return s


def compare(first, second, x):
    result = first(x) - second(x)
    print(f"Результат сравнения: {result}")


if __name__ == '__main__':
    th1 = Process(target=compare(function_1, control_x, 0.5))
    th2 = Process(target=compare(function_2, control_y, math.pi/2))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
