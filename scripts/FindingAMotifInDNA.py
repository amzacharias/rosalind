# This program is for /rosalind.info/problems/subs/

# This program will output the starting point(s) at which a substring
# matches another string.

# Amanda Zacharias; July 26th, 2022

"""
Given two strings s and t, t is a substring of s if t is contained as a
contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found
 to its left, including itself (e.g., the positions of all occurrences of
  'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at
   position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent
 the starting and ending positions of the substring in s; for example,
  if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j;
note that t will have multiple locations in s if it occurs more than
 once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""
# Import modules
import pandas as pd
import os


def read_rosalind_file(filename):
	# This function reads in the file
	# Input: a filename (string)
	# Output: A string
	dirname = os.path.dirname(os.getcwd())
	file = open(os.path.join(dirname, "input", filename), "r")
	file_ls = file.read().split()
	return {"s": file_ls[0], "t": file_ls[1]}


def find_matches(seqs_dict):
	# This function finds indexes of where substring (t) matches string(s).
	# Input: a dictionary
	# Output: A list of integers
	matches = []
	window_size = len(seqs_dict["t"])
	for i in range(0, len(seqs_dict["s"]) - 1):
		if seqs_dict["s"][i:window_size + i] == seqs_dict["t"]:
			# Add one because rosalind doesn't use 0 indexing
			matches.append(i + 1)

	return matches


def main():
	# This is the main function.
	# Input: Nothing
	# Output: Nothing
	# Read in files
	seqs = read_rosalind_file("rosalind_subs.txt")
	print(seqs)
	str_matches = find_matches(seqs)
	print(*str_matches)

main()
