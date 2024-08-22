#!/usr/bin/env python3
"""Runtime Measurement Module"""


import asyncio
from typing import List
from time import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Coroatine that measures the total runtime for
    executing async_comprehension four times in parallel.
    """
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    
    total_runtime = time() - start_time
    
    return total_runtime
async def main():
    """Async function to demonstrate the usage of
    measure_runtime
    """
    return await measure_runtime()


if __name__ == "__main__":
    print(asyncio.run(main()))