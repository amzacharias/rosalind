#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
Script for rosalind.info/problems/maj
Given: A positive integer k≤20, a positive integer n≤104, 
    and k arrays of size n containing positive integers not exceeding 105.
Return: For each array, output an element of this array occurring strictly 
    more than n/2 times if such element exists, and "-1" otherwise.
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
        lst: List of lists containing integers (stored as strings)
    """
    fpath = os.path.join(os.getcwd(), "input", filename)
    with open(fpath, "r") as in_file:
        k, n = [int(x) for x in in_file.readline().strip().split()]
        arr = [line.strip().split() for line in in_file]

    return arr


def find_majority(indiv_lst):
    """Find integer that is in the majority in a list
    
    Args:
        indiv_lst: List of integers stored as strings

    Returns:
        The majority integer or -1 of none exist
    """
    n = len(indiv_lst)
    major_val = ""
    for val in set(indiv_lst):
        val_count = indiv_lst.count(val)
        if val_count > n / 2: 
            major_val = val
    if (len(major_val) == 0):
        return '-1'
    else:
        return major_val


def main():
    """This is the script driver"""
    # 1. Read in dataframe of integers
    arr_data = get_file("rosalind_maj.txt")
    # 2. Get most common integer in each row/lst
    major_values = []
    for x in arr_data:
        major_values.append(find_majority(x))
    major_values_str = " ".join(major_values)
    # 3. Output to console
    print(major_values_str)
    
main()
