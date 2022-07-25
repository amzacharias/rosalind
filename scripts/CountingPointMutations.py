# This program is for rosalind.info/problems/hamm/

# This program will calculate the Hamming distance of two sequences

# Amanda Zacharias; May 12th, 2021

"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

"""
Hamming distance = the number of nucleotides that differ between two sequences
of equal length. 
"""

import os

# Read in the file
dirname = os.path.dirname(os.getcwd())
DNA_file = open(os.path.join(dirname, "input", "rosalind_hamm.txt"), "r")
DNA_s = DNA_file.read()
DNA_ls = DNA_s.split()
seq1 = DNA_ls[0]
seq2 = DNA_ls[1]

# This function will count the number of point mutations in the two sequences.
# In other words, it will calculate the Hamming distance.

def calc_HammingDist (seq1, seq2):
    count = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
        else:
            continue
    return count

# Calls the function, calc_HammingDist(), function to calculate the
# Hamming distance. Prints the final result.

print(calc_HammingDist(seq1,seq2))
