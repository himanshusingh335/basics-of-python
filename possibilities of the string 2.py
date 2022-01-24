# Task is to print all the possibilities of the string till the length of the given string.

# Input Format

# First line consist of a string

# Constraints

# No constraints

# Output Format

# Each possiblities are printed in the new line

# Sample Input 0

# abc
# Sample Output 0

# a
# b
# c
# ab
# ac
# ba
# bc
# ca
# cb
# abc
# acb
# bac
# bca
# cab
# cba
from itertools import permutations
 
inputstr=str(input())
newstr=""
for n in range(1,len(inputstr)+1):
    perm=permutations(inputstr,n)
    for i in perm:
        for j in i:
            newstr+=j
        print(newstr)
        newstr=""