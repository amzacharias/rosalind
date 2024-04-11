#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/cons/
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. 
    (If several possible consensus strings exist, then you may return any one of them.)
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'done'
# Imports -----------------------------------------------
import os
import pandas as pd
import numpy as np

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
    fastq_id = ""
    for line in fa_file:
        line = line.strip()  # remove whitespace
        if not line:
            continue
        if line.startswith(">"):
            fastq_id = line[1:]
            if fastq_id not in fasta_dict:
                fasta_dict[fastq_id] = []
            continue  # This line is important! Ensure whole sequence is captured.
        fasta_dict[fastq_id] += line
    return fasta_dict


def count_nts(seqs_df):
    """Counts the number of times each nucleotide (A,C,G,T) occurs in each column (sample).
    
    Args: 
        seqs_df (DataFrame): Dataframe with nucleotide sequence (rows) of each sample (columns).
    
    Returns: 
        DataFrame: A dataframe with the number of times each nucleotide occurs in each sample.
    """
    # Count for each nucleotide; convert NAs to 0's; make everything an integer; sort nts alphabetically
    counts_df = seqs_df.apply(lambda x: x.value_counts()).replace(np.nan, 0).astype(int).sort_index()
    return counts_df


def get_consensus(cnts_df):
    """Get the most frequent nucleotide at each position in the sequence.
    
    Args: 
        cnts_df (DataFrame): Dataframe with number of times each nucleotide occurs in each position

    Returns: 
        str: The consensus sequence
    """
    max_str = cnts_df.idxmax().str.cat()
    return max_str


def write_results(cons_seq, cnts_df, filename):
    """Save the results to a text file.
    
    Args: 
        cons_seq (str): Consensus sequence
        cnts_df (DataFrame): Number of times each nt occurs in each position
        filename (str): Name of output file

    Returns: 
        Writes a text file to the output directory in this project folder
    """
    out_path = os.path.join(os.getcwd(), "output", filename)
    with open(out_path, "w") as out_file:
        out_file.write(cons_seq)
        out_file.write("\n")
    cnts_df.add_suffix(":", axis="index").to_csv(
        out_path, sep = " ", header=False, mode = "a")


def main(): 
    """This is the main driver of this script"""
    # 1. Read in sequences
    seq_dict = get_fasta_file("rosalind_cons.txt")
    seq_df = pd.DataFrame.from_dict(seq_dict)
    # 2. Transpose dataframe so each column is a position along the sequence
    t_seq_df = seq_df.transpose()
    # 3. Count number of times each nucleotide occurs
    nt_counts_df = count_nts(t_seq_df)
    # 4. Get the consensus string
    consensus_str = get_consensus(nt_counts_df)
    # 5. Save results to a file
    write_results(consensus_str, nt_counts_df, "rosalind_cons_out.txt")

main()
