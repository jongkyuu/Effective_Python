---
title: "Python - Closure에 대해"
excerpt: "Closure에 대해 알아보자"

categories:
  - Theory
tags:
  - [CSharp, Theory, Exception, Advanced]

toc: true
toc_sticky: true

date: 2021-12-17
last_modified_at: 2021-12-17
---

Closure에 대해 알아보기 전에 필요한 배경지식을 먼저 살펴본다. Closure를 이해하기 위해서는 함수의 중첩, 일급 객체(first-class citizen), 파이썬의 nonlocal scope에 대한 이해가 선행되어야 한다.

<br>

## 함수의 중첩

파이썬에서는 함수의 중첩 선언이 가능하다.

```python
def greetings():
    def say_hello():
        print("Hello!")
    say_hello()

>>> greetings()

Hello!
```

greetings 함수가 내부 함수인 say_hello 함수를 호출하고 있다.

<br>

## 일급 객체(First-Class Citizen)

일급 객체는 OOP에서 사용되는 개념 중 하나로 아래의 조건을 만족하는 객체를 의미한다.

- 변수 혹은 데이터 구조(자료구조) 안에 담을 수 있어야 한다
- 매개변수로 전달할 수 있어야 한다
- 리턴값으로 사용될 수 있어야 한다

우리가 익히 알고 있는 int, str, float, list 타입의 모든 객체는 일급 객체라고 볼 수 있다. 파이썬에서는 함수도 위의 일급 객체 조건을 만족한다. 즉 함수를 변수에 할당할 수 있고, 매개변수로 전달도 가능하고, 리턴값으로 사용할 수 있다. 

```python
def add(a, b):
    retun a + b 

def execute(func, *args):
    return func(*args)  # 리턴값으로 사용

f = add  # 변수에 담음

>>> execute(f, 3, 5)  # 함수의 매개변수로 전달

8
```

## nonlocal

```python
z = 3

def outer(x):
    y = 10
    def inner():
        x = 1000
        return x

    return inner()

>>> print(outer(10))

1000
```

inner 함수의 입장에서 scope를 살펴보자
- inner 함수 블록 안에 있는 영역은 local 스코프라고 불린다. 로컬 영역 안의 모든 개체들은 inner의 제어 아래에 있다.
- inner 함수 밖에, outer 함수 안에 있는 영역은 nonlocal 스코프로 불린다. outer의 변수 y는 inner 입장에서 nonlocal 스코프의 변수이다.
- outer 함수 밖의 영역은 global 스코프이다. z변수는 global 스코에 선언된 변수로 outer 함수 뿐 아니라 다른 코드나 함수에서도 참조 가능하다.

이렇게 global, nonlocal, local 스코프를 구분해서 각 스코프는 자신의 영역에 최대한 관심을 가지고, 다른 영역의 변수나 객체에 대해서는 제한적인 제어를 가지게 된다.

따라서 inner 함수는 local 스코프에서 x를 찾았기 때문에 외부 스코프 영역을 찾아보지 않고 1000을 리턴한다.


내부 스코프의 변수는 외부 스코프의 변수에 대해 읽기는 문제없이 가능하지만 쓰기는 제한적이다. 아래 예제를 보자.

```python
def count(x):
    def read_value():
        print(x)
    read_value()

def count2(x):
    def write_value():
        x += 1
        print(x)
    write_value()

>>> count(5)

5

>>> count2(5)

UnboundLocalError: local variable 'x' referenced before assignment
```

위의 예제에서 read_value 내부함수는 nonlocal 영역의 변수 x를 출력하고 있다. 외부 스코프의 변수에 대해 읽기는 문제없이 가능하다.

하지만 write_value 내부함수를 실행하면 UnboundLocalError가 발생한다. local 변수 x가 할당되기 전에 참조되었다는 의미로 local 영역에는 x라는 변수가 없는데 거기다 1을 더했기 때문에 발생한 에러이다. 

파이썬에서는 값을 수정하거나 쓸때는 기본적으로 local 변수에 대해서만 가능하다. 함수에서 외부의 변수를 함부로 건드리면 버그가 발생하기 쉽기 때문이다. 내부 함수 수십개가 count함수의 상태값을 수정한다면 예상하지 못한 결과를 초래할 수 있다. 따라서 local 영역에서 밖의 영역에 대한 값을 참조하는 것은 가능하지만 쓰는것은 제한하고 있는 것이다.

만약 의도적으로 nonlocal 스코프의 값을 수정하고 싶으면 nonlocal statement를 사용하면 된다. global 스코프의 값을 제어하고 싶다면 global statement를 사용하면 된다.

```python
def count2(x):
    def write_value():
        nonlocal x  # x가 nonlocal 변수임을 선언
        x += 1
        print(x)
    write_value()

>>> count2(5)

6

```


## Closure

