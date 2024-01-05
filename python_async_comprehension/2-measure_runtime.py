#!/usr/bin/env python3


'''
A module that defines 
'''


import asyncio, time, typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    gather_routine = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*gather_routine)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
