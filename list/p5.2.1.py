colors = ["빨간색", "파란색", "노란색", "검정색", "초록색"]

for color in colors:
    print("나는 %s을 좋아한다" % color)  # %S는 문자열

# or

n = len(colors)  # len() 함수: 리스트 길이
for i in range(0, n):  # i의 값:0~4
    print("나는 %s을 좋아한다" % colors[i])  # i : colors의 인덱스