파이썬에서 클로저는 ‘자신을 둘러싼 스코프(네임스페이스)의 상태값을 기억하는 함수’다. 어떤 함수의 내부 함수가 외부 함수의 변수(*프리변수)를 참조할 때, 외부 함수가 종료된 후에도 내부 함수가 외부 함수의 변수를 참조할 수 있도록 어딘가에 저장하는 함수를 의미한다. 

프리변수(free variable) : 어떤 함수에서 사용되지만 그 함수 내부에서 선언되지 않는 변수를 의미

그리고 어떤 함수가 클로저이기 위해서는 다음의 세 가지 조건을 만족해야 한다.

- 해당 함수는 어떤 함수 내의 중첩된 함수여야 한다.
- 해당 함수는 자신을 둘러싼(enclose) 함수 내의 상태값을 참조해야 한다.
- 외부함수가 내부함수를 반환해야 한다.

```python
def hello(msg):
    message = "Hi, " + msg

    def say():
        print(message)

    return say

f = hello("Dear")

>>> f()

Hi, Dear
```

hello 함수는 매개변수로 msg를 받아 message라는 변수에 문자열로 저장하고 say 함수를(함수 자체를) 리턴한다. 내부함수인 say는 nonlocal 변수인 message를 출력해준다. 여기서 say 함수가 클로저의 조건을 모두 만족한다는 사실을 알수 있다.

- 어떤 함수 내의 중첩된 함수 : say 함수는 hello 함수의 내부함수
- 둘러싼(enclose) 함수 내의 상태값을 참조 : nonlocal 스코프의 message 변수 참조
- 외부함수가 내부함수를 반환 : hello 함수는 say 함수를 리턴

hello함수를 "Dear"라는 문자열을 매개변수로 전달해서 실행한 결과를 f 변수에 저장하고 f를 실행하면 "Hi, Dear" 문자열을 출력한다. 이 과정을 살펴보면 아래와 같다.

1. hello함수에 "Fox"를 매개변수값으로 넘겨주며 실행
2. message변수에 매개변수를 이용해 "Hi, Fox"라는 문자열을 저장
3. say함수가 message변수를 참조
4. say함수 리턴
5. f변수가 say함수를 참조
6. f변수 실행(say함수 실행)
7. f변수는 message변수를 출력

그런데 4번 단계에서 hello함수는 종료되고 메모리에서도 삭제되어서 hello 함수의 변수인 message도 함께 삭제외었을텐데 f 함수를 실행하면 message 변수가 출력되는 것이 이상하다.

이것이 가능한 이유는 클러저 때문이다. 중첩 함수인 say가 외부 함수인 hello의 변수 message를 참조하기에 message변수와 say의 환경을 저장하는 클로저가 동적으로 생성되었고 f가 실행될때는 해당 클로저를 참조하여 message값을 출력할 수 있는 것입니다.

이 클로저는 f변수에 say함수가 할당될 때 생성됩니다.


### 클로저의 위치

```python
## 함수 선언
def hello(msg):
    message = "Hi, " + msg

    def say():
        print(message)

    return say

f = hello("Dear")

>>> print(dir(f))  # f 객체가 가지고 있는 메소드와 변수 확인

['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', 
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__',
 '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', 
'__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__']

>>> print(type(f.__closure__))   # __closure__ 타입 확인
<class 'tuple'>      # __closure__는 튜플로 클로저가 enclosing 스코프에서 참조하는 변수들을 담고 있다. 

>>> print(f.__closure__)   # __closure__ 프린트
(<cell at 0x00000282C2A844F8: str object at 0x00000282C3183F30>,)


>>> print(dir(f.__closure__[0]))   # __closure__ 객체가 가지고 있는 메소드와 변수 확인
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
 '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']

>>> print(f.__closure__[0].cell_contents)  # 각 원소의 cell_contents 는 그 값 자체를 갖고 있다
Hi, Dear

```

클로저에서 자신 안에 정의된 내부 변수가 아닌, Enclosing하고 있는 변수에 접근하는 것을 파이썬에서 지원하고 있다. 파이썬 3 기준으로, 클로저 함수는 \_\_closure\_\_ 변수를 자동으로 갖고 있다. 이 변수는 튜플 타입으로서 클로저가 enclosing 스코프에서 참조하는 변수들을 담고 있다. 그리고 각 원소의 cell_contents 는 그 값 자체를 갖고 있다.

클로저가 생성될 때 \_\_closure\_\_ 변수가 같이 생성되고 유지되기 때문에 기존 함수가 삭제되어도 문제없이 클로저를 실행할 수 있다.

## Closure 사용의 장점 

- 관리와 책임을 명확히 할 수 있고
- 각 변수가 섞여 불필요한 충돌을 방지할 수 있으며
- 사용환경(context)에 맞게 임의대로 내부구조를 조정할 수 있다.

> (장점에 대해 좀더 고민해보기..)


## 참조

- https://shoark7.github.io/programming/python/closure-in-python
- https://tibetsandfox.tistory.com/9