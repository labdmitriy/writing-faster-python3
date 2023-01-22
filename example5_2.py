# example5.py
import numpy  # pip install numpy


def compute_sum_of_powers():
    numbers = numpy.arange(1_000_001) ** 2
    return numpy.sum(numbers)

total = compute_sum_of_powers()
# print(total)
