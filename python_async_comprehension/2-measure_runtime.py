#!/usr/bin/env python3


'''
A module that defines measure_runtime coroutine.
'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    A measure_runtime coroutine that will
    execute async_comprehension four times
    in parallel using asyncio.gather.

    Returns the total time execution of async_comprehension
    async function.
    '''
    start_time = time.time()
    gather_routine = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*gather_routine)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
