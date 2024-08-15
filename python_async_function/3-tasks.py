#!/usr/bin/env python3
""" Module with a function using asyncio.Task. """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
""" Import the wait_random coroutine from 0-basic_async_syntax. """


async def task_wait_random(max_delay: int) -> float:
    """ Asynchronous coroutine that takes in an integer argument
    waits for a random delay between 0 and max_delay. """
    return await wait_random(max_delay)
