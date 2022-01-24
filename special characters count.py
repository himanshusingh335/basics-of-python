# Solve the problem based on the number of special characters.If the count is odd print first odd digits and next even digits(and viceversa) in the same series present in the string.

# Input Format

# First line consist of string with alphabets,numbers and special characters.

# Constraints

# No Constraints

# Output Format

# Consist of Numbers alone.

# Sample Input 0

# abc@147#25%gd&b
# Sample Output 0

# 42175

inputstr=str(input())
i=0
numbers=[]
for a in inputstr:
    if a>="a" and a<="z" or a>="0" and a<="9":
        if a>="0" and a<="9":
            numbers.append(int(a))
    else:
        i=i+1

if i%2==0:
    numbers=sorted(numbers,key=lambda x:x%2)
else:
    numbers=sorted(numbers,key=lambda x:x%2, reverse=True)

strnumbers=""
for b in numbers:
    strnumbers+=str(b)
print(strnumbers)