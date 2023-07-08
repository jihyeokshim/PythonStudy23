# remove():
member = ["홍지웅", 20, "경기도 김포시", "jiwoong@naver.com", "010-1234-5678"]
print(member)

member.remove(20)  # 20의 값을 가진 요소 삭제
print(member)

# pop():
data = [10, 20, 30, 40, 50, 60, 70, 80]
print(data)

x = data.pop(2)
print(x)
print(data)

x = data.pop(3)
print(x)
print(data)

# clear():
data = [3, 12, 7, -3, -9]
print(data)

data.clear()
print(data)
