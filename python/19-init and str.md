1、__init__()初始化方法: 创建对象的时候，就顺便这个对象的属性给设置了

    * 使用方式
```python
def Class:
    #初始化函数，用来完成一些默认的设定
    def __init__():
        pass
```

    *__init__()方法的调用
    
```python
class Person():

    def __init__(self):
        #封装数据
        self.name = "小竹"
        self.age = 23

    def person_info(self):
        print("输入信息为：")

p1 = Person()
p1.person_info()
print("我的名字叫%s,今年%s岁了"%(p1.name , p1.age))
```

    总结1

    当创建p1对象后，在没有调用__init__()方法的前提下，p1就默认拥有了2个属性name和age，原因是__init__()方法是在创建对象后，就立刻被默认调用了

创建完对象后__init__()方法已经被默认的执行了，可以让对象在调用__init__()方法的时候传递一些参数

```python
class Person():

    def __init__(self , name , age):
        #默认调用__init__()方法，进行封装数据
        self.name = name
        self.age = age

    def person_info(self):
        print("输入信息为：我的名字叫%s,今年%s岁了"%(self.name , self.age))

p1 = Person("王武" , 24)
p1.person_info()
```

总结2

    __init__()方法，在创建一个对象时默认被调用，不需要手动调用
    __init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
    __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去

    把数据封装到对象中
    
    __new__()构造对象的方法
           ------   
        得到了一个对象
           -------
       调用__init__()方法
       
2、__str__()对象转换为字符串的方法，一定需要返回值(return)

    直接打印id()看到的是创建出来的p1对象在内存中的地址
    
```python
class Person():

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return "输入信息为：我的名字叫%s,今年%s岁了"%(self.name , self.age)

    def person_info(self):
        print("输入信息为：我的名字叫%s,今年%s岁了"%(self.name , self.age))

	#上面的两种结果一种是返回数据，一种是打印，注意返回时，不用加print
p1 = Person("王武" , 24)
print(p1)
```

    总结

    在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
    当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据


