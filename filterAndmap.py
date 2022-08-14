x = []
for i in range(5):
    a = int(input("Enter number "+str(i+1)+": "))
    x.append(a)


def filterEven(num: int) -> bool:
    if(num % 2 == 0):
        return False
    else:
        return True


def multiply2(num: int) -> int:
    return num*2


l1 = list(filter(filterEven, x))
l2 = list(map(multiply2, l1))
print(l1, l2, sep=",")
