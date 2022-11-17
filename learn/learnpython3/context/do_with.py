#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

@contextmanager
def log(name):
    print(f'[{name}] start...')
    yield
    print(f'[{name}] end.')

with log('DEBUG'):
    print('Hello, world!')
    print('Hello, Python!')
