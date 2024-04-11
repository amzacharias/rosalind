#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for https://rosalind.info/problems/lcsm/
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return a single solution)
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'finished'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
def get_fasta_file(filename):
    """This function reads in a fasta file
    
    Args: 
        filename (str): The filename

    Returns: 
        dict: A dictionary with fasta files; key = ID, value = sequence
    """
    fa_file = open(os.path.join(os.getcwd(), "input", filename), "r")
    fasta_dict = {}
    fasta_id = ""
    for line in fa_file:
        line = line.strip()  # remove whitespace
        if not line:
            continue
        if line.startswith(">"):
            fasta_id = line[1:]
            if fasta_id not in fasta_dict:
                fasta_dict[fasta_id] = "" # empty is str, not lst!
            continue  # This line is important! Ensure whole sequence is captured.
        fasta_dict[fasta_id] += line
    return fasta_dict


def find_motif(seqs):
    """Find the largest motif that is shared across all sequences.
    
    Args: 
        seqs (list): A list of three sequences (strings)

    Returns: 
        A string with the largest pattern of shared nucleotides in a row
    """
    # Get the shortest sequence and remove from remaining list
    srt_seqs = sorted(seqs, key = len)
    shortest_seq = srt_seqs[0]
    other_seqs = srt_seqs[1: ]
    # Instantiate variables for looping
    matching_motifs = []
    for idx in range(0, len(shortest_seq)): 
        for jdx in range(idx, len(shortest_seq) + 1):
            if (idx != jdx):
                cur_motif = shortest_seq[idx:jdx]
                # Is the motif in all the other sequences
                if all(cur_motif in seq for seq in other_seqs):
                    matching_motifs.append(cur_motif)
    # Select the longest motif
    best_motif = max(matching_motifs, key=len)
    return(best_motif)

def main(): 
    """This is the main driver of this script"""
    # 1. Read in sequences
    seq_dict = get_fasta_file("rosalind_lcsm.txt")
    seqs_list = list(seq_dict.values())
    # 2. Find shared motif
    shared_motif = find_motif(seqs_list)
    print(shared_motif)

main()