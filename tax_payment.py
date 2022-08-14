def filter(N, A, Q):
    countArr = []
    string = ""
    for i in Q:
        count = 0
        l = i[0]
        r = i[1]
        x = i[2]
        for j in A:
            if l <= j[0] <= r:
                if j[1] > x:
                    count += 1
        if(count != 0):
            countArr.append(count)
    for i in countArr:
        return i


N = int(input())
A = []
Q = []
for i in range(N):
    strinput = str(input()).split(' ')
    arr = [int(i) for i in strinput]
    A.append(arr)
q = int(input())
for i in range(q):
    strinput = str(input()).split(' ')
    arr = [int(i) for i in strinput]
    Q.append(arr)

print(filter(N, A, Q))
