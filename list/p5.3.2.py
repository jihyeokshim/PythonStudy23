arr = [5, 3, 12, 9, 2]
print(arr)

arr.append(10)
print(arr)


scores = []  # []: 빈 리스트, 요소가 없음

while True:  # 무한 반복
    score = int(input("성적을 입력하세요(종료:-1)"))

    if score == -1:
        break  # score가 -1이면 while루프 빠져나감
    else:
        scores.append(score)
print(scores)
