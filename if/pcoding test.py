# 3-1
number = int(input("숫자를 입력하세요."))

if number > 10:
    print("%d(는) 10보다 크다." % (number))
elif number < 10:
    print("%d(는) 10보다 작다." % number)
else:
    print("%d(는) 10이다." % number)

# 3-2
number1 = int(input("첫번째 숫자를입력하세요."))
number2 = int(input("두번째 숫자를 입력하세요."))

if number1 > number2:
    print("%d 은(는) %d 보다 크다." % (number1, number2))
elif number2 > number1:
    print("%d 은(는) %d 보다 작다." % (number1, number2))
else:
    print("%d 은(는) %d 와(과)같다." % (number1, number2))

# 3-3
number = input("숫자를 입력하세요.")
number2 = int(number[2])
if number2 % 2 == 0:
    print("%d은(는) 짝수이다." % number2)
else:
    print("%d은(는)홀수이다." % number2)
