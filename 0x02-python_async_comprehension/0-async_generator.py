#!/usr/bin/env python3
'''
Write a coroutine called
async_generator that takes no arguments.
'''
from typing import AsyncGenerator
import asyncio
from random import uniform


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    Use the random module.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        i = uniform(0, 10)
        yield i
