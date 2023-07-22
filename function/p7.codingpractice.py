# C7-1
def add(a, b):
    c = a + b
    print("%d + %d = %d" % (a, b, c))


add(12, 15)
add(245, 300)
add(-38, -12)


# C7-2
def sum_int(start, end):
    total = 0
    for i in range(start, end + 1):
        total = total + i
    print("%d~%d 정수 합계: %d" % (start, end, total))


sum_int(20, 50)
sum_int(600, 800)


# C7-3
def member_join(*args):
    result = ""
    for arg in args:
        result = result + arg + " "
    print(
        "가입 회원:",
        result,
    )


member_join("김정연", "안서영")
member_join("황선형", "김철영", "이창연")
member_join("정수진", "김보람", "정수연", "함소영")


# C7-4
def multiply(num, x):
    i = 0
    while i < len(num):
        num[i] = num[i] * x

        i = i + 1


numbers = [10, 20, 30, 40, 50]

multiply(numbers, 10)
print(numbers)

multiply(numbers, 10)
print(numbers)


# C7-5
def tri_area(w, h):
    result = w * h * 0.5
    return result


width = int(input("너비를 입력하세요"))
height = int(input("높이를 입력하세요"))

print("-삼각형의 너비:", width)
print("-삼각형의 높이:", height)
print("-삼각형의 면적", tri_area(width, height))


# C7-6
def sum_besu(n):
    sum = 0
    for i in range(1, 101):
        if i % n == 0:
            sum = sum + i
    return sum


besu = int(input("구하고자 하는 배수를 입력하세요:"))

total = sum_besu(besu)

print("1~100 사이 %d의 배수의 합계: %d" % (besu, total))
