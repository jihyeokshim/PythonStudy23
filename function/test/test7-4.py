# E7-4
def mile_kilo(kilo):
    mile = kilo * 0.621371
    return mile


kilo = int(input("킬로미터를 입력하세요."))
print("%s 킬로미터는 %.2f마일이다." % (kilo, mile_kilo(kilo)))
