x1 = int(input("좌표1 의 x:"))
y1 = int(input("좌표1 의 y:"))
x2 = int(input("좌표2 의 x:"))
y2 = int(input("좌표2 의 y:"))


def sub(a, b):
    ans = a - b
    return ans


def sqrt(a):
    ans = a * a
    return ans


def add(a, b):
    ans = a + b
    return ans


def root(a):
    for c in range(1,99999999999):



a = sub(x2, x1)
b = sub(y2, y1)

a1 = sqrt(a)
b2 = sqrt(b)

c = add(a1, b2)
print(c)
