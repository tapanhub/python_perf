#!/usr/bin/env python

"""Measuring Time"""

from time import perf_counter

#@profile
def use_forloop(n):
    sum_ = 0
    for i in range(n):
        sum_ += i
    return sum_

def use_sum(n):
    return sum(range(n))


if __name__ == "__main__":
    n = 1_000_000
    start = perf_counter()
    use_forloop(n)
    for_duration = perf_counter() - start
    start = perf_counter()
    use_sum(n)
    sum_duration = perf_counter() - start
    print(f"for time = {for_duration}")
    print(f"sum time = {sum_duration}")

