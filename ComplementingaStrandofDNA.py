# This program is for rosalind.info/problems/rna/

# This program will will produce the reverse complement of a DNA string.

# Amanda Zacharias; April 29th, 2021

"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

# Read in the file
DNA_file = open("rosalind_revc.txt","r")
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
