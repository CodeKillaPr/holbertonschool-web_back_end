#!/usr/bin/env python3
"""
Module with a function element_length annotated with types
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes an iterable object 'lst' and returns a list of tuples.
    Each tuple contains an element from 'lst' and its length.

    Args:
        lst (Iterable[Sequence]): An iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing an element from 'lst'
        and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
