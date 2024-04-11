#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This script is for rosalind.info/problems/bins
Given: Two positive integers n≤105 and m≤105 , 
    a sorted array A[1..n] of integers from −105 to 105 and
    a list of m integers −105≤k1,k2,…,km≤105.
Return: For each ki, output an index 1≤j≤ns.t. A[j]=ki or "-1" if there is no such index.

Basically, we don't care about the first two positive integers. 
We just want indexes for where elements in the list of integers occur in the sorted array.

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
        list: A backgeround sorted list to be searched in
        list: A list of numbers to query in the above array.
    """
    fpath = os.path.join(os.getcwd(), "input", filename)
    with open(fpath, "r") as in_file:
        num1, num2, back, query = [in_file.readline().strip() for repeat in range(0,4)]
        back = [int(x) for x in back.strip().split()]
        query = [int(x) for x in query.strip().split()]
    return back, query


def indiv_search_iter(q_int, back):
    """Performs a binary search for one integer in a background set of sorted integers.
    
    Iterative approach rather than recursive.

    Args: 
        q_int (int): Query integer to search for
        back (lst): A sorted list of integers

    Returns: 
        The index of q_int's location in back. If there are no matches, returns -1
    """
    # Instantiate variables
    low = 0
    high = len(back) - 1 # subtract 1 b.c. python is 0 based
    mid = 0
    # Begin loop
    while low <= high:
        mid = (high + low) // 2
        # If query is less than the middle point
        if q_int < back[mid]:
                high = mid - 1
        # If query is greater than middle point
        elif q_int > back[mid]: 
                low = mid + 1
        # If query == middle point
        elif q_int == back[mid]: 
             return mid + 1 # results for rosalind are 1-based, not 0-based
    # If no matches were found, q_int is not in back
    return -1      


def write_results(out_lst, filename):
    """Save the results to a text file.
    
    Args: 
        out_lst (lst): List to save
        filename (str): Name of output file

    Returns: 
        Writes a text file to the output directory in this project folder
    """
    out_str = ' '.join([str(x) for x in out_lst]) # format as str for saving

    out_path = os.path.join(os.getcwd(), "output", filename)
    with open(out_path, "w") as out_file:
        out_file.write(out_str)
    
    
def main():
    """This is the main driver of the script"""
    # 1. Read in file
    back_lst, query_lst = get_file("rosalind_bins.txt")
    # 2. Perform searches
    search_results = [indiv_search_iter(x, back_lst) for x in query_lst]
    # 3. Save results
    write_results(search_results, "rosalind_bins.txt")

main()
