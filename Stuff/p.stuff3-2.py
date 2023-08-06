def timer(a, b, c, d):
    slow = ""
    fast = ""
    if c > a:
        slow = "%s:%s" % (c, d)
        fast = "%s:%s" % (a, b)
    elif a > c:
        slow = "%s:%s" % (a, b)
        fast = "%s:%s" % (c, d)
    elif a == c:
        if b > d:
            slow = "%s:%s" % (a, b)
            fast = "%s:%s" % (c, d)
        elif b < d:
            slow = "%s:%s" % (c, d)
            fast = "%s:%s" % (a, b)

    return slow, fast


hour1 = input("첫 번째 시간의 시를 입력하세요.")
minute1 = input("첫 번째 시간의 분을 입력하세요.")
hour2 = input("두 번째 시간의 시를 입력하세요.")
minute2 = input("두 번째 시간의 분을 입력하세요.")
slow, fast = timer(hour1, minute1, hour2, minute2)
print("빠른시간:%s" % fast)
print("느린시간:%s" % slow)
