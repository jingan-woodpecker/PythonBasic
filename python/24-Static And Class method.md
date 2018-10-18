1、类方法

    是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
    （当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。
    
```python
class People(object):

    address = "Guangdong"

    #类方法，用@classmethod修饰
    @classmethod
    def get_address(cls):
        #改变类属性
        cls.address = "shenzhen"
        return cls.address

p = People()
#通过实例对象引用
print(p.get_address())
#通过类对象引用
print(People.get_address())
```

2、静态方法

    需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数(即没有默认传递的参数)
    
```python
class People(object):

    address = "Guangdong"

    #静态方法，用@staticmethod修饰
    @staticmethod
    def get_address():
        #通过类名该变类属性
        People.address = "BeiJing"
        return People.address

#通过类对象引用
print(People.get_address())
```

    总结

    从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
    而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名
    称的类属性和实例属性的情况下，实例属性优先级更高。静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用