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

#### else:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장A

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장B

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...

#### ex.

```python
x = int(input("숫자를 입려하세요."))

if x%2 == 0:
   print("x는 짝수이다.")
else:
   print("x는 홀수이다.")
```

### if ~ elif~ else~ 구문:

#### if 조건식:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장1

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장2

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...

#### elif 조건식:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장A

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장B

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...

#### else 조건식:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장i

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;문장ii

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...

#### ex.

```python
number = int(input("숫자를 입력하세요."))

if number > 0
    print("%d는양수이다." %number)
elif number < 0
    print("%d는 음수이다." %number)
else number == 0
    print("%d는 0이다." %number)
```

### if문의 중첩

#### if문의 중첩은 and 와 비슷하게 작용하지만, 두개이상의 변수가 있을때 쓰는양을 줄여준다.

### if문 중첩:

#### 수학 90 국어90 A+

#### 수학 90 국어 80 A-

#### if score >= 90:

#### if score2 >=90:

#### grade = "A+"

#### elif score2 >= 80:

#### grade = "A-"

### and 문

#### 수학 90 국어90 A+

#### 수학 90 국어 80 A-
