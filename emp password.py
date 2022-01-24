# Given input of array of string in format : separated by comas (,).Emp will contain only alphabets and employee number. You have to generate password based on input.

# Input Format

# emp1 name:emp1 number,emp2 name:emp2 number,...,empN name:empN number

# Constraints

# Name will consist of only alphabets and Number will consist only integer.

# Output Format

# Generated password.

# Sample Input 0

# Robert:36787,Tina:68721,Jo:56389
# Sample Output 0

# tiX
# Explanation 0

# len of robert is 6 and 6 is present in emp number of robert (36787),
# so prin4 the alphabet at position 6 that is t. 
# len of tina is 4 and it is not present in the 68721 so select the number which is maximum and it must be less than the len of tina so select 2 print the alphabet at position 2 that is i.
# len of Jo is 2 it is not present in 56389 and any number which is less than 2 is not present so print X.

inputstr=""
inputstr=str(input())
newList=inputstr.split(',')
inputDict={}
password=""
def split(word:str)->[]:
    return [char for char in word]

for i in newList:
    myList=i.split(':')
    inputDict[myList[0]]=myList[1]
for key,value in inputDict.items():
    if(str(len(key)) in split(value)):
        password+=key[len(key)-1]
    else:
        numList=split(value)
        for i in numList:
            i=int(i)
        maxNum=int(max(numList))
        while maxNum>len(key):
            if len(key)<int(min(numList)):
                break
            else:
                numList.remove(str(maxNum))
                maxNum=int(max(numList))
        if len(key)<int(min(numList)):
            password+='X'
        else:
            password+=key[maxNum-1]
print(password)