#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait_random n times with the specified max_delay."""
    x = uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
