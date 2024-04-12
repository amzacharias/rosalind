#!/usr/bin/env python
# -*-coding: utf-8 -*-
"""
Description:
This script is for rosalind.info/problems/deg
Given: A simple graph with n <= 10^3 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the dgree of vertex i.  
"""
__author__ = 'Amanda Zacharias'
__contact__ = '16amz1@queensu.ca'
__date__ = '2024/04/11'
__version__ = '1.0'
__status__ = 'finished'
# Imports -----------------------------------------------
import os
import pandas as pd

# Code -----------------------------------------------
def get_graph_file(filename):
    """Read in the graph file as a pandas dataframe
    
    Args: 
        filename (str): Name of the input file including extension

    Returns: 
        DataFrame: Pandas DataFrame with edge vertices
    """
    fpath = os.path.join(os.getcwd(), "input", filename)
    in_df = pd.read_table(fpath, sep = " ")
    return in_df


def count_vertices(in_df):
    """Counts the number of times each vector occurs in the first two columns.

    Explicitly stating first two columns because some graph array 
        might have more columns (i.e. 3rd column = weights).
    
    Args: 
        in_df (DataFrame): Dataframe with vertices (rows) in the first two columns.
    
    Returns: 
        DataFrame: A dataframe with the number of times each vertex occurs in each column.
    """
    # Count for each vertex; sort numerically
    counts_df = in_df.iloc[:, 0:2].stack(future_stack=True).value_counts().sort_index()
    return counts_df


def write_res(out_series, filename):
    """Save results to a txt file
    
    Args:
        out_series (DataFrame Series): Dataframe Series to be saved
        filename (str): Name of file to be saved including extension

    Returns:
        Writes a txt file to the output directory    
    """
    out_str = " ".join(out_series.to_string(header=False, index=False).split())

    out_path = os.path.join(os.getcwd(), "output", filename)
    with open(out_path, "w") as f:
            f.write(out_str)


def main():
    """The main driver of this script"""
    # 1. Read in graph edges file
    # Note! The first row/header contains the number of vertexes and edges, respectively.
    edges_df = get_graph_file("rosalind_deg.txt")
    # 2. Count vertices
    counts_df = count_vertices(edges_df)
    print(counts_df)
    # 3. Save dataframe
    write_res(counts_df, "rosalind_deg.txt")

main()