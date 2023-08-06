def program(a):
    if a <= 40:
        overtime = 0
        pay = 12000 * a
    elif a > 40:
        overtime = a - 40
        pay = (12000 * 40) + (overtime * (12000 * 1.5))
    return overtime, pay


name = input("이름을 입력하세요:")
worktime = int(input("일주일간 일한 시간을 입력하세요"))
overtime, pay = program(worktime)
print("-이름: %s" % name)
print("- 일주일간 일한 시간: %d시간" % worktime)
print("-오버타임:%d" % overtime)
print("-주급: %d" % pay)
