#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/dna/
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of
    times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
DNA_file = open(os.path.join(os.getcwd(), "input", "rosalind_dna.txt"), "r")
DNA_s = DNA_file.read()

print(DNA_s)
print(len(DNA_s))

counts = {"A":0, "C":0, "G":0, "T":0}
for nt in DNA_s:
    if nt == "A":
        counts["A"] = counts["A"] + 1
    if nt == "C":
        counts["C"] = counts["C"] + 1
    if nt == "G":
        counts["G"] = counts["G"] + 1
    if nt == "T":
        counts["T"] = counts["T"] + 1

print(counts["A"], counts["C"], counts["G"], counts["T"])
        
