count = 0
i = 1
while i <= 1000:
    if i % 3 != 0:
        print(i, end=" ")
        count = count + 1
        if count % 10 == 0:
            print("\n")
    i = i + 1
