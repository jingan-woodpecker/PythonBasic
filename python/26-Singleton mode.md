单例模式

    举个常见的单例模式例子，我们日常使用的电脑上都有一个回收站，在整个操作系统中，回收站只能有一个
    实例，整个系统都使用这个唯一的实例，而且回收站自行提供自己的实例。因此回收站是单例模式的应用。
    
    确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。
    
* 通过类方法来保证创建的对象是唯一的

```python
class User(object):

    __instance = None
    def __init__(self , name):
        self.name = name

    @classmethod
    def get_instance(cls , name):
        if not cls.__instance:
            cls.__instance = User(name)
        return cls.__instance

#这样调用最后的结果都是"lisi",原因是第一次进入判断初始化"lisi"后
#再次将"wangwu"输入后，if的条件就不是None了，所以还是"lisi"
u1 = User.get_instance("lisi")
u2 = User.get_instance("wangwu")

print(u1==u2)
print(id(u1),id(u2))
'''
True
39419408 39419408
'''
```

* 用__new__()方法创建单例模式，保证一个对象

```python
class User(object):

    __instance = None
    def __init__(self , name):
        self.name = name

    def __new__(cls, name):
        if not cls.__instance:
            #创建当前类的对象，并赋值给类属性__instance
            cls.__instance=object.__new__(cls )
        return cls.__instance

u1 = User("lisi")
u2 = User("wangwu")
#因为第二次new后，然后初始化后self变成了wangwu，所以两个结果都是"wangwu"
#都同时指向一个对象，只是值改变了
print(u1.name, u2.name)
print(u1==u2)
print(id(u1),id(u2))
```