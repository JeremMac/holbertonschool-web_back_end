#!/usr/bin/env python3


'''
A module that define the async function wait_n.
'''

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    An async routine called wait_n that takes in 2 int arguments.
    '''
    delays = []

    async def wait_and_append_delay():
        '''
        A function that wait and append the delay into
        a list.
        '''
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Create a list to hold the task objects
    tasks = [wait_and_append_delay() for _ in range(n)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    await task_wait_random(max_delay)

    return delays
