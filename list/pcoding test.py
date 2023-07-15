my_list = ["p", "y", "t", "h", "o", "n", "i", "s", "f", "u", "n", "!"]
# E5-1
print(my_list[5:11])

# E5-2
print(my_list[-5:-2])

# E5-3
print(my_list[8:])

# E5-4
print(my_list[:4])

# E5-5
list = []
line = "I am a genius!"
for i in range(len(line)):
    j = line[i]
    list.append(j)
print(list)

# E5-6
list = []
line = "I am a genius!"
i = 0
while i < len(line):
    j = line[i]
    list.append(j)
    i = i + 1
print(list)

numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
# E5-7
i = 0
for n in numbers:
    i = i + n
print(i)

# E5-8
i = 0
num = 0
while i < len(numbers):
    num = num + numbers[i]
    i = i + 1
print(num)

# E5-9
i = 0
n = 0
list = []
while i < len(numbers):
    if i % 2 == 1:
        list.append(numbers[i])
    i = i + 1
print("짝수 번째 요소: %s" % list)
print("합계:%s" % sum(list))

# E5-10
fruits = ["사과", "오렌지", "딸기", "수박", "멜론"]

for i in range(len(fruits)):
    print("%d.%s" % (i + 1, fruits[i]))

data = [
    [10, 20, 30],
    [
        40,
        50,
    ],
    [60, 70, 80, 90],
]
# E5-11
for row in range(len(data)):
    for x in data[row]:
        print(x, end=" ")
    print()

# E5-12
for i in range(len(data)):
    for j in range(len(data[i])):
        if j == 0:
            print(data[i][j], end=" ")
    print()

# S5-1
file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]
for i in range(len(file_names)):
    list1 = file_names[i].split(".")
    print("%s => 파일명:%s,확장자:%s" % (file_names[i], list1[0], list1[1]))

# S5-2
emails = [
    ["kim", "naver.com"],
    ["hwang", "hanmail.net"],
    ["lee", "korea.com"],
    ["choi", "gmail.com"],
]

email_new = []
for email in emails:
    x = "@".join(email)
    email_new.append(x)
print(email_new)
