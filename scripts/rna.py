#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This program is for rosalind.info/problems/rna/
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'initiated'
# Imports -----------------------------------------------
import os

# Code -----------------------------------------------
DNA_file = open(os.path.join(os.getcwd(), "input", "rosalind_rna.txt"), "r")
DNA_s = DNA_file.read()

RNA_s = ""
for nt in DNA_s:
    if nt == "T":
        RNA_s += "U"
    else:
        RNA_s += nt

print(RNA_s)
