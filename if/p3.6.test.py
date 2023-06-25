# cost = int(input("구매 금액은?"))

# if 10000 <= cost < 50000:
#     sale = 5
# elif 50000 <= cost < 300000:
#     sale = 7.5
# elif 300000 <= cost:
#     sale = 10
# else:
#     sale = 0

# discount = cost * sale / 100
# pay = cost - discount
# print(pay)


# print("서비스 만족도")
# print("1.매우만족")
# print("2.만족")
# print("3.불만족")
# print("1/2/3")
# rating = int(input("점수를 매겨주세요."))
# cost = int(input("음식값은?"))

# if rating == 1:
#     tip = 20
# elif rating == 2:
#     tip = 10
# elif rating == 3:
#     tip = 0

# tipmoney = cost / 100 * tip
# print(cost + tipmoney)


# first = int(input("첫번째 정수는?"))
# second = int(input("두번째 정수는?"))
# third = int(input("세번째 정수는?"))
# if first > second and first > third:
#     largest = first
# elif second > first and second > third:
#     largest = second
# elif third > first and third > second:
#     largest = third
# print("%d,%d,%d중에서 가장 큰 수는 %d 입니다." % (first, second, third, largest))


# id = input("아이디를 입력해주세요.")
# if id == "admin":
#     password = int(input("비밀번호를 입력해주세요."))
#     if password == 2456:
#         print("컨텐츠 이용이 가능합니다.")
#     else:
#         print("접속 불가 다시 시도해주세요.")
# elif id != "admin":
#     level = int(input("회원레벨은?(1~9)"))
#     if 1 <= level <= 3:
#         print("컨텐츠이용이 가능합니다.")
#     elif 4 <= level <= 9:
#         print("콘텐츠를 이용할 수 없습니다.")


unit = int(input("단위를 입력해주세요(1.섭씨 2.화씨)"))
temp = int(input("온도를 입력해주세요"))

if unit == 1:
    if temp <= 0:
        state = str("고체")
    elif 0 < temp <= 100:
        state = "액체"
    else:
        state = "기체"
elif unit == 2:
    temp = temp * 9 / 5 + 32
    if temp <= 32:
        state = "고체"
    elif temp >= 212:
        state = "액체"
    else:
        state = "기체"
print(temp, state)
