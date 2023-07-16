year_sale = {"2016": 237, "2017": 98, "2018": 158, "2019": 233, "2020": 120}

# E6-1
for key in year_sale:
    if key == "2017":
        print("%s년 자동차 판매량:%d대" % (key, year_sale[key]))
# E6-2
sm = 0
for key in year_sale:
    if key == "2019" or key == "2018":
        print("%s년 자동차 판매량:%d" % (key, year_sale[key]))
        sm = sm + year_sale[key]

print("2년간 자동차 판매량: %d대" % sm)

# E6-3
sm = 0
for key in year_sale:
    sm = sm + year_sale[key]

avg = sm / len(year_sale)

print("5년간 총 판매량: %d" % sm)
print("5년간 연 평평균 판매량: %d" % avg)

# E6-4
sum = 0
year = 0
for key in year_sale:
    if year_sale[key] > sum:
        sum = year_sale[key]
        year = key
    else:
        sum = sum
        year = year
print("판매량이 가장 많은 해:%s" % year)
print("판매량:%d대" % sum)


person = {
    "name": "홍길동",
    "age": 30,
    "family": 5,
    "children": ["선미", "성진", "소영"],
    "pets": ["강아지", "고양이", "이구아나"],
}

# E6-5
print(person["age"])

# E6-6
print(len(person))

# E6-7
for key in person:
    if key == "pets":
        for name in person[key]:
            print(name, end="/")

# E6-8
for key in person:
    if key == "children":
        n = len(person[key])
        print(n)


temp = {"월": 15.5, "화": 17.0, "수": 16.2, "목": 12.9, "금": 11.0, "토": 10.5, "일": 13.3}

# S6-1
print("-" * 30)
for key in temp:
    print(key, end="    ")
print()
print("-" * 30)
for key in temp:
    print(temp[key], end="  ")
print()

# S6-2
date = 100000
day = ""
for key in temp:
    if temp[key] < date:
        date = temp[key]
        day = key
    else:
        date = date

print("요일:%s, 최저기온:%.1f" % (day, date))

# S6-3
sum = 0
for key in temp:
    sum = sum + temp[key]
    avg = sum / len(temp)
print("일주일간 기온 평균:%.1f" % avg)
