1、类的数据可以隐藏(数据私有化)的原理

    a xx: 共有变量
    b _x: 单前置下划线：私有属性或方法
    c __xx: 双前置下划线：避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
    d __xx__: 双前后下划线： 用户名字空间的魔法对象或属性
    e xx_: 单后置下划线： 用于避免python关键字的冲突

类的私有属性直接创建对象访问会直接报错    
```python
class TestClass(object):
    def __init__(self):
        self.__num = 100

t = TestClass()
print(t.__num)

'''
AttributeError: 'TestClass' object has no attribute '__num'
'''
```  
dir()可以查看对象中都有哪些属性和哪些方法

```python
import pprint
class TestClass(object):
    def __init__(self):
        self.__num = 100

t = TestClass()
pprint.pprint(dir(t))

'''
['_TestClass__num',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
'''
```

    查看上述打印结果的列表中的第一个"'_TestClass__num'"，如果是私有的就会将原本的"__num"
    前面添加下划线和类名"_TestClass",这就称为“名字重整”，所以就有隐藏作用，直接访问是访问不到的。

2、为私有属性添加getter和setter方法(防意识方法)
    
    所有成员变量都设置成私有的，比如设置一个类Person()里面有一个变量为年龄age按照正常情况是从1到100岁，如果不是私有的，被设置为负数，或者大于100，
    显然不合理，所以不允许属性被随意设置；如果要设置可以使用getter()和setter()方法，进行一些判断的逻辑进行限制，再被调用，就可以防止被随意设置。
 
```python
class TestClass(object):
    def __init__(self):
        self.__num = 100

    def getNum(self):
        return self.__num

    def setNum(self , num):
        if num < 100:
            self.__num = num

t = TestClass()
t.setNum(30)
print(t.getNum())
#30
```

2、property的使用

    上述的方式相对繁琐：需要获取的时候，必须调用getter方法，设置的时候，必须调用setter方法
    可以使用property升级getter和setter方法
    将getter和setter方法，放入到一个变量中
    
````python
class TestClass(object):
    def __init__(self):
        self.__num = 100

    def getNum(self):
        return self.__num

    def setNum(self , num):
        if num < 100:
            self.__num = num

    #解释器会自动判断什么时候调用getter,什么时候调用getter
    num = property(getNum , setNum)

t = TestClass()
t.num = 30
print(t.num)
````

property另一种简化的方式： 使用修饰器，且方法名和属性名一致

```python
class TestClass(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):  #方法名num和属性名要一致
        return self.__num

    @num.setter
    def num(self , num):
        if num < 100:
            self.__num = num

t = TestClass()
t.num = 30
print(t.num)
```