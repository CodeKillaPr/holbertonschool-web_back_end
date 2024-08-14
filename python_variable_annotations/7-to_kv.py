#!/usr/bin/env python3
"""
Module with a type-annotated function to_kv
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a string k and an int OR float v as arguments
    and returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v and
    should be annotated as a float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input value which
        can be either int or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k
        and the square of v as a float.
    """
    return (k, v ** 2.0)
