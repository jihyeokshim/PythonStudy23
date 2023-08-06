while True:
    grade = int(input("성적을 입력하세요:"))
    if grade >= 90:
        level = "수"
    elif 90 > grade >= 80:
        level = "우"
    elif 80 > grade >= 70:
        level = "미"
    elif 70 > grade >= 60:
        level = "양"
    elif 60 > grade:
        level = "가"
    print("등급:%s" % level)
    choice = input("계속하시겠습니까? (중단:q, 계속:y)")
    if choice == "q":
        break
