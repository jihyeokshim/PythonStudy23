word = input("영어 문장을 입력하세요.")

for x in word:
    print(x)


phone = input("하이픈(-)을 포함한 후대폰 번호를 입력하세요.")

for x in phone:
    if x != "-":
        print("%s" % x, end="")
