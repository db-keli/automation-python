#!/usr/bin/env python3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line + 