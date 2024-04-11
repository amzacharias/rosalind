#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/fib/
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
Note: the number of offspring in any month == number of rabbits that were alive
2 months prior.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
"""
Fibonnaci:
Fn = Fn - 1 + Fn - 2
F1 = F2 = 1 to initiate the sequence

Helpful video: https://www.youtube.com/watch?v=3eBIHdyGJLQ
Helpful link: https://github.com/kaniick/Rosalind/blob/
master/Bioinformatics%20Stronghold/Rabbits%20and%20Recurrence%
20Relations%20(FIB)
"""
# Read in the file
fib_file = open(os.path.join(os.getcwd(), "input", "rosalind_fib.txt"), "r")
fib_s = fib_file.read()
fib_ls = fib_s.split()
n = int(fib_ls[0])
k = int(fib_ls[1])

def loop_fib(n_months, k_offspring):
    """Doesn't use recursion to calculate the total rabbit population.
    
    Args: 
        n_months (int): Number of months for mating
        k_offspring (int): Number of offspring produced by each parent pair

    Returns: 
        int: Estimated number of children produced in total
    """
    parent, child = 1, 1
    # months - 1 because the first line of this function accounts for month 1
    for i in range(n_months - 1):
        # old child -> new parent
        # old parent + (old child * k_offspring) -> new child
        child, parent = parent, parent + (child * k_offspring)
    return child

print(loop_fib(n, k))

def rec_fib(n, k):
    """Uses recursion to calculate the total rabbit population.
    
    Args: 
        n_months (int): Number of months for mating
        k_offspring (int): Number of offspring produced by each parent pair

    Returns: 
        int: Estimated number of children produced in total
    """
    # Base case, F1 = 0
    if n == 0:
        return 0
    # Base case, F2 = 1 or F2 = 2
    elif n == 1 or n == 2:
        return 1
    # Fn = Fn - 1 + Fn - 2
    else:
        return rec_fib(n - 1, k) + k * rec_fib(n - 2, k)

print(rec_fib(n,k))

memo = {}
def mem_fib(n, k = 1):
    """Uses recursion to calculate the total rabbit population, with memory optimization.

    Provided by Rosalind explanation; uses memoization to minimize recursion running time.
    Uses a data structure (dictionary) to store results.
    
    Args: 
        n_months (int): Number of months for mating
        k_offspring (int): Number of offspring produced by each parent pair

    Returns: 
        int: Estimated number of children produced in total
    """
    args = (n, k)
    if args in memo:
        return memo[args] # We have computed this before!

    # We haven't computed this before
    if n == 0:
        ans = 0
    elif n == 1 or n == 2:
        return 1
    else:
        ans = mem_fib(n - 1, k) + k * mem_fib(n - 2, k)
    memo[args] = ans # Store the result
    return ans

mem_fib(n, k)

"""
The following is unit testing for Rec_fib(). Includes testing for only regular
cases.
"""

if __name__ == "__main__":
    print("Testing n = 0")
    # Test n = 0
    n = 0
    k = 2
    print(str(rec_fib(n, k)) + " should return 0")
    print("Testing n = 1")
    # Test n = 2
    n = 1
    k = 2
    print(str(rec_fib(n, k)) + " should return 1")
    print("Testing n = 5, k = 3")
    # Test n = 5, k = 3
    n = 5
    k = 3
    print(str(rec_fib(n, k)) + " should return 19")
