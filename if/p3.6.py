# if문 중첩

print("=" * 50)
now_year = int(input("현재년은?"))
now_month = int(input("현재달은?"))
now_day = int(input("현재일은?"))

birth_year = int(input("출생년은?"))
birth_month = int(input("출생달은?"))
birth_day = int(input("출생일은?"))

if birth_month < now_month:
    age = now_year - birth_year
elif birth_month == now_month:
    if birth_day < now_day:
        age = now_year - birth_year
    else:
        age = now_year - birth_year - 1
else:
    age = now_year - birth_year - 1
print(age)
