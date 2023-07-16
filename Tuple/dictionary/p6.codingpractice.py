# C6-1
dans = (2, 3, 4, 5, 6, 7, 8, 9)

print("구구단표")
print("=" * 30)

for dan in dans:
    print(str(dan) + "단")
    for i in range(1, 10):
        print("%d x %d = %d" % (dan, i, dan * i))
    print("-" * 30)

# C6-2
scores = {"김채린": 85, "박수정": 98, "함소희": 94, "안예린": 90, "연수진": 93}
sum = 0

for key in scores:
    sum = scores[key] + sum

    print("%s:%d" % (key, scores[key]))

avg = sum / len(scores)
print("합계:%d,평균:%.2f" % (sum, avg))

# C6-3
admin_info = {"id": "admin", "password": "12345"}

input_id = input("아이디를 입력하세요")
input_pass = input("비밀번호를 입력하세요:")

if input_id == "admin" and input_pass == "12345":
    print("정보에 접근 권한이 있습니다!")
else:
    print("정보에 접근 권한이 없습니다!")

# C6-4
words = {"꽃": "flower", "나비": "butterfly", "학교": "school", "자동차": "car", "비행기": "plane"}
print("<영어 단어 맞추기 킈즈>")

for kor in words:
    input_word = input("%s에 해당되는 영어 단어를 입력해주세요:" % kor)

    if input_word == words[kor]:
        print("정답입니다.")
    else:
        print("틀렸읍니다.")
