#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for /rosalind.info/problems/prot/
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Imports -----------------------------------------------
import os
import pandas as pd

# Code -----------------------------------------------
def read_rosalind_file(filename):
	"""This function reads in a file.

	Args:
		filename (str): A filename 

	Returns: 
		str: The data in the file
	"""
	# This function reads in the file
	# Input: a filename (string)
	# Output: A string
	filepath = os.path.join(os.getcwd(), "input", filename)
	with open(filepath, 'r') as file:
		data = file.read().strip()
	return data


def read_table(filename):
	"""This function reads in a codon table.

	Args:
		filename (str): A filename 

	Returns: 
		DataFrame: The codon table as a pandas dataframe
	"""
	filepath = os.path.join(os.getcwd(), "input", filename)
	table = pd.read_table(filepath,
						  header=None,
						  names=["RNA", "AA"],
						  delimiter=" ",
						  dtype={"RNA": str, "AA": str},)

	return table


def convert(input_seq, table):
	"""Converst an RNA sequence to an amino acid sequence.
	
	Args: 
		input_seq (str): The input RNA sequence
		table (DataFrame): The codon table

	Returns: 
		str: The converted amino acid sequence
	"""
	converted_seq = ""
	for idx in range(0, len(input_seq), 3):
		str_subset = input_seq[idx:idx+3]
		print(str_subset)
		match_idx = table.index[table["RNA"] == str_subset][0]
		aa = table.iat[match_idx, 1]
		if aa != "Stop":
			converted_seq += aa
	return converted_seq


def main():
	"""This is the main function."""
	# Read in files
	rna_seq = read_rosalind_file("rosalind_prot.txt")
	codon_table = read_table("codon_table.txt")
	# Convert RNA to amino acid
	protein_seq = convert(rna_seq, codon_table)
	print(protein_seq)
	# Save results
	filepath = os.path.join(os.getcwd(), "output", "rosalind_prot_out.txt")
	text_file = open(filepath, "wt")
	n = text_file.write(protein_seq)
	text_file.close()

main()
