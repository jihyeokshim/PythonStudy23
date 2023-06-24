### 비교 연산자: >,<,==,!=,<=,>=

### 논리 연산자: and,or,not

```python
* 조건1 "and" 조건2: 조건1과 조건2가 둘다 참인 경우에만 참이된다.
* 조건1 "or" 조건2: 조건1 또는 조건2 중 하나만 참이어도 참이 된다.
* not 조건: 조건이 참이면거짓, 고짓이면 참으로 해서 논리값을 반대로 변경하다.
```

### AND:

```
 연산자 "and": >>>score1 = 75
               >>>score2 = 90
               >>>score1>=80 and score2>=80
결과:false 첫 번째조건인 score1이 거짓이기 때문에
```

### OR

```
연산자 "or": >>> x=10
             >>> x%2 == 0 or x%6 == 0
결과: True 두조건 중 x%2는 참이기 때문에 결과도 참
```

### Not

```
연산자:"not": >>> x=25
              >>> not x%2 == 0
결과: true 조건 x%2는 거짓이기 때문에 결과는 참이다.
```

### if~구문:

#### if 조건식:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장1:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장2:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...

#### ex.

```python
age = int(input("나이는?"))
ticket = 2000

if age>= 65:
    ticket = 0
```

### if ~ else 구문:

#### if 조건식:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장1

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장2

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...
