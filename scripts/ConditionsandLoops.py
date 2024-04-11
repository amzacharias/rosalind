#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/ini4/
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Code -----------------------------------------------
a = 4537
b = 9210
output = 0

for i in range(a,b+1):
    if i % 2 == 1:
        output = output + i
    else:
        output = output

print(output)
