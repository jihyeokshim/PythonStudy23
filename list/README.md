## 리스트

#### 리스트란?

#### 리스트는 여러개의 값을 하나의 변수에 담을수있는 구조이다.

### 리스트 생성 = 2가지 방법

```python
list1 = [3,15,-12,5,"사과","딸기"]  #[]를 이용하여 리스트 생성
print(list1)

list2 = list(range(1,21,2))         #list() 함수로 리스트 생성
print(list2)

#실행결과:
[3,15,-12,5,'사과','딸기']
[1,3,5,7,9,11,13,15,17.19]
```

#### 기본서식: 리스트명 = [요소1,요소2,요소3]

#### 리스트에서 요소 추출:

```python
color = ["빨강", "주황", "노랑", "초록","파랑","남색","보라"]
print(color[0])     #인덱스는 0부터
print(color(5))     #인덱스 5 의 요소
print(color[2:6])   #인덱스 2부터 5까지
print(color[-3])    #뒤에서 3번째 요소
print(color[-4:-1]) #뒤에서 4번째부터 뒤에서 2번째 까지의 요소
```

### for문에서 리스트 사용

```python
colors = ["빨간색","파란색","노란색","검정색","초록색"]

for color in colors:
    print("나는 %s을 좋아한다" %color)    #%s는 문자열
```

> 실행 결과

```
나는 빨간색을 좋아한다
나는 파란색을 좋아한다
나는 노란색을 좋아한다
나는 검정색을 좋아한다
나는 초록색을 좋아한다
```

#### 기본 형식: for변수 in '리스트명':

### While문에서 리스트 사용

```python
animals = ["코끼리", "호랑이", "사슴", "펭귄", "여우"]

i = 0
while i < len(animals):      #len()함수:리스트 길이
    print(animals[i])        #animals[i]:인덱스i의 요소

    i = i + 1
```

> 실행 결과

```
코끼리
호랑이
사슴
펭귄
여우
```

### 리스트 요소 변환

#### 리스트명 다음에 점(.)을 찍은 다음 함수명을 사용하는 함수르 메소드(Method)라고 한다

```
  메소드    /                      의미
  -----------------------------------------------------------------
  append()  / 리스트 제일 뒤에 새로운 요소 추가
  insert()  / 리스트에서 특정 인덱스 앞에 새로운 요소 삽입
  index()   / 리스트에서 특정 요소의 위치인 인덱스번호를 구함
  remove()  / 리스트에서 특정갑을 가진 요소를 삭제함
  pop()     / 리스트에서 특정 인덱스 번호를 가진 요소를 추출하고
              그 요소를 삭제함
  clear()   / 리스트의 전체 요소를 삭제함
  reverse() / 리스트 요소를 거꾸로함
  copy()    / 리스트를 복사하여 새로운 리스트를 생성함
  sort()    / 리스트 요소들을 오름차순(또는 내림차순)으로 정렬함
```

#### 리스트 요소 수정

##### 서식:리스트명[인덱스] = 데이터

```python
flowers = ["목련","벚꽃","장미","백일홍"]
flowers[1] = 무궁화    #리스트flowers의 인덱스 1, "벚꽃"을 "무궁화"로 수정한다.
print(flowers)

결과:  ["목련","무궁화","장미","백일홍"]
```

#### 리스트 요소 추가( append() )

##### 서식:리스트명.append(데이터)

```python
list = [5,3,12,9,2]
arr.append(10)     #
print(arr)

결과: [5,3,12,9,2,10]
```

#### 리스트 요소 삽입( insert() )

##### 서식:리스트명.insert(인덱스번호,데이터)

```python
fruits = ["apple","orange","banana","cherry"]
print(fruits)

fruits.insert(1,"melon")
print(fruits)

fruits.insert(2,"strawberry")
print(fruits)

결과:  ["apple","orange","banana","cherry"]
       ["apple","melon","orange","banana","cherry"]
       ["apple","melon","strawberry","orange","banana","cherry"]
```

#### 리스트 요소 위치 찾기( index() )

##### 서식: 리스트명.index(인덱스 번호)

```python
number = [5,20,13,7,8,22,7,17]
print(number)

idx = number.index(7)   #7이 가장 먼저 나오는 위치의 인덱스 번호: 3
print(idx)

결과: [5,20,13,7,8,22,7,17]
       3
```

#### 리스트 요소 삭제하기( remove(), pop(), clear() )

##### remvove() <br/><br/> 서식: 리스트명.remove(데이터)

