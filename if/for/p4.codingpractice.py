# C4-1
count = 0
for i in range(200, 801):
    if i % 5 != 0:
        print("%d" % i, end=" ")
        count = count + 1
    if count % 10 == 0:
        print()

# C4-2
print("-" * 40)
print("     cm      mm      m       inch")
print("-" * 40)

for cm in range(1, 101):
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm * 0.3937
    print("     %d      %d      %d      %d" % (cm, mm, m, inch))
print("-" * 40)

# C4-3
for i in range(1, 11):
    print("*" * (0 + i), end=" ")
    print()

# C4-4
for i in range(1, 11):
    print("*" * (10 - i), end=" ")
    print()

# C4-5
number = input("숫자를 입력하세요.")

total = 0

for a in number:
    a = int(a)
    if a % 2 != 0:
        total = total + 1

print("홀수의 개수:%d개" % total)

# C4-6
print("-" * 50)
print(" 킬로그램  파운드  온스")
print("-" * 50)

for kg in range(100, 201, 2):
    pound = kg * 2.204623
    ounce = kg * 35.273962
    print("%5d%6.1f%7.1f" % (kg, pound, ounce))

# C4-7
for i in range(5):
    for j in range(10):
        print("*", end=" ")
    print()

# C4-8
for i in range(9, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

# C4-9
n = 1
sum = 0
count = 0

while n <= 100:
    if n % 2 != 0:
        sum = sum + n
        print("%6d" % sum, end=" ")
        count = count + 1

        if count % 10 == 0:
            print()

    n = n + 1

# C4-10
print("-" * 30)
print("     달러    원화    유로")
print("-" * 30)

dollar = 0

while dollar <= 100:
    won = dollar * 1080
    euro = dollar * 0.81

    print("%7d %8.0f %7.1f" % (dollar, won, euro))

    dollar = dollar + 10

print("-" * 30)

# C4-11
sentence = input("문장을 입력해주세요")
i = len(sentence) - 1

while i >= 0:
    if sentence[i] == " ":
        print("-", end="")
    else:
        print("%s" % sentence[i], end="")
    i = i - 1
