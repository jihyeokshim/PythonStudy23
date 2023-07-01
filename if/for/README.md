### 반복문:

### for문, while문

### for문:

```python
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")
```

==

```python
for x in range(5)  #x가 0~4의 값을 가지고 5번 반복
print("안녕하세요!")
```

#### for문은 특정 문장을 여러번 반복수행 시키는데 사용

#### range(숫자) 0 에서 시작하고 숫자-1 에서 끝난다

### for문의 기본 구조:

```python
for i in range(10):      #for변수 in range(종료값):
    print(i,end=" ")     #문장1,문장2,...
결과:0 1 2 3 4 5 6 7 8 9

for i in range(1,11):    #for 변수 in range(시작값,종료값):
    print(i,end=" ")      #문장1,문장2...
결과:1 2 3 4 5 6 7 8 9 10

for i in range(1,10,2):  #for 변수 in range(시작값,종료값,증가_감소)
    print(i,end=" ")      #문장1,문장2...
결과: 1 3 5 7 9
```

### for문 문자열

```python
word = input("영어 문장을 입력하세요.")

for x in word:     # x는 word의 각 문자를 가지고 반복
    print(x,end="")
결과: 문장:I am happy
      I  a m  h a p p y
```
