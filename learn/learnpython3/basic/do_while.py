#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算1+2+3+...+100:
sum = 0
for n in range(1, 101):
    sum = sum + n
print(sum)

# 计算1x2x3x...x100:
acc = 1
for n in range(1, 101):
    acc = acc * n
print(acc)
