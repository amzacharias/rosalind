#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/ini2/
This program will calculate the square of the hypotenuse of the right triangle, 
whose legs have lengths a and b. a and b are positive integers, < 1000.
Formula for triangle hypotensue: c = sqrt(a**2 + b**2)
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'finished'
# Code -----------------------------------------------
a = 842
b = 985
c = (a**2) + (985**2)
# Since we want the square of something that is having its square root taken,
# these two will negate and we can skip those two steps. 
print(c)
