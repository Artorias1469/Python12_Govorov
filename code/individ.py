#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_subsets(current_set, remaining_elements):
    if not remaining_elements:
        print(current_set)
        return

    print_subsets(current_set + [remaining_elements[0]], remaining_elements[1:])
    print_subsets(current_set, remaining_elements[1:])

if __name__ == "__main__":
    input_set = input("Введите элементы множества через пробел: ")
    user_set = list(map(int, input_set.split()))

    print_subsets([], user_set)
