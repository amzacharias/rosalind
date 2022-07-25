# This program is for /rosalind.info/problems/iprb/

# This program will calculate the probability of a dominate allele
# being produced by two random organisms.

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

# Probablility that chromosome 1 = dominant
# Probability that chromosome 2 = dominant

# Probability of getting two dominants
# Probability of getting 1 dominant and 1 heterozygote
# Probability of getting 2 heterozygotes and at least one donating a dominant
# Probability of getting 1 het and 1 passive, but het passes dominant allele

def read_file(filename):
	# This function reads in the file
	# Input: a filename (string)
	# Output: A dictionary of population information.
	# 	key = organism type, value = number of organisms (int)
	file = open(filename, "r")
	file_s = file.read()
	file_ls = file_s.split()
	k = int(file_ls[0])
	m = int(file_ls[1])
	n = int(file_ls[2])
	total = k + m + n
	return {"AA": k, "Aa": m, "aa": n}


def dominant_prob(pop_dict):
	# Total number of organisms
	total = sum(pop_dict.values())
	# Probability of parental combinations
	# Would be more elegant to calculate probability of recessive subtracted by 1
	AA_AA_probability = (pop_dict["AA"] / total) * ((pop_dict["AA"] - 1) / (total - 1))
	AA_Aa_probability = (pop_dict["AA"] / total) * ((pop_dict["Aa"]) / (total - 1)) + \
						(pop_dict["Aa"] / total) * ((pop_dict["AA"]) / (total - 1))
	AA_aa_probability = (pop_dict["AA"] / total) * ((pop_dict["aa"]) / (total - 1)) + \
						(pop_dict["aa"] / total) * ((pop_dict["AA"]) / (total - 1))
	Aa_Aa_probability = (pop_dict["Aa"] / total) * ((pop_dict["Aa"] - 1) / (total - 1))
	Aa_aa_probability = (pop_dict["Aa"] / total) * ((pop_dict["aa"]) / (total - 1)) + \
						(pop_dict["aa"] / total) * ((pop_dict["Aa"]) / (total - 1))
	# Probability of dominant allele
	A_allele_probability = AA_AA_probability + AA_Aa_probability + \
						   AA_aa_probability + \
						   (Aa_Aa_probability * 0.75) + \
						   (Aa_aa_probability * 0.50)
	return A_allele_probability


def main():
	# This is the driver function
	# Input: nothing
	# Output: nothing
	pop_demo = read_file("rosalind_iprb.txt")
	print(pop_demo)
	dom_prob = dominant_prob(pop_demo)
	print("{:.5f}".format(dom_prob))

main()

