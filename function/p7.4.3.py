def func():
    global x  # 여기서 x는 메인 루틴의 전역 변수
    x = 200  # x-->전역변수
    print(x)  # x-->전역변수

    x = 100  # 전역 변수: x
    print(x)  # x --> 전역 변수
    func()
    print(x)  # x --> 전역변수


def cir_area():
    global r
    result = r * r * 3.14
    return result


def cir_length():
    global r
    result = 2 * 3.14 * r
    return result


r = float(input("반지름을 입력하세요:"))
area = cir_area()
length = cir_length()
print("원의 면적: %.1f, 원주의 길이: %.1f" % (area, length))

# alternative


def cir_area(r):
    result = r * r * 3.14
    return result


def cir_length(r):
    result = 2 * 3.14 * r
    return result


r = float(input("반지름을 입력하세요:"))
area = cir_area()
length = cir_length()
print("원의 면적: %.1f, 원주의 길이: %.1f" % (area, length))
