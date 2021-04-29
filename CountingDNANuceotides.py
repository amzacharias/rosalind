# This program is for rosalind.info/problems/dna/

# This program will return the # of occurence of each DNA nucleotide (ACGT)
# within a string. 

# Amanda Zacharias; April 29th, 2021

"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
    times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

DNA_file = open("rosalind_dna.txt","r")
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
        
