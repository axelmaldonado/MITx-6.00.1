#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:20:07 2018

@author: axel
"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    result = 0.0
    if base > num:
        return 0
    elif base == num:
        return 1
    else:
        for x in range(1,int(num)):
            if abs(base**x - num) <= abs(base**(x+1)-num):
                result = x
                break
    return result

print(closest_power(16,136.0))