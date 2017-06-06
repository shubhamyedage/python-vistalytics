import numpy as np


def average_change(a):
    dummy_result = [j - i for i, j in zip(a[:-1], a[1:])]
    return get_mean(dummy_result)


def get_change(a, b):
    return round(float(b) - float(a), 2)


def percentage_change(a, b):
    if a == 0:
        return 0
    result = round((b - a) * 100 / a, 2)
    return 0 if abs(result) < 5 else result


def get_std_dev(v):
    v = [x for x in v]
    return round(np.std(v), 2)


def get_mean(v):
    v = [x for x in v]
    return round(np.mean(v), 2)


def merge_list_percentage(list1, list2):
    dummy_list = [round((a * 100/b), 2) for a, b in zip(list1, list2)]
    return dummy_list


def get_linear_function_properties(y_data):
    x_data = np.arange(0, len(y_data))
    z = np.polyfit(x_data, y_data, 1)
    return round(z[0], 2), round(z[1], 2)


def compare(a, b):
    return (a * b) > 0
