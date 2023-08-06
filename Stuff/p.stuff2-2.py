phone = input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")
nohyphon = phone[0:3] + phone[4:8] + phone[9:13]
print(nohyphon)

phone = "010-1010-2020"
print(phone.replace("-", ""))
