#创建案例
#创建Student类，描述学生类
#学生具有Student.name属性
#但name格式并不统一
#可以增加一个函数，

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #介绍自己
    def intro(self):
        print("hi,my name is {0}".format(self.name))

    def setname(self):
        self.name = name.super()

s1 = Student("zqc",20)
s1.intro()

#property案例
# 定义一个person类，具有name，age属性
#对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，用整数保存
# x=property(fget,fset,fdel,doc)
class Person():
    def fget(self):
        return self._name * 2

    def fset(self,name):
        self._name = "NOName"

    def fdel(self):
        self._name = "NoName"
    name = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
print(p1.name)    #触发fget
p1.name = "zqc"   #触发fset
del p1.name       #触发fdel

# __getattr__

class A():
    name = "NoName"
    age = 18

    def __getattr__(self, name):
        print("没找到呀没找到")
        print(name)

a = A()
print(a.name)
print(a.addr)
# 作业：
# 为什么会打印第四句话，而且第四句话是打印的 None

# __setattr__案例
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性： {0}".format(name))
        # 下面语句会导致问题，死循环
        # self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name, value)


p = Person()
print(p.__dict__)
p.age = 18


# __gt__

class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print("哈哈， {0} 会比 {1} 大吗？".format(self, obj))
        return self._name > obj._name


# 作业：
# 字符串的比较是按什么规则
stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)

# 作业：
# 下面显示结果不太美观，能否改成形如  "哈哈， one 会比 two 大吗？“


# 三种方法的案例
class Person:
    # 实例方法
    def eat(self):
        print(self)
        print("Eating.....")

    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.....")

    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying....")


yueyue = Person()

# 实例方法
yueyue.eat()
# 类方法
Person.play()
yueyue.play()
# 静态方法
Person.say()
yueyue.say()

# 作业：
# 自行查找三种方法内存使用方面的区别

#抽象

class Animal():
    def sayHello(self):
        pass
class Dog(Animal):
    def  sayHello(self):
        print("闻一下对方")

class Person(Animal):
    def  sayHello(self):
        print("稳一下对方")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()

#抽象类的实现
import abc
#声明一个类并且指定当前类的元类
class Human(metaclass=abc,ABCMeta):
    #定义一个抽象的方法
    @ abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @ abc.abstractclassmethod
    def drink():
        pass
    #定义静态抽象方法
    @ abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("I'm sleeping……")

#函数名可以当变量来用
def sayHelllo(name):
    print("{0}您好".format(name))

sayHelllo("月月")

liuyang = sayHelllo
liuyang("月月")

#组合类例子1
# 自己定义一个类
class A():
    pass
def say(self):
    print("saying....")
say(9)
A.say = say

a = A()
a.say()

# 组合类例子 2
# 自己组装一个类
from types import MethodType
class A():
    pass
def say(self):
    print("Saying......")

a = A()
a.say = MethodType(say,A)
a.say()

# 利用type造一个类

# 先定义类应该具有的成员函数
def say(self):
    print("say......")
def talk(self):
    print("talking.....")

A = type("AName",(object,),{"class.say":say,"class.talk":talk})
a = A()
a.class_say()
a.class_talk()

#元类演示
#元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass结尾
class ZqcMetaClass(type):
    # 注意以下写法
    def __new__(cls,name,bases,attrs):
        print("哈哈，我是元类啊")
        attrs['id'] = '0000'
        return type.__new__(cls,name,bases,attrs)

#元类定义完就可以使用
class Teacher(object,metaclass=ZqcMetaClass):
    pass
t = Teacher()
t.id