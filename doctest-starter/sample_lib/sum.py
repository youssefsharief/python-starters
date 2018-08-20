"""
This is the "sample_lib" module.

The example module supplies one function, sum().  For example,

>>> sum_fn(5,7)
12
"""

def sum_fn(x,y):
    """Return the sum of 2 integers

    >>> sum_fn(1,2)
    3
    >>> sum_fn(1,"d")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x+y
