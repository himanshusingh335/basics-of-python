# Input integers are separated by comma(,).Form num1 by adding all the numbers except which are present in between 5 and 8.And num2 by concating numbers from 5 to 8.Then display the sum of num1 and num2.

# Input Format

# First line consist of integers separated by comma(,).

# Constraints

# Assume that 8 appears after 5.

# Output Format

# Sum of num1 and num2.

# Sample Input 0

# 3,2,6,5,1,4,8,9
# Sample Output 0

# 5168

strinput=str(input())
arr=strinput.split(',')
arr=[int(i) for i in arr]
sum=0
j=0
subarr=[]
for i in range(len(arr)):
    if arr[i]==5:
        subarr.append(arr[i])
        i+=1
        while(arr[i]!=8):
            subarr.append(arr[i])
            i+=1
        subarr.append(8)
setarr=set(arr)
setsubarr=set(subarr)
newarr=setarr.difference(setsubarr)
arr=list(newarr)
sum=0
for i in arr:
    sum+=i
mystr=""
for i in subarr:
    mychar=str(i)
    mystr+=mychar
sum=sum+int(mystr)
print(sum)