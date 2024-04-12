#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This script is for rosalind.info/problems/ins
Given: A positive integer n <= 10^3 and an array A[1..n] of integers.
Return: The number of swaps performed by insertion sort algorithm on A[1..n].
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'finished'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
def get_file(filename):
    """Read in the text file from Rosalind.
    
    Args: 
        filename (str): The name of the input file including extension
        
    Returns: 
        lst: A list of integers to sort
    """
    fpath = os.path.join(os.getcwd(), "input", filename)
    with open(fpath, "r") as in_file:
        num1, raw_lst = [in_file.readline().strip() for repeat in range(0,2)]
        raw_lst = [int(x) for x in raw_lst.strip().split()]
    return raw_lst


def insert_sort(raw_lst):
    """Use an insertion sort algorithm to sort an unordered list of integers.
    
    Args: 
        raw_lst (lst): Integers to be ordered

    Returns: 
        lst: Returns an ordered list
    """
    nswaps = 0
    for idx in range(1, len(raw_lst)):
        curr_value = raw_lst[idx]
        jdx = idx - 1 # get index to the left of the current value
        while jdx >= 0 and curr_value < raw_lst[jdx]: # if current is < value to the left
            raw_lst[jdx + 1] = raw_lst[jdx] # move larger value to the right
            jdx -= 1 # let's look at value further left on next loop
            nswaps += 1
        # once all numbers > curr value are nudged to the right, add curr_value back
        raw_lst[jdx + 1] = curr_value

    return raw_lst, nswaps


def main():
    """This is the main driver of the script"""
    # 1. Read in file
    unordered_lst = get_file("rosalind_ins.txt")
    # 2. Perform sorting
    ordered_lst, nswap = insert_sort(unordered_lst)
    print(nswap)

main()
