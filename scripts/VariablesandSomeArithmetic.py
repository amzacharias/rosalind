# This program is for rosalind.info/problems/ini2/

# This program will calculate the square of the hypotenuse of the right triangle
# whose legs have lengths a and b. a and b are positive integers, each
# less than 1000.

# Formula for triangle hypotenuse: c = sqrt(a**2 + b**2)"""

a = 842
b = 985
c = (a**2) + (985**2)
# Since we want the square of something that is having its square root taken,
# these two will negate and we can skip those two steps. 
print(c)
