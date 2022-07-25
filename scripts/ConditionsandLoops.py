# This program is for rosalind.info/problems/ini4/

# This program will sum all odd integers that are found between two positive
# integers

# Amanda Zacharias; April 26th, 2021

"""
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
"""

a = 4537
b = 9210
output = 0

for i in range(a,b+1):
    if i % 2 == 1:
        output = output + i
    else:
        output = output

print(output)
