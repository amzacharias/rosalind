# This program is for /rosalind.info/problems/prot/

# This program will convert an RNA sequence to protein sequence.

# Amanda Zacharias; July 25th, 2022

"""
Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms:
	k individuals are homozygous dominant for a factor,
	m are heterozygous,
	and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms
will produce an individual possessing a dominant allele
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""
# Import modules
import pandas as pd

def read_rosalind_file(filename):
	# This function reads in the file
	# Input: a filename (string)
	# Output: A string
	with open(filename, 'r') as file:
		data = file.read().strip()
	return data


def read_table(filename):
	# This function reads in a codon table
    # And formats it nicely
	# Input: a filename (string)
	# Output: a pandas dataframe
	table = pd.read_table(filename,
						  header=None,
						  names=["RNA", "AA"],
						  delimiter=" ",
						  dtype={"RNA": str, "AA": str},)

	return table


def convert(input_seq, table):
	# This function converts an rna sequence to
	# amino acid sequence.
	# Input: a string and pandas dataframe
	# Output: a string
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
	# This is the main function.
	# Input: Nothing
	# Output: Nothing
	# Read in files
	rna_seq = read_rosalind_file("rosalind_prot.txt")
	codon_table = read_table("codon_table.txt")
	# Convert RNA to amino acid
	protein_seq = convert(rna_seq, codon_table)
	print(protein_seq)

	text_file = open("rosalind_prot_out.txt", "wt")
	n = text_file.write(protein_seq)
	text_file.close()

main()
