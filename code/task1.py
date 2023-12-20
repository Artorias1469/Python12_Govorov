#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

@lru_cache(maxsize=None)
def fib_recursive_cached(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)

@lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive_cached(n - 1)

def main():
    n = 10

    print("Факториал итеративно:", timeit.timeit(lambda: factorial_iterative(n), number=10000))
    print("Факториал итеративно:", timeit.timeit(lambda: fib_iterative(n), number=10000))

    print("Факториал рекурсивно:", timeit.timeit(lambda: factorial_recursive(n), number=100))
    print("Факториал рекурсивно:", timeit.timeit(lambda: fib_recursive(n), number=100))

    print("Факториал рекурсивно (с кэшированием):", timeit.timeit(lambda: factorial_recursive_cached(n), number=100))
    print("Факториал рекурсивно (с кэшированием):", timeit.timeit(lambda: fib_recursive_cached(n), number=100))

if __name__ == "__main__":
    main()
