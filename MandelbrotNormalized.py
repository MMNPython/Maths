#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:52:21 2020

@author: mmn
"""

from math import log, log2

MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER
    
    return n + 1 - log(log2(abs(z)))