## 튜플

### 튜플과 리스트는 매우 유사하다. 하지만 차이점은

#### 1. 튜플에서는 리스트의 대괄호[] 대신 소괄호 사용()

#### 2. 튜플에서는 요소의 수정과 추가가 불가능하다.

### 튜플 생성하기:

#### 기본서식: 튜플명 = (데이터,데이터,데이터,...)

```python
animals = ("토끼", "거북이", "사자", "여우")  #튜플 aniamls 생성

numbers = tuple(range(10))    #tuple(을 이용한 튜플 생성)

결과: ("토끼", "거북이", "사자", "여우")
      (0,1,2,3,4,5,6,7,8,9)
```

### 튜플 요소 추출:

```python
n = (10,11,12,13,14,15,16,17,18,19,20)

n[0]     #n의 0번째 요소
n[2:5]   #n의 2번째부터 5번째까지의 요소
n[2:]    #n의 2번째부터 끝까지의 요소
n[:5]    #n의 처음부터 5번째까지의 요소
n[-2]    #n의 뒤에서부터 2번째 요소
n[::-1]  #n의 순서가 반대로
```

#### 튜플 길이는 len() 함수를 이용해서 구한다.

```python
tuple1 = (10,20,30,40,50)
len(tuple1)

결과: 5
```

#### 튜플 병합은 +기호를 이용한다.

```python
tuple1 = (10,20,30)
tuple2 = (40,50,60)
tuple3 = tuple1 + tuple2

결과: (10,20,30,40,50,60)
```

## 딕셔너리

#### 딕셔너리는 자료를 찾는 인덱스를 의미하는 키(key)와 자료의 내용인 값(value)을 이용하여 데이터를 관리한다.

#### 딕셔너리는 중괄호로 감싼다.

```python
score = {"kor":90, "eng":89, "math":95}
          =키  =값   =키 =값   =키  =값
```

### 딕셔너리 생성하기

#### 기본서식: 딕셔너리 = {키:값, 키:값, 키:값,...}

```python
member = {"name": "황예린", "age":22, "email":"yerin@hanmail.net"}

score = dict([("국어",80), ("영어",90), ("수학",100)])  #dict()함수 사용

결과:  {"name": "황예린", "age":22, "email":"yerin@hanmail.net"}
       {"국어":80, "영어":90, "수학":100}
```

### 딕셔너리 요소 추출

```python
user = {"id":"kim55", "name":"강성준", "level":7, "point":10000}

print(user)          #딕셔너리 전체 출력
print(user["id"])    #"id" 키의 값을 출력
print(user["name"])  #"name" 키의 값 출력
print(user["point"]) #"point" 키의 값 출력
```

### 딕셔너리 요소 변환:

#### 딕셔너리 요소 추가

```python
scores = {"kor":90, "eng":89, "math":98}
scores["music"] = 100    #"music":100 추가

결과: {"kor":90, "eng":89, "math":98, "music":100}
```

#### 딕셔너리 요소 수정

##### 기본 서식: 딕셔너리[키] = 값

```python
words = {"door": "문", "chair": "의자", "table": "책상", "house": "집"}
print(words)

words["table"] = "테이블"    #"table"키의 요소를 "테이블"로 변경
print(words)

words["house"] = "히우스"    #"house"키의 요소를 "하우스"로 변경
print(words)

결과: {'door':'문', 'chair':'의자', 'table':'책상', 'house':'집'}
{'door':'문', 'chair':'의자', 'table':'테이블', 'house':'집'}
{'door':'문', 'chair':'의자', 'table':'테이블', 'house':'히우스'}
```

#### 딕셔너리 요소 삭제

#### pop() 메소드나 clear() 메소드 사용

#### pop():

```python
car = {"brand": "현대", "model": "아반떼", "start": "1990", "year": 2021}

x = car.pop("start")   #"start" 요소 추출과 동시에 해당 요소 삭제

print(car)

결과: {'brand':'현대', 'model':'아반떼', 'start':'1990', 'year':2021}
{'brand': '현대', 'model': '아반떼', 'year': 2021}
```

#### clear()

```python
car = {"brand": "현대", "model": "아반떼", "start": "1990", "year": 2021}
print(car)

car.clear()
print(car)

결과: {'brand':'현대', 'model':'아반떼', 'start':'1990', 'year':2021}
{}
```
