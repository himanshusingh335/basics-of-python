import math


def preprocess(p, x, y, n):
    for i in range(n):
        p[i] = x[i] * x[i] + y[i] * y[i]

    p.sort()


def query(p, n, rad):

    start = 0
    end = n - 1
    while ((end - start) > 1):
        mid = (start + end) // 2
        tp = math.sqrt(p[mid])

        if (tp > (rad * 1.0)):
            end = mid - 1
        else:
            start = mid

    tp1 = math.sqrt(p[start])
    tp2 = math.sqrt(p[end])

    if (tp1 > (rad * 1.0)):
        return 0
    elif(tp2 <= (rad * 1.0)):
        return end + 1
    else:
        return start + 1


n = int(input())
arrx = []
arry = []
for i in range(n):
    arrstr = str(input()).split()
    arr = [int(i) for i in arrstr]
    arrx.append(arr[0])
    arry.append(arr[1])
q = int(input())
p = [0]*n
preprocess(p, arrx, arry, n)
for i in range(q):
    q1 = int(input())
    print(query(p, n, q1))


# def solve(pointCount, points, queryCount, queries):
#     return 0


# pointCount = int(input())
# points = [list(map(int, input().split()))for i in range(pointCount)]
# queryCount = int(input())
# queries = []
# for i in range(queryCount):
#     queries.append(input())
# out_ = solve(pointCount, points, queryCount, queries)
# for i in out_:
#     print(i)
