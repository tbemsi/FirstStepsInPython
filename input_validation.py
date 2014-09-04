__author__ = 'bemsibom'

from math import *
from numbers import Number
import types
import functools

def dim_validate_number(dim):
    """
    Test if dim is a Number .

    >>> dim_validate(5)
    True

    >>> dim_validate("a")
    False

    >>> dim_validate("a string")
    False
    """
    return isinstance(dim, Number)


def dim_validate_positive(dim):
    """
    Test if a dim is positive
    :param dim: dimension
    :return: True or false

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False
    """
    return dim >= 0


def dim_validate_argument(dim1):
    """
    Test for the presence of all arguments
    :param dim1:
    :param dim2:
    :return:

    >>> dim_validate(5)
    True

    >>> dim_validate(5)
    True

    >>> dim_validate(None)
    False

    >>> dim_validate(,5)
    False
    """
    if dim1 is not None:
        return True

def dim_validate_float(dim):
    """
    Test if dim is a floating point integer .

    >>> dim_validate(5)
    True

    >>> dim_validate("a")
    False

    >>> dim_validate(pi)
    False
    """
    return isinstance(dim, float)


def dim_validate_int_float(dim):
    """
    Test if dim is a floating point integer .

    >>> dim_validate(5)
    True

    >>> dim_validate("a")
    False

    >>> dim_validate(pi)
    False
    """
    return isinstance(dim, float) or isintance(dim, int)


def validate_function(f: callable):
    """
    Tests if f is a function

    """
    return isinstance(f, (types.FunctionType, types.BuiltinFunctionType, functools.partial))