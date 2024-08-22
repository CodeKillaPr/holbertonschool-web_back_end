#!/usr/bin/env python3
"""Async Generator Module"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async Generator that yields random numbers
    between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    """Async function to demonstrate the usage
    of async generator"""
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)


if __name__ == "__main__":
    asyncio.run(print_yielded_values())
