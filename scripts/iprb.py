#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for /rosalind.info/problems/iprb/
Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms:
	k individuals are homozygous dominant for a factor,
	m are heterozygous,
	and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms
will produce an individual possessing a dominant allele
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
def read_file(filename):
	# This function reads in the file
	# Input: a filename (string)
	# Output: A dictionary of population information.
	# 	key = organism type, value = number of organisms (int)
	file = open(os.path.join(os.getcwd(), "input", filename), "r")
	file_s = file.read()
	file_ls = file_s.split()
	k = int(file_ls[0])
	m = int(file_ls[1])
	n = int(file_ls[2])
	# total = k + m + n
	return {"AA": k, "Aa": m, "aa": n}


def dominant_prob(pop_dict):
	# Total number of organisms
	total = sum(pop_dict.values())
	# Probability of parental combinations
	# Would be more elegant to calculate probability of recessive subtracted by 1
	probability_AAxAA = (pop_dict["AA"] / total) * ((pop_dict["AA"] - 1) / (total - 1))
	probability_AAxAa = (pop_dict["AA"] / total) * ((pop_dict["Aa"]) / (total - 1)) + \
						(pop_dict["Aa"] / total) * ((pop_dict["AA"]) / (total - 1))
	probability_AAxaa = (pop_dict["AA"] / total) * ((pop_dict["aa"]) / (total - 1)) + \
						(pop_dict["aa"] / total) * ((pop_dict["AA"]) / (total - 1))
	probability_AaxAa = (pop_dict["Aa"] / total) * ((pop_dict["Aa"] - 1) / (total - 1))
	probability_Aaxaa = (pop_dict["Aa"] / total) * ((pop_dict["aa"]) / (total - 1)) + \
						(pop_dict["aa"] / total) * ((pop_dict["Aa"]) / (total - 1))
	# Probability of dominant allele
	probability_A_allele = probability_AAxAA + probability_AAxAa + \
						   probability_AAxaa + \
						   (probability_AaxAa * 0.75) + \
						   (probability_Aaxaa * 0.50)
	return probability_A_allele


def main():
	# This is the driver function
	# Input: nothing
	# Output: nothing
	pop_demo = read_file("rosalind_iprb.txt")
	print(pop_demo)
	dom_prob = dominant_prob(pop_demo)
	print("{:.5f}".format(dom_prob))

main()
