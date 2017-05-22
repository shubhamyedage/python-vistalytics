import math


def average_change(a):
    dummy_values1 = [0 if math.isnan(x) else x for x in a]
    dummy_values2 = [j - i for i, j in zip(dummy_values1[:-1], dummy_values1[1:])]
    return round(sum(dummy_values2) / len(dummy_values2), 2)


def get_change(a, b):
    return round(b - a, 2)


def percentage_change(a, b):
    return round((b - a) * 100 / a, 2)