# E7-6


def count(s, a):
    cnt = 0
    for x in s:
        if x == a:
            cnt += 1
    return cnt


sent = input("영어 문장을 입력해주세요")
y = input("알파벳 하나를 입력하세요.")

print("%s에 포함된 %s의 개수는 %d개이다." % (sent, y, count(sent, y)))
