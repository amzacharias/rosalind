#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/rna/
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
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
DNA_file = open(os.path.join(os.getcwd(), "input", "rosalind_revc.txt"), "r")
DNA_s = DNA_file.read()

# Step 1: reverse the string
#   Code found on https://www.w3schools.com/python/python_howto_reverse_string.asp
#   [::1] = start at the end of the string & end at position 0.
reverse_DNA = DNA_s[::-1]

# Step 2: take the complements of the nucleotides
# A -> T, C -> G, T -> A, G -> C
rc_DNA = ""
for nt in reverse_DNA:
    if nt == "A":
        rc_DNA += "T"
    if nt == "C":
        rc_DNA += "G"
    if nt == "T":
        rc_DNA += "A"
    if nt == "G": 
       rc_DNA += "C"

print(rc_DNA)
