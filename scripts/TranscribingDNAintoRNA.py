# This program is for rosalind.info/problems/rna/

# This program will transcribe a DNA string to an RNA string.

# Amanda Zacharias; April 29th, 2021

"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""
import os

dirname = os.path.dirname(os.getcwd())
DNA_file = open(os.path.join(dirname, "input", "rosalind_rna.txt"), "r")
DNA_s = DNA_file.read()

RNA_s = ""
for nt in DNA_s:
    if nt == "T":
        RNA_s += "U"
    else:
        RNA_s += nt

print(RNA_s)
