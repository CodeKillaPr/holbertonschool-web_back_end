#!/usr/bin/env python3
"""
Module with a regular function for creating an asyncio.Task.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Create a asyncio.Task that waits for a random delay.

    Args:
            max_delay (int): The maximum delay for the wait.

    Returns:
            Any: The asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
