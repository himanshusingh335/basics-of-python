# Reverse the given input string without changing the positions of the special characters.

# Input Format

# First line consist of string with special characters

# Constraints

# No Constraints

# Output Format

# First line consist of reverse of the string without changing the positions of special characters.

# Sample Input 0

# abcd@12#ef$k
# Sample Output 0

# kfe2@1d#cb$a

mystr=str(input())
myList=[]
for i in mystr:
    if i>='a' and i<='z' or i>='0' and i<='9':
        myList.append(str(i))
myList.reverse()
a=0
newList=list(mystr)
for i in range(len(mystr)):
    if mystr[i]>='a' and mystr[i]<='z' or mystr[i]>='0' and mystr[i]<='9':
        newList[i]=myList[a]
        a=a+1
newstr=""
for i in newList:
    newstr=newstr+i
print(newstr)