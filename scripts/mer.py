#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
Script for rosalind.info/problems/mer
Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, 
    a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.  
Return: A sorted array C[1..n+m] containing all the elements of A and B.
Hint: The very first element of C is either A[1] or B[1] , whichever is smaller.
     The rest of can then be constructed recursively
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/12'
__version__ = '1.0'
__status__ = 'completed'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
def get_file(filename):
    """Read in the text file from Rosalind.
    
    Args: 
        filename (str): The name of the input file including extension
        
    Returns: 
        list: A list of sorted integers
        list: A list of sorted integers
    """
    fpath = os.path.join(os.getcwd(), "input", filename)
    with open(fpath, "r") as in_file:
        num1, lst1, num2, lst2 = [in_file.readline().strip() for repeat in range(0,4)]
        lst1 = [int(x) for x in lst1.strip().split()]
        lst2 = [int(x) for x in lst2.strip().split()]
    return lst1, lst2


def execute_sortmerge(lst1, lst2, merged_lst):
    """This function merges two lists of sorted integers, retaining the sorting.
    
    Uses recursion. 
    Needs high recursion limit with large lists (sys.setrecursionlimit(1500))

    Args: 
        lst1: First sorted list
        lst2: Second sorted list
        merged_lst: Instantiated list with merged lst1 and lst2

    Returns: 
        lst: A sorted combination of lst1 and lst2
    """
    # Base case: lst1 and lst2 are empty
    if (len(lst1) == 0) & (len(lst2) == 0):
        return merged_lst
    # Base case: one of the lists is empty, so add the rest of other list
    elif (len(lst1) >= 1) & (len(lst2) == 0):
        merged_lst.extend(lst1)
        lst1.clear()
        return merged_lst
    elif (len(lst1) == 0) & (len(lst2) >= 1):
        merged_lst.extend(lst2)
        lst2.clear()
        return merged_lst
    # Otherwise, find smallest value in lsts and add to merged
    else: 
    # elif (len(lst1) >= 1) & (len(lst2) >= 1):
        if lst1[0] < lst2[0]:
            # Are all values in lst1 < lst2[0]?
            if all(x < lst2[0] for x in lst1):
                merged_lst.extend(lst1)
                lst1.clear()
                return execute_sortmerge(lst1, lst2, merged_lst)
            else:
                # Find largest range of values smaller than lst2[0]
                for idx in range(0, len(lst1)):
                    if lst1[idx] >= lst2[0]:
                        merged_lst.extend(lst1[0:idx])
                        lst1 = lst1[idx: ]
                        return execute_sortmerge(lst1, lst2, merged_lst)
        elif lst2[0] < lst1[0]:
            # Are all values in lst2 < lst1[0]?
            if all(x < lst1[0] for x in lst2):
                merged_lst.extend(lst2)
                lst2.clear()
                return execute_sortmerge(lst1, lst2, merged_lst)
            # Find largest range of values smaller than lst1[0]
            for idx in range(0, len(lst2)):
                if lst2[idx] >= lst1[0]:
                    merged_lst.extend(lst2[0:idx])
                    lst2 = lst2[idx: ]
                    return execute_sortmerge(lst1, lst2, merged_lst)
        elif lst1[0] == lst2[0]:
            [merged_lst.append(l) for l in (lst1.pop(0),lst2.pop(0))]
            return execute_sortmerge(lst1, lst2, merged_lst)
    

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
    """This is the main driver of the script."""
    # 1. Read in data
    in_lst1, in_lst2 = get_file("rosalind_mer.txt")
    print(len(in_lst1) + len(in_lst2))
    # 2. Initialize final list
    c_lst = [min(in_lst1[0], in_lst2[0])]
    if c_lst[0] in in_lst1:
        in_lst1.remove(c_lst[0])
    elif c_lst[0] in in_lst2:
        in_lst2.remove(c_lst[0])
    # 3. Execute merge sort
    c_lst_full = execute_sortmerge(in_lst1, in_lst2, c_lst)
    print(len(c_lst_full))
    # 4. Save
    write_results(c_lst_full, "rosalind_mer.txt")

main()
