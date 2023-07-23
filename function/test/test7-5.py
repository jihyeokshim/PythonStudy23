# E7-5
def calculator(opt, num1, num2):
    result = 0
    global o
    if opt == 1:
        o = "+"
        result = num1 + num2
    elif opt == 2:
        o = "-"
        result = num1 - num2
    elif opt == 3:
        o = "*"
        result = num1 * num2
    elif opt == 4:
        o = "*"
        result = num1 / num2
    else:
        print("옵션을 선택해주세요.")
    return result


o = ""
x = int(input("원히는 연산을 선택하세요(1/2/3/4):"))
y = int(input("첫 번째 숫자를 입력하세요:"))
z = int(input("두 번째 숫자를 입력하세요:"))
res = calculator(x, y, z)
print("%s%s%s = %s" % (y, o, z, res))
