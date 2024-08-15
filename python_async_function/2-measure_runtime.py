#!/usr/bin/env python3
"""
Module with a function to measure the runtime of wait_n.
"""


import time
from typing import List
from asyncio import run
from random import uniform
from time import time as current_time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each wait_n.

    Returns:
        float: The average execution time per call to wait_n.
    """
    start_time = current_time()  # Record the start time

    # Use asyncio.run to execute wait_n and measure total execution time
    run(wait_n(n, max_delay))

    end_time = current_time()  # Record the end time

    # Calculate the total execution time and return the average
    total_time = end_time - start_time
    return total_time / n


# Test the measure_time function
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
