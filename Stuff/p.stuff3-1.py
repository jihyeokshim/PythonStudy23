def grader(a):
    if a == "A+":
        b = 4.5
    elif a == "A":
        b = 4.0
    elif a == "B+":
        b = 3.5
    elif a == "B":
        b = 3.0
    elif a == "C+":
        b = 2.5
    elif a == "C":
        b = 2.0
    elif a == "D+":
        b = 1.5
    elif a == "D":
        b = 1.0
    elif a == "F":
        b = 0

    return b


grade = input("등급을 입력해주세요(A+,A,B+,...,F)")
score = grader(grade)
print("등급:%s, 평점:%d" % (grade, score))
