#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This script is for rosalind.info/problems/fibo
Given: A positive integer n≤25.
Return: The value of Fn.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'finished'
# Code -----------------------------------------------
def get_fibo(n):
    """
    Get the fibonacci sequence.

    Args: 
        n (int): The number that the sequence is based on

    Returns: 
        A number.
    """
    # base case n = 0
    if n == 0:
        return 0
    # base case n = 1
    elif n == 1:
        return 1
    elif n >= 2: 
        return get_fibo(n - 1) + get_fibo(n - 2)

get_fibo(20) # 6765
