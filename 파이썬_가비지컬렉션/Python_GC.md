## 파이썬의 메모리 관리

- 파이썬은 C 또는 C++과 같이 프로그래머가 직접 메모리를 관리하지 않고 레퍼런스 카운트(Reference Counts)와 가비지 콜렉션(Automatic Garbage Collection)에 의해 관리됩니다.

### 레퍼런스 카운트(Reference Counts)

- 파이썬은 내부적으로 malloc()와 free()를 많이 사용하기 때문에 메모리 누수의 위험이 있습니다.
  - c언어에서 malloc 함수로 사용할 메모리 공간 확보.
    - malloc 함수는 힙(heap) 부분의 메모리를 사용
    - 스택에 생성된 변수는 사용한 뒤 따로 처리를 해주지 않아도 되지만 malloc 함수를 사용하여 힙에서 할당한 메모리는 반드시 해제를 해주어야 함
  - free 함수로 동적으로 할당한 메모리 해제
  - 메모리를 할당만 하고 해제를 해주지 않으면 메모리 누수(memory leak) 발생
- 이런 이슈가 있기 때문에 파이썬은 메모리를 관리하기 위한 전략으로 레퍼런스 카운트를 사용합니다.

레퍼런스 카운트 전략이란 파이썬의 모든 객체에 카운트를 포함하고, 이 카운트는 객체가 참조될 때 증가하고, 참조가 삭제될 때 감소시키는 방식으로 작동됩니다. 이때 카운터가 0이 되면 메모리가 할당이 삭제됩니다.

```python
import sys

class RefenceCountTest():
    def __init__(self):
        print('create object')


a = RefenceCountTest()
print(f'count {sys.getrefcount(a)}')
b = a
print(f'count {sys.getrefcount(a)}')
c = a
print(f'count {sys.getrefcount(a)}')
c = 0
print(f'count {sys.getrefcount(a)}')
b = 0
print(f'count {sys.getrefcount(a)}')

"""
OUT PUT:
count 2
count 3
count 4
count 3
count 2
"""
```

