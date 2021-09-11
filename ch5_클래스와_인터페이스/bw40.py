

#a = MyChildClass()
#print("a 값 : ", a.value)


class Person:
    def __init__(self):
        print("Person")


class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("Student")


class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        print("Worker")


class PartTimer(Student, Worker):
    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        print("PartTimer")


#a = Person()
#b = Student()
#c = Worker()
d = PartTimer()
print("="*30)


class Person:
    def __init__(self):
        print("Person")


class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student")


class Worker(Person):
    def __init__(self):
        super().__init__()
        print("Worker")


class PartTimer(Student, Worker):
    def __init__(self):
        super().__init__()
        print("PartTimer")


d = PartTimer()
print("="*30)


class MyBaseClass:
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

#a = MyBaseClass(5)
# print("="*30)


class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesTwo:
    def __init__(self):
        self.value *= 2


class PlusFive:
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print('첫 번째 부모 클래스 순서에 따른 값은 (5 * 2) + 5 =', foo.value)
print("="*30)


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = AnotherWay(5)
print('두 번째 부모 클래스 순서에 따른 값은', foo.value)   # 똑같은 결과인 15
print("="*30)


class AnotherWay2(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        PlusFive.__init__(self)
        TimesTwo.__init__(self)


foo = AnotherWay2(5)
print('세 번째 부모 클래스 순서에 따른 값은', foo.value)   # 똑같은 결과인 15
print("="*30)


# 다이아몬드 상속으로 인한 문제
# 다이아몬드 상속이 이뤄지면 공통 조상 클래스의 __init__메서드가 여러번 호출될 수 있기 떄문에 코드가 예기치 않은 방식으로 작동할 수 있다

class MyBaseClass:
    def __init__(self, value):
        self.value = value
        print("MyBaseClass ")
        print("Value : ", self.value)


class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        print("TimesSeven ")
        print("Value : ", self.value)
        self.value *= 7
        print("Value : ", self.value)


class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        print("PlusNine ")
        print("Value : ", self.value)
        self.value += 9
        print("Value : ", self.value)


class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)


foo = ThisWay(5)
print('(5 * 7) + 9 = 44가 나와야 하지만 실제로는', foo.value)
print("="*30)


class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7


class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9


class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)


foo = GoodWay(5)
print('7 * (5 + 9) = 98이 나와야 하고 실제로도', foo.value)
print("="*30)

print(GoodWay.mro())
print("="*30)

#
mro_str = '\n'.join(repr(cls) for cls in GoodWay.mro())
print(mro_str)
print("="*30)
