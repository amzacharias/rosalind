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

import os

def get_file(filename):
    # This function reads in the fasta file
    # Input: a filename (string)
    # Output: a dictionary (key = ID, value = sequence)
    dirname = os.path.dirname(os.getcwd())
    gc_file = open(os.path.join(dirname, "input", filename), "r")
    fasta_dict = {}
    fastq_id = ""
    for line in gc_file:
        line = line.strip()  # remove whitespace
        if not line:
            continue
        if line.startswith(">"):
            fastq_id = line[1:]
            if fastq_id not in fasta_dict:
                fasta_dict[fastq_id] = []
            continue  # This line is important! Ensure whole sequence is captured.
        fasta_dict[fastq_id] += line
    print(fasta_dict)
    return fasta_dict


def calc_gc_content(fasta_sequence):
    # Calculate GC Content
    # Input:  sequence list
    # Output: an integer
    G_count = fasta_sequence.count("G")
    C_count = fasta_sequence.count("C")
    Total_count = len(fasta_sequence)
    GC_Sum = G_count + C_count
    Decimal_GC = GC_Sum / Total_count
    Percent_GC = Decimal_GC * 100
    return Percent_GC


def get_max_gc(gc_dict):
    # Function will find the sequence and id with the highest gc content.
    # Input: dictionary (key = id, value = gc content)
    # Output: returns the highest gc content
    max_gc = ["fastq_id", 0000]  # instantiate empty list
    for fastq_id, gc_content in gc_dict.items():
        if gc_content > max_gc[1]:
            max_gc = [fastq_id, gc_content]
        else:
            max_gc = max_gc
    return max_gc

def main():
    # The main driver of this script
    # Input: None
    # Output: writes a file and prints messages to the user
    # 1. Read in sequences
    seq_dict = get_file("rosalind_gc.txt")
    # 2. Calculate % GC content of each sequence
    gc_dict = {}
    for fastq_id, sequence in seq_dict.items():
        gc_dict[fastq_id] = calc_gc_content(sequence)
    # 3.Get sequence and with highest GC content and its ID
    max_gc_pair = get_max_gc(gc_dict)
    print("{} \n{:.6f}".format(max_gc_pair[0], max_gc_pair[1]))

main()
# Rosalind_3726
# 54.057018
