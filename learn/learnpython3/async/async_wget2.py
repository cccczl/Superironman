#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

async def hello():
    print(f'Hello world! ({threading.currentThread()})')
    await asyncio.sleep(1)
    print(f'Hello again! ({threading.currentThread()})')

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
