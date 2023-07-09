phone_list1 = ["010-3654-2637", "010-3984-5377", "010-3553-0973"]
print(phone_list1)

phone_list2 = []
for numb in phone_list1:  # numb  ="010-3654-2637"
    x = numb.replace("-", "")

    phone_list2.append(x)

print(phone_list2)

[1, "test", [2, 3, 4], 3.412]
