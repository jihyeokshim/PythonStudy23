# if 조건식:
#     문장1
#     문장2

# else:
#     문장A
#     문장B

x = int(input("양의 정수를 입력하세요"))

if x % 2 == 0:
    print("짝수이다")
else:
    print("홀수이다")


pilgi = int(input("필기점수를 입력하세요"))
silgi = int(input("실기점수를 입력하세요"))

if pilgi >= 80 and silgi >= 80:
    result = "합격"
else:
    result = "불합격"

print("-필기 시험점수:%d" % (pilgi))
print("-실기 시험점수:%d" % (silgi))
print(result)


char = input("영어 소문자 하나 입력하세요.")

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(char + "는 모음이다.")
else:
    print(char + "는 자음이다.")
