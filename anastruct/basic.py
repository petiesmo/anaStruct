import numpy as np
import collections
try:
    from anastruct.cython.cbasic import converge, angle_x_axis
except ImportError:
    from anastruct.cython.basic import converge, angle_x_axis


def find_nearest(array, value):
    """
    :param array: (numpy array object)
    :param value: (float) value searched for
    :return: (tuple) nearest value, index
    """
    # Subtract the value of the value's in the array. Make the values absolute.
    # The lowest value is the nearest.
    index = (np.abs(array-value)).argmin()
    return array[index], index


def integrate_array(y, dx):
    """
    integrate array y * dx
    """
    return np.cumsum(y) * dx


class FEMException(Exception):
    def __init__(self, type_, message):
        self.type = type_
        self.message = message


def args_to_lists(*args):
    arg_lists = []
    for arg in args:
        if isinstance(arg, collections.Iterable) and not isinstance(arg, str):
            arg_lists.append(arg)
        else:
            arg_lists.append([arg])
    lengths = list(map(len, arg_lists))
    n = max(lengths)
    if n == 1:
        return arg_lists

    args = []
    for arg, l in zip(arg_lists, lengths):
        if l == n:
            args.append(arg)
        else:
            args.append([arg[0] for _ in range(n)])
    return args