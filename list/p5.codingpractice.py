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
