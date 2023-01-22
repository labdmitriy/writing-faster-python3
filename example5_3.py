# example5.py
import numpy  # pip install numpy


def compute_sum_of_powers():
    return numpy.sum(numpy.arange(1_000_001) ** 2)

total = compute_sum_of_powers()
# print(total)
