#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Student object (name: {self.name})'

    __repr__ = __str__

print(Student('Michael'))
