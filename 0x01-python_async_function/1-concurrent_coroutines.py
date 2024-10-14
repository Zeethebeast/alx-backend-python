#!/usr/bin/env python3
"""Import wait_random from the previous python file"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n concurrence"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    result = await asyncio.gather(*tasks)
    result = sorted(result, key=float)
    """You will spawn wait_random n times with the specified max_delay."""
    return result
