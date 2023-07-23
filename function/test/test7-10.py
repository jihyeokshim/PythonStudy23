def change(a):
    result = 0
    if a == "1":
        b = int(input("센티미터 단위의 길이를 입력하세요."))
        result = b * 0.393701
        print("%s센티미터 --> %.2f인치" % (b, result))
    elif a == "2":
        b = int(input("킬로그램 단위의 무게를 입력하세요."))
        result = b * 2.204623
        print("%s킬로그램 --> %.2f파운드" % (b, result))
    else:
        print("옵션을 선택해주세요.")


option = input("원하는 환산 단위를 선택하세요.(1/2):")
change(option)