- RefenceCountTest 객체를 생성해서 a에 할당한 뒤 a 객체의 레퍼런스 카운트를 확인해보면 2가 출력되는것을 볼 수 있습니다.
- getrefcount()의 파라미터값으로 a가 임시 참조되었기 때문에 1이 아닌 2가 출력됩니다.
- 첫 번째 출력 이후 b, c에 각각 참조될 때 마다 1씩 증가하는 걸 확인할 수 있습니다. 그리고 b, c에 0이 할당될 때 1씩 감소하는 것을 확인할 수 있습니다.
- 파이썬에서는 이런 동작이 Py_INCREF와 Py_DECREF을 통해 구현되어 있습니다.(Python Doc)
  - 코드는 [cpython/object.h](https://github.com/python/cpython/blob/main/Include/object.h)를 참고
  - PyObject에서 ob_refcnt(레퍼런스 카운트) 프로퍼티를 가지고 있습니다. 그리고 Py_INCREF에서 증가시키고, Py_DECREF에서 감소시킨 후 ob_refcnt가 0일 때 메모리를 할당을 삭제하는 Py_Dealloc를 실행합니다.
- 파이썬은 레퍼런스 카운트를 통해 메모리를 관리합니다. 하지만 레퍼런스 카운트만으로 메모리를 관리했을 때 약점이 있습니다.

### 순환 참조

- 순환 참조란 간단하게 컨테이너 객체가 자기 자신을 참조하는 것을 말합니다. 자기 자신이 참조될 때 프로그래머는 할당된 객체를 추적하기 어려워지고, 이때 메모리 누수가 발생할 수 있습니다

```python
class RefenceCountTest():
    def __init__(self):
        print('create object')
    def __del__(self):
        print(f'destroy {id(self)}')

a = RefenceCountTest()
a = 0
print('end .....')

"""
OUT PUT:
create object
destroy 1845296687376
end .....
"""
```

- `__del__()`은 메모리 할당이 삭제되는 시점에 실행되는 메소드입니다.
- a 변수에 0을 재할당할 때 `__del__()`이 실행됩니다.

```python
# me 프로퍼티에 자기 자신을 할당합니다.
class RefenceCountTest():
  def __init__(self):
    print('create object')
    self.me = self
  def __del__(self):
    print(f'destroy {id(self)}')

a = RefenceCountTest()
a = 0
print('end .....')

"""
OUT PUT:
create object
end .....
destroy 1723515726288
"""
```

- 하지만 순환 참조가 될 때는 위 코드처럼 출력됩니다.
- 위 코드는 이전과 다르게 ‘end …..’를 출력하고 `__del__()`이 실행되는 걸 확인할 수 있습니다.
- a 변수에 새로운 값을 할당해도 a.me가 자기 자신을 참조하고 있어 레퍼런스 카운트가 남아있기 때문에 이런 현상이 발생합니다.
- 이렇게 되면 레퍼런스 카운트가 0에 도달할 수 없고 할당된 메모리를 삭제할 수 없어 메모리 누수가 발생합니다.
- 파이썬은 이 문제를 **가비지 컬렉션**으로 해결합니다.

### 가비지 컬렉션(garbage collection)

- 파이썬의 gc 모듈을 통해 가비지 컬렉터를 직접 제어할 수 있다.
- gc 모듈은 cyclic garbage collection을 지원하는데 이를 통해 reference cycles(순환 참조)를 해결할 수 있다.
- gc모듈은 오로지 순환 참조를 탐지하고 해결하기 위해 존재한다. gc 파이썬 공식문서에서도 순환 참조를 만들지 않는다고 확신할 수 있으면 gc.disable()을 통해 garbage collector를 비활성화시켜도 된다고 언급하고 있다.

- 가비지 컬렉터는 내부적으로 generation(세대)과 threshold(임계값)로 가비지 컬렉션 주기와 객체를 관리한다.
- 세대는 0세대, 1세대, 2세대로 구분되는데 최근에 생성된 객체는 0세대(young)에 들어가고 오래된 객체일수록 2세대(old)에 존재한다.
- 더불어 한 객체는 단 하나의 세대에만 속한다. 가비지 컬렉터는 0세대일수록 더 자주 가비지 컬렉션을 하도록 설계되었는데 이는 [generational hypothesis](https://www.memorymanagement.org/glossary/g.html#term-generational-hypothesis)에 근거한다.
  - generational hypothesis의 두 가지 가설
    - 대부분의 객체는 금방 도달할 수 없는 상태(unreachable)가 됨
    - 오래된 객체(old)에서 젊은 객체(young)로의 참조는 아주 적게 존재함

<br>

- 주기는 threshold와 관련 있는데 gc.get_threshold()로 확인해 볼 수 있다.

```
>>> gc.get_count()
(304, 8, 6)
>>> gc.get_threshold()
(700, 10, 10)
```

- gc.get_count()에서 나온 수치는 세대별 객체의 count를 의미한다.
- gc.get_threshold()에서 나온 수치는 GC를 수행하는 임계점이다. 각각 threshold 0, threshold 1, threshold 2를 의미하는데 n세대에 객체를 할당한 횟수가 threshold n을 초과하면 가비지 컬렉션이 수행되며 이 값은 변경될 수 있다.
- 0세대의 경우 메모리에 객체가 할당된 횟수에서 해제된 횟수를 뺀 값, 즉 객체 수가 threshold 0을 초과하면 실행된다.
- 다만 그 이후 세대부터는 조금 다른데 0세대 가비지 컬렉션이 일어난 후 0세대 객체를 1세대로 이동시킨 후 카운터를 1 증가시킨다.
- 이 1세대 카운터가 threshold 1을 초과하면 그때 1세대 가비지 컬렉션이 일어난다.
  - [gcmodule.c 코드](https://github.com/python/cpython/blob/main/Modules/gcmodule.c#L832-L836)

### 가비지 컬렉터가 어떻게 순환 참조를 발견하는지?

- 새로운 객체가 만들어질때 파이썬은 객체를 메모리와 0세대에 할당한다. 만약 0세대의 객체 수가 threshold 0보다 크면 collect_generations()를 실행한다.
- collect_generations() 메서드가 호출되면 모든 세대(기본적으로 3개의 세대)를 검사하는데 가장 오래된 세대(2세대)부터 역으로 확인한다. 해당 세대에 객체가 할당된 횟수가 각 세대에 대응되는 threshold n보다 크면 collect()를 호출해 가비지 컬렉션을 수행한다.
- collect() 메서드는 순환 참조 탐지 알고리즘을 수행하고 특정 세대에서 도달할 수 있는 객체(reachable)와 도달할 수 없는 객체(unreachable)를 구분하고 도달할 수 없는 객체 집합을 찾는다. 도달할 수 있는 객체 집합은 다음 상위 세대로 합쳐지고(0세대에서 수행되었으면 1세대로 이동), 도달할 수 없는 객체 집합은 콜백을 수행한 후 메모리에서 해제된다.
  - 이 과정은 먼저 레퍼런스 카운트(RC)를 gc_refs에 복사합니다.
    - 그리고 객체에서 참조하고 있는 다른 컨테이너 객체를 찾아 참조되고 있는 컨테이너 객체의 gc_refs를 감소시킵니다. (TIP. 순환 참조는 컨테이너 객체에서 발생할 수 있는 이슈입니다)
    - 즉, 다른 컨테이너 객체에 참조되고 있는 수 A와 현재 레퍼런스 카운트 B를 빼서 B - A > 0 일 경우 도달 가능한 객체(reachable)가 되고, 0 일 때 도달할 수 없는 객체(unreachable)로 분류합니다.
    - 이후 도달 가능한 객체들은 다음 세대 리스트와 병합되고, 도달할 수 없는 객체들은 메모리에서 제거됩니다. 이런 메커니즘을 순환 참조 알고리즘이라고 합니다.
