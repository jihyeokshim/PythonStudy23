# E7 - 7


def addition(src):
    sum = 0
    for i in range(len(src)):
        sum += src[i]
    return sum


tup1 = (10, 20, 30, 40, 50)
tup2 = (20, 10, 40)
result = addition(tup2)
print("튜플의 합계:%s" % result)