```python
numbers = [1,5,15,20,24,17,35]
print(numbers)

numbers.remove(20)    #20의 값을 가진 요소 삭제
print(numbers)

결과: [1,5,15,20,24,17,35]
      [1,5,15,24,17,35]
```

##### pop() <br/><br/> 서식: 리스트명.pop(인덱스번호)

```python
data = [10,20,30,40,50,60,70,80]
print(data)

x = data.pop(2)     # 인덱스 번호가 2 인 30이 삭제된다
print(x)
print(data)

결과: [10,20,30,40,50,60,70,80]
       30
      [10,20,40,50,60,70,80]
```

##### clear() <br/><br/> 서식: 리스트명.clear()

```python
data = [3,12,7,-3,-9]
print(data)

data.clear()    #리스트 data내에 있는 모든 요소를 삭제
print(data)

결과: [3,12,7,-3,-9]
      []
```

#### 리스트 병합 (+)

##### 서식:리스트명 = 리스트1 + 리스트2 + ....

```python
person1 = ["kim", 23, "kim@naver.com"]
person2 = ["lee", 35, "lee@hanmail.net"]

person = person1 + person2    # 두 리스트 합치기

print(person)

결과:  ['kim', 23, 'kim@naver.com', 'lee', 35, 'lee@hanmail.net']
```

#### 리스트 합계 구하기 ( sum() \*sum은 메소드가 아니라 파이썬의 내장함수 )

```python
scores = [80, 90, 85, 95, 100]

sm = sum(scores)
avg = sm / len(scores)

print("합계:", sm)
print("평균:", avg)

결과:  합계: 450
       평균: 90.0
```

#### 리스트 순서 반대로 하기 ( reverse() )

##### 서식: 리스트명.reverse()

```python
data = [10,20,30,40,50]
print(data)

data.reverse()
print(data)

결과: [10,20,30,40,50]
      [50,40,30,20,10]
```

#### 리스트 복사하기( copy() )

##### 서식: 리스트명.copy()

```python
fruits = ["apple","banana","orange"]
print(fruits)

x = fruits.copy()        # 리스트fruits를 복사하여 새로운 리스트 생성
print(x)

결과: ["apple","banana","orange"]
      ["apple","banana","orange"]
```

#### 리스트 정렬( sort(), sort(reverse=True) )

##### 리스트명.sort()

```python
data = [12, 8, 15, 32, -3, -20, 15, 34, 6]
print(data)

data.sort()      #리스트내의 요소들을 오름차순으로 정렬
print(data)

data.sort(reverse=True)   #리스트내의 요소들을 내림차순으로 정렬
print(data)

결과:  [12, 8, 15, 32, -3, -20, 15, 34, 6]
       [-20, -3, 6, 8, 12, 15, 15, 32, 34]
       [34, 32, 15, 15, 12, 8, 6, -3, -20]
```

### 문자열과 리스트

```
  문자열 메소드  /                      의미
  -----------------------------------------------------------------
  find()     / 문자열에서 특정 문자열을 찾아 위치(인덱스번호)를 구함
  replace()  / 문자열에서 특정 문자열을 다른 문자열로 치환함
  split()    / 특정 문자열을 기준으로 문자열을 쪼개서 리스트에 저장함
  join()     / 리스트의 요소를 하나로 묶어서 문자열로 변환함
```

#### 문자열 찾기( find() )

```python
string1 = "Python is fun!"
print(string1)

x = string1.find("fun")
print(x)

결과: "Python is fun!"
      10
```

#### 문자열 치환하기( replace() )

```python
string1 = "사과는 맛있다. 나는 사과를 제일 좋아한다."
print(string1)

x = string1.replace("사과","딸기") # 문자열"사과"를 "딸기로 치환한다.
print(x)

결과: 사과는 맛있다. 나는 사과를 제일 좋아한다.
      딸기는 맛있다. 나는 딸기를 제일 좋아한다.
```

#### 문자열 쪼개기( split() )

```python
hello = "have a nice day"
print(hello)

list1 = hello.split(" ")
print(list1)
print(type(list1))

for i in range(0, len(list1)):
    print("list1[%d]: %s" % (i, list1[i]))

결과: have a nice day
      ['have', 'a', 'nice', 'day']
      <class 'list'>
      list1[0]: have
      list1[1]: a
      list1[2]: nice
      list1[3]: day
```

#### 리스트 문자열로 변환하기 ( join() )

```python
names = ["황예린", "홍지수", "안지영"]
print(names)

x = "/".join(names)
print(x)

결과: ['황예린', '홍지수', '안지영']
      황예린/홍지수/안지영
```
