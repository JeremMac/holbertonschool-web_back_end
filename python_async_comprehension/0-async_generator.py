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
    while i < 10:
        await asyncio.sleep(1)
        rand_num = random.uniform(0, 10)
        yield rand_num
        i += 1
