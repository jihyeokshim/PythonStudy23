# C5-1
data = list(range(1, 22))
for i in range(0, len(data)):
    print("%d" % i, end=" ")

# C5-2
num = list(range(1, 22))
for i in range(0, len(num)):
    if (num[i]) % 2 == 0:
        print("%d" % num[i], end=" ")

# C5-3
num = list(range(0, 21))
i = 1
while i < len(num):
    if (i) % 2 != 0:
        print("%d" % i, end=" ")
    i = i + 1

# C5-4
data = []

for x in range(10, 21):
    data.append(x)

print(data)

# C5-5
questions = ["s_hool", "compu_er", "deco_ation", "windo_", "hi_tory"]
answer = ["c", "t", "r", "w", "s"]
for i in range(len(questions)):
    q = "%s:밑 줄에 들어갈 알파벳은?" % questions[i]
    guess = input(q)

    if guess == answer[i]:
        print("정답")
    else:
        print("오답")

# C5-6
scores = []

while True:
    x = int(input("성적을 입력하세요(종료시 -1 입력)"))
    if x == -1:
        break
    else:
        scores.append(x)
print(scores)
sum = 0
# for score in range(0, len(scores)):
#     sum = sum + scores[score]

for score in scores:
    sum = sum + score

avg = sum / len(scores)
print("합계:%d,평균:%.2f" % (sum, avg))

# C5-7
s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87, 87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

soo = 0
woo = 0
mi = 0
yang = 0
ga = 0

i = 0
while i < len(s):
    if s[i] >= 90:
        soo = soo + 1
    if 89 >= s[i] >= 80:
        woo = woo + 1
    if 79 >= s[i] >= 70:
        mi = mi + 1
    if 69 >= s[i] >= 60:
        yang = yang + 1
    if 59 >= s[i]:
        ga = ga + 1
    i = i + 1

print("수:%d명" % soo)
print("우:%d명" % woo)
print("미:%d명" % mi)
print("양:%d명" % yang)
print("가:%d명" % ga)

# C5-8
seats = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
]
print(len(seats))
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == 0:
            print("%3s" % "□", end="")
        else:
            print("%3s" % "∎", end="")
    print()
