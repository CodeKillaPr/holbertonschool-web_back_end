#!/usr/bin/env python3

import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns task_wait_random n times with
    the specified max_delay.

    Args:
            n (int): The number of times to spawn task_wait_random.
            max_delay (int): The maximum delay for each task_wait_random.

    Returns:
            List[float]: The list of delays in ascending order.
    """
    # Create a list to store the tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Execute tasks concurrently using asyncio.gather
    delays = await asyncio.gather(*tasks)

    # Return the list of delays in ascending order
    return sorted(delays)
