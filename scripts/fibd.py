#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/fibd/
Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after
    the n-th month if all rabbits live for m months.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'inprogress'
# Imports -----------------------------------------------
import os
import numpy as np

# Code -----------------------------------------------
n = 6
k = 1 # doesn't change for this problem
m = 3

def loop_mortal_fib(n_months, k_offspring, m_lifespan):
    """Calculate the total rabbit populations, allowing for limited lifespan.
    
    The total number of rabbits at any time is the number of rabbits from the previous
    generation + the number of rabbits from two generations ago and the children they produce.

    Args: 
        n_months (int): Number of months for mating
        k_offspring (int): Number of offspring produced by each parent pair
        m_lifespan (int): Number of months the rabbits have to live before death

    Returns: 
        int: Estimated number of children produced in total
    """
    rabbits = np.asarray([1, 0])# After two generations, 1 pair is 1 month old, and 1 pair is 0 months old.
    for i in range(3, n_months):
        # Produce children
        rabbits_of_age = rabbits[(rabbits >= 1)]
        rabbits = np.append(rabbits, [0]*(len(rabbits_of_age)*k_offspring))
        print(rabbits)
        # Everyone grows up by 1 month
        rabbits = rabbits + 1
        print(rabbits)
        # Remove old rabbits
        rabbits = rabbits[(rabbits < m_lifespan)]
        print(rabbits)
    return len(rabbits)

print(loop_mortal_fib(n, k,m))
