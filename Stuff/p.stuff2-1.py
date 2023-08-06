kg = int(input("변환할 킬로그램(kg)은?"))
pound = kg * 2.204623
ounce = kg * 35.273962

print("-" * 30)
print("킬로그램  파운드  온스")
print("-" * 30)
print("%d%13.2f%8.2f" % (kg, pound, ounce))
