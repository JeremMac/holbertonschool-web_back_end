#!/usr/bin/env python3

'''
A module that define the asynchrone function wait_random.
'''


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''
    An asynchronous coroutine that takes in an integer argument.

    Takes an integer as argument (default value is 10)

    returns the waiting time of the coroutine.
    '''
    waiting_time = uniform(0, max_delay)
    await asyncio.sleep(waiting_time)
    return(waiting_time)
