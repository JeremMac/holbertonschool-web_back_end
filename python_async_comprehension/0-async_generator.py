#!/usr/bin/env python3


'''
A module that defines the async_generator async function.
'''


import asyncio
import random


async def async_generator():
    '''
    A function that loops ten times asynchronously
    waits for one second then yield  random
    number between 0 and 10.
    '''
    i = 0
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1
