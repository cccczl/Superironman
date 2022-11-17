#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading

# 新线程执行的代码:
def loop():
    print(f'thread {threading.current_thread().name} is running...')
    for n in range(1, 6):
        print(f'thread {threading.current_thread().name} >>> {n}')
        time.sleep(1)
    print(f'thread {threading.current_thread().name} ended.')

print(f'thread {threading.current_thread().name} is running...')
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print(f'thread {threading.current_thread().name} ended.')
