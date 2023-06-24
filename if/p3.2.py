# 비교연산자: >,<,==,!=,<=,>=
# 논리연산자: and,or,not

# 5 == 5
# True
# >>>10>20
# False
# >>>8<=8
# True
 
score1 = 85
score2 = 95
if score1 >= 80 and score2>=80:
    print("True")

x = 10
if x%2 == 0 or x%6 == 0:
    print("true")
else:
    print("false")

x = 25
if not x%2 == 0:
    print("True")