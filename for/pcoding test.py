# E4-1
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
        print()

# E4-2
sums = 0
for i in range(1, 101):
    if i % 3 == 0:
        sums = sums + i
print("1~100 까지 3의 배수 합계: %d" % sums)

# E4-3
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")

# E4-4
count = 0
for i in range(1, 101):
    if i % 5 == 0:
        print("%d" % i, end=" ")
        count = count + 1
    if count % 5 == 0:
        print()

# E4-5
sum = 0
for i in range(1, 101):
    if i % 4 == 0:
        sum = sum + i
        print("%d --> %d" % (i, sum))

# E4-6
j = 1
for i in range(1, 11):
    j = j * i
    print("10! = %d" % j)

# E4-7
i = 1
j = 1
while i <= 10:
    j = j * i
    i = i + 1
    print("10! = %d" % j)

# E4-8
print("-" * 50)
print("   cm     mm     m     inch")
print("-" * 50)
for cm in range(1, 51):
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.39
    print("%5d %6d %6.1f %6.1f" % (cm, mm, m, inch))

# E4-9
print("-" * 50)
print("   cm     mm     m     inch")
print("-" * 50)
cm = 1
while cm <= 50:
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.3937
    cm = cm + 1
    print("%5d %6d %6.2f %6.2f" % (cm, mm, m, inch))

# S4-1
num = 0
count = 0
while num < 1000:
    num = num + 1
    if num % 3 != 0:
        count = count + 1
        print(num, end=" ")
    if count % 10 == 0:
        print()

# S4-2
while True:
    grade = int(input("성적을 입력하세요."))
    if grade >= 90:
        print("등급:수")
    elif 90 > grade >= 80:
        print("등급: 우")
    elif 80 > grade >= 70:
        print("등급: 미")
    elif 70 > grade >= 60:
        print("등급: 양")
    elif 60 > grade:
        print("등급: 가")
    choice = input("계속하시겠습니까?(중단:q,계속:y)")
    if choice == "y":
        continue
    if choice == "q":
        break

# S4-3
num = int(input("시작 수를 입력해주세요."))
num2 = int(input("끝수를 입력해주세요."))

for i in range(num, num2 + 1):
    flag = False

    for b in range(2, i // 2):
        if i % b == 0:
            flag = True
            break

    if flag == False:
        print(i, end=" ")
