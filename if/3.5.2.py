print("기능선택")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")

s = int(input("계산기 기능을 선택하세요(1/2/3/4)"))

num1 = int(input("첫번째 숫자를 입력하세요."))
num2 = int(input("두번째 숫자를 입력하세요."))

if s == 1:
    result = num1 + num2
elif s == 2:
    result = num1 - num2
elif s == 3:
    result = num1 * num2
elif s == 4:
    result = num1 / num2

print(result)
