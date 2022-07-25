# This program is for rosalind.info/problems/iprb/

# This program will use recursion to calculate Fn of the Fibonacci sequence.

# Amanda Zacharias; May 4th, 2021

"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Note: the number of offspring in any month == number of rabbits that were aliv
2 months prior.
"""

"""
Fibonnaci:
Fn = Fn - 1 + Fn - 2
F1 = F2 = 1 to initiate the sequence

Helpful video: https://www.youtube.com/watch?v=3eBIHdyGJLQ
Helpful link: https://github.com/kaniick/Rosalind/blob/
master/Bioinformatics%20Stronghold/Rabbits%20and%20Recurrence%
20Relations%20(FIB)
"""

# Read in the file
fib_file = open("rosalind_fib.txt","r")
fib_s = fib_file.read()
fib_ls = fib_s.split()
n = int(fib_ls[0])
k = int(fib_ls[1])

# Function that doesn't use recursion to calculate the total rabbit population.

def Loop_Fib(n_months, k_offspring):
    parent, child = 1, 1
    # months - 1 because the first line of this function accounts for month 1
    for i in range(n_months - 1):
        # old child -> new parent
        # old parent + (old child * k_offspring) -> new child
        child, parent = parent, parent + (child * k_offspring)
    return child

# Function that does use recursion to calculate the total rabbit population

def Rec_fib(n, k):
    # Base case, F1 = 1
    if n == 1:
        return 1
    # Base case, F2 = 1
    elif n == 1:
        return 2
    # Fn = Fn - 1 + Fn - 2
    else:
        return Rec_fib(n - 1, k) + k * Rec_fib(n - 2, k)

print(Rec_fib(n,k))

# Further optimization provided by Rosalind explanations
# Uses memoization to minimize the recursive function's running time
# Use a data structure (dictionary) to store results)

memo = {}
def Mem_fib(n, k = 1):
    args = (n, k)
    if args in memo:
        return memo[args] # We have computed this before!

    # We haven't computed this before
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = Mem_fib(n - 1, k) + k * Mem_fib(n - 2, k)
    memo[args] = ans # Store the result
    return ans

"""
The following is unit testing for Rec_fib(). Includes testing for only regular
cases.
"""

if __name__ == "__main__":
    print("Testing n = 1")
    # Test n = 1
    n = 1
    k = 2
    print(str(Rec_fib(n, k)) + " should return 1")
    print("Testing n = 2")
    # Test n = 2
    n = 2
    k = 2
    print(str(Rec_fib(n, k)) + " should return 2")
    print("Testing n = 5, k = 3")
    # Test n = 5, k = 3
    n = 5
    k = 3
    print(str(Rec_fib(n, k)) + " should return 19")
