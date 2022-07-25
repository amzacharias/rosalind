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

def read_file(filename):
	# This function reads in the file
	# Input: a filename (string)
	# Output: A string
	file = open(filename, "r")
	file_s = file.read()
	file_clean = file_s.strip()
	return {file_clean}

def main():
	# This is the main function.
	# Input: Nothing
	# Output: Nothing
	rna_seq = read_file("rosalind_prot.txt")

main()
