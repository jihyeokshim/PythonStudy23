def func(n):
    x = n + 5
    return x


a = func(10)
print(a)
b = func(20)
print(b)

# 서식: def 함수(매개변수1, 매개변수2,...):
# 문장1
# 문장2
# ...
# return 변수 1
# ...
# 변수2 = 함수(입력값1, 입력값2,...)
# ...


def inch_to_cm(inch):
    cm = inch * 2.54
    return cm


num = int(input("인치를 입력하세요:"))
result = inch_to_cm(num)
print("%d inch => %.2f cm" % (num, result))
