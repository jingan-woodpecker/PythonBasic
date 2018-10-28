1、什么是动态语言？

    动态语言(JS,PHP,Ruby,Python...)：可以在运行的过程中，修改代码
    静态语言(C,C++...)；编译时已经确定好代码，运行过程中不能修改
    
2、为对象动态添加属性

```python
class Person(object):
    def __init__(self, name ,age):
        self.name = name
        self.age = age

P = Person("小竹","22")
#给P对象动态添加sex属性
P.sex = "female"
print(P.sex)
#注意：动态添加的实例属性，只针对特定对象，再次创建新的对象是没有的
# P2 = Person("小王","23")
# print(P2.sex)
#要想所有创建的对象都可以使用动态添加的属性，可以添加类属性
```
3、为类动态添加实例方法
    
    首先导入types模块，然后使用MethodType()添加方法
    注意：第一个参数为要添加的方法的方法名，第二个参数为对象

```python
class Person(object):
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")

def run(self,speed):
    print("%s在移动，速度是%s km/h"%(self.name,speed))

P = Person("小李",22)
#先导入types模块
import types
#使用MethodType()添加方法，第一个参数为要添加的方法的方法名，第二个参数为对象
P.run =types.MethodType(run,P)
P.run(200)
```

4、为类动态添加类方法

```python
class Person(object):
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")

P = Person("小星",19)

@classmethod
def fun1(cls):
    print("classmethod")

#添加fun1类方法到Person中
Person.fun1 = fun1
P.fun1()

#classmethod
```

5、为类动态添加静态方法

```python
class Person(object):
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")

P = Person("小星",19)

@staticmethod
def fun2(a , b):
    return a+b

Person.fun2 = fun2
print(P.fun2(10,20))

#30
```

6、限制类的属性的添加(__slots__)

```python
class student(object):
    __slots__ = ("name","age")

stu = student()
stu.name = "晶晶"
stu.age = 18
#sex属性无法添加
stu.sex = "女生"

'''
stu.sex = "女生"
AttributeError: 'student' object has no attribute 'sex'
'''
```