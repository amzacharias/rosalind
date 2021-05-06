# This program is for rosalind.info/problems/gc/

# This program will return the ID and GC content of the DNA string with the
# highest GC content. 

# Amanda Zacharias; May 4th, 2021

"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
"""

# Read in the file
fasta_dict = {}
gc_file = open("rosalind_gc.txt")
for line in gc_file:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        fasta_ID = line[1:]
        if fasta_ID not in fasta_dict:
            fasta_dict[fasta_ID] = []
    sequence = line
    fasta_dict[fasta_ID] = sequence
    
# Function will calculate GC Content
# Input:  sequence list
# Output: an integer
def GC_content(sequence):
    G_count = sequence.count("G")
    C_count = sequence.count("C")
    Total_count = len(sequence)
    GC_Sum = int(G_count) + int(C_count)
    Decimal_GC = float(GC_Sum) / Total_count
    Percent_GC = (Decimal_GC) * 100
    return Percent_GC

# Key: sequence ID, Value: % GC content
GC_dict = {}
for fasta_ID, sequence in fasta_dict.items():
    GC_dict[fasta_ID] = float(GC_content(sequence))
    
# Function will find the sequence and ID with the highest GC content.
# Input: dictionary (key = ID, value = GC content)
# Output: returns the highest GC content
def max_GC(GC_dict):
    max_GC = ["fasta_ID", 0000]
    for fasta_ID, GC_content in GC_dict.items():
        if GC_content > max_GC[1]:
            max_GC = [fasta_ID, GC_content]
        else:
            max_GC = max_GC
    return max_GC

# Call max_GC to find the sequence with the highest GC content and its respective
# ID.
max_GC_pair = max_GC(GC_dict)
print(str(max_GC_pair[0]) + " " + str(max_GC_pair[1]) + "%")




