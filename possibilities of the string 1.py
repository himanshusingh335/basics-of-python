# Print all the possibilities of the given string of length of the string

# Input Format

# First line consist of input string

# Constraints

# No constraints

# Output Format

# Each possibility is printed in new line.

# Sample Input 0

# abc
# Sample Output 0

# abc
# acb
# bac
# bca
# cab
# cba

from itertools import permutations

strinput=str(input())
perm=permutations(strinput)
permstr=""
for i in perm:
    for j in i:
        permstr+=j
    print(permstr)
    permstr=""