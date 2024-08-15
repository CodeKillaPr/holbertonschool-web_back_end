#!/usr/bin/env python3
"""
Module with a regular function for creating an asyncio.Task.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        Any: An asyncio.Task for wait_random with the specified max_delay.
    """
    # Create a task for wait_random with the given max_delay
    task = asyncio.create_task(wait_random(max_delay))
    return task


# Test the task_wait_random function
if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
