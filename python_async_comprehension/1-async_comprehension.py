#!/usr/bin/env python3
"""Async Comprehension Module"""


import asyncio
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Coroatine that asynchronously
    collect 10 random numbers
    using an async comprehensions.
    """

    result = [i async for i in async_generator()]
    return result

async def main():
    """Async function to demonstrate the usage of
    async_comprehension.
    """
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())
