char = input("영문 대문자 또는 소문자 하나를 입력하세요")

if (
    char == "a"
    or char == "A"
    or char == "e"
    or char == "E"
    or char == "i"
    or char == "I"
    or char == "o"
    or char == "O"
    or char == "u"
    or char == "U"
):
    result = "모음"
else:
    result = "자음"

print("%s->%s" % (char, result))


height = int(input("키를 입력하세요"))
weight = int(input("몸무게를 입력하세요"))

s = (height - 100) * 0.9
if s <= weight:
    print("표준또는 마른 체형입니다.")
else:
    print("다이어트가 필요함")

daypay = 9500
nightpay = daypay * 1.5
time = int(input("1(주간근무) 또는 2(야간 근무시간)을 입력해주세요.)"))
timework = int(input("근무시간을 입력해주세요."))
if time == 1:
    pay = timework * daypay
elif time == 2:
    pay = timework * nightpay

print("%d시간동안 일한 주간 급여는 %d원 입니다." % (timework, pay))
