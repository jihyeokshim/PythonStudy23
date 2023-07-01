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

# 3-4
number = int(input("첫번째 숫자를 입력하세요."))
number2 = int(input("두 번빼 숫자를 입력하세요."))
answer = number + number2
if answer % 3 == 0:
    print("%d은(는) 3 의배수이다." % (answer))
else:
    print("%d은(는) 3 의배수가 아니다." % (answer))

# 3-5
age = int(input("당신의 나이는?"))
if age < 35:
    print("당신은 평균 나이(35세)미만이다.")
else:
    print("당신은 평균 나이(35세)이상이다.")

# 3-6
numb = input("수를 입력하세요.")
n = int(len(numb))
if n == 1:
    print("%d 은(는) 한자리 숫자이다." % int(numb))
elif n == 2:
    print("%d 은(는) 두자리 숫자이다." % int(numb))
elif n == 3:
    print("%d 은(는) 세자리 숫자이다." % int(numb))
else:
    print("오류! %d 은(는) 범위(0~999) 이외의 숫자이다." % int(numb))

# 3-7
line = input("문자열을 입력하세요.")
n = int(len(line))
if n % 2 == 0:
    print("문자열의 개수: %d" % n)
    print("문자열의 개수는 짝수이다.")
elif n % 2 != 0:
    print("문자열의 개수: %d" % n)
    print("문자열의 개수는 홀수이다.")
else:
    print("오류!")

# 3-8
num1 = int(input("첫번째 숫자를 입력하세요."))
num2 = int(input("두번째 숫자를 입력하세요."))
print("원하는 연산은?")
symbol = input("+,-,*,/ 중 하나를 선택하세요.")
if symbol == "+":
    ans = num1 + num2
    print("%d+%d = %d" % (num1, num2, ans))
elif symbol == "-":
    ans = num1 - num2
    print("%d-%d = %d" % (num1, num2, ans))
elif symbol == "*":
    ans = num1 * num2
    print("%d*%d = %d" % (num1, num2, ans))
elif symbol == "/":
    ans = num1 / num2
    print("%d/%d = %.2f" % (num1, num2, ans))
else:
    print("오류")

# 3-9
grade = int(input("점수를 입력하세요."))
if 100 >= grade >= 90:
    print("성적:%d점, 등급:수" % grade)
elif 89 >= grade >= 80:
    print("성적:%d점, 등급:우" % grade)
elif 79 >= grade >= 70:
    print("성적:%d점, 등급:미" % grade)
elif 69 >= grade >= 60:
    print("성적:%d점, 등급:양" % grade)
elif 59 >= grade >= 0:
    print("성적:%d점, 등급:가" % grade)
else:
    print("입력오류!")

# s3-1
grade = input("등급을 입력해 주세요.(A+,A,B+,B,C+,C,D+,D,F)")
if grade == "A+":
    print("등급:A+, 평점:4.5")
elif grade == "A":
    print("등급:A, 평점:4")
elif grade == "B+":
    print("등급:B+, 평점:3.5")
elif grade == "B":
    print("등급:B, 평점:3")
elif grade == "C+":
    print("등급:C+, 평점:2.5")
elif grade == "C":
    print("등급:C, 평점:2")
elif grade == "D+":
    print("등급:D+, 평점:1.5")
elif grade == "D":
    print("등급:D, 평점:1")
elif grade == "F":
    print("등급:f, 평점:0")
else:
    print("오류")

# s3-2
timehour1 = int(input("첫 번째 시간의 시를 입력하세요."))
timeminute1 = int(input("첫 번째 시간의 분을 입력하세요."))
timehour2 = int(input("두 번째 시간의 시를 입력하세요."))
timeminute2 = int(input("두 번째 시간의 분을 입력하세요."))

time1 = "%d:%d" % (timehour1, timeminute1)
time2 = "%d:%d" % (timehour2, timeminute2)

if timehour1 or timehour2 > 12:
    print("오류")
elif timeminute1 or timeminute2 > 59:
    print("오류")
else:
    if timehour1 < timehour2:
        print("빠른시간:" + time1)
        print("늦은시단:" + time2)
    elif timehour2 < timehour1:
        print("빠른시간:" + time2)
        print("늦은시단:" + time1)
    elif timehour1 == timehour2:
        if timeminute1 < timeminute2:
            print("빠른시간:" + time1)
            print("늦은시단:" + time2)
        elif timeminute2 < timeminute1:
            print("빠른시간:" + time2)
            print("늦은시간:" + time1)
        else:
            print("오류")
    else:
        print("오류")

# s3-3
name = input("이름을 입력하세요.")
time = int(input("일주일간 일한 시간을 입력하세요."))

overtime = time - 40
if 0 <= time <= 40:
    money = time * 12000
elif time > 40:
    money = (40 * 12000) + (overtime * 18000)

if overtime > 0:
    print("이름:" + name)
    print("일주일간 일한 시간:%d시간" % time)
    print("오버타임:%d" % overtime)
    print("주급:%d" % money)
elif overtime == 0:
    print("이름:" + name)
    print("일주일간 일한 시간:%d시간" % time)
    print("오버타임:0")
    print("주급:%d" % money)
else:
    print("오류")
