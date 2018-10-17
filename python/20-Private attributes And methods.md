1、私有属性和方法

    注意：要获得私有属性必须在类中定义一个方法，否则无法获取,私有方法的原理与私有属性一致
    
```python
class GetName():
    def __init__(self , name):
        if len(name) > 6:
            self.__name = name
        else:
            print("名字的长度必须大于6")
            
    #定义一个方法来获取私有属性
    def get_username(self):
        return self.__name

    def __str__(self):
        #获取方法
        self.__say_hello()
        return "姓名为%s"%self.__name
        
    #定义一个私有方法
    def __say_hello(self):
        print(self.__name)

p1 = GetName("liao jingan")
print(p1.get_username())
print(p1)
```

    总结

    Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
    它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

    
 2、__del__()方法(删除指的是删除引用)
 
    创建对象后，python解释器默认调用__init__()方法；

    当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法 
    
```python
import time
class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name


    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)

# 创建对象
dog = Animal("哈皮狗")

# 删除对象
del dog


cat = Animal("波斯猫")
cat2 = cat
cat3 = cat

print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3

print("程序2秒钟后结束")
time.sleep(2)

'''
__init__方法被调用
__del__方法被调用
哈皮狗对象马上被干掉了...
__init__方法被调用
---马上 删除cat对象
---马上 删除cat2对象
---马上 删除cat3对象
__del__方法被调用
波斯猫对象马上被干掉了...
程序2秒钟后结束
'''
```
    * 上述代码中是删除完了cat、cat2、cat3三个对象才调用__del__()方法的
    因为删除第一个cat后，还有引用指向cat2和cat3所以并不会调用__del__()方法进行回收，只有在没有引用的情况下才会调用。