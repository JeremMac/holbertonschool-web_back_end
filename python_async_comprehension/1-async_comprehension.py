#!/usr/bin/env python3


'''
A module that define async_comprehension async function.
'''


import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''
    Coroutine will collect 10 random numbers using an
    async comprehensing over async_generator.

    Returns the 10 random number generated
    by async_generator function.
    '''
    random_numbers = [i async for i in async_generator()][:10]
    return random_numbers
