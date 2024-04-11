#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/hamm/
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
Hamming distance = the number of nucleotides that differ between two sequences
of equal length. 
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
# Read in the file
DNA_file = open(os.path.join(os.getcwd(), "input", "rosalind_hamm.txt"), "r")
DNA_s = DNA_file.read()
DNA_ls = DNA_s.split()
seq1 = DNA_ls[0]
seq2 = DNA_ls[1]

def calc_hamming_dist (seq1, seq2):
    # This function will count the number of point mutations in the two sequences.
    # In other words, it will calculate the Hamming distance.
    # This function only searches the length of seq1; hence, assuming seq1 and seq2 are the same length.
    # Input: seq1 (string), seq2 (string)
    # Output: Returns hamming distance between seq1 and seq2 (integer)
    count = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
        else:
            continue
    return count

# Calls the function, calc_hamming_dist(), function to calculate the
# Hamming distance. Prints the final result.
print(calc_hamming_dist(seq1,seq2))
