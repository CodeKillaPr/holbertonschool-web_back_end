#!/usr/bin/env python3
"""
Module with a type-annotated function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as an argument and returns
    a function that multiplies a float by multiplier.

    Args:
        multiplier ([[[float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a
        float and returns the product.
    """
    def multiplier_function(x: float) -> float:
        """
        Inner function that multiplies a float by
        the multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The product of x and the multiplier.
        """
        return x * multiplier

    return multiplier_function
