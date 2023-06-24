# start = int(input("시작수는?"))
 # end = int(input("끝수는?"))
 # number = int(input("정수를 입력하세요"))

# if start< number < end:
#     print("%d은(는) %d~%d 사이에 있다." %(number,start,end))
# else:
#     print("%d은(는) %d~%d 사이에 없다."%(number,start,end))

# month = int(input("월을 숫자로 입력하세요:"))
# if 3 <= month <= 5:
#         print("%d월은봄입니다." %(month))
# if 6 <= month <= 8:
#      print("%d월은여름입니다." %(month))
# if 9 <= month <= 11:
#      print("%d월가을입니다." %(month))
# if 12 <= month <= 2:
#      print("%d월은겨울입니다." %(month))

number = int(input("주민번호 뒷자리 첫번째 숫자를 입력해 주세요."))
if number == 1 or number == 3:
      print("남성입니다.")
elif number == 4 or number == 2:
      print("여성입니다.")
else:
      print("err")