#!/usr/bin/env python3
"""
Module with a type-annotated function sum_list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that takes a list of floats as
    an argument and returns their sum.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
