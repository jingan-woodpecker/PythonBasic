1、类的定义

    格式如下
    
    class 类名:
    
        方法列表
        
```python
# 定义一个类
class Person():
	#具有相同属性和行为的对象可以抽象出一个类,人可以休息/工作就是相同属性
    def sleep(self):
        print("人类可以休息")

    def work(self):
        print("人类可以工作")
```

    说明：

    定义类时有2种：新式类和经典类，上面的Car为经典类，如果是Car(object)则为新式类
    类名 的命名规则按照"大驼峰"

2、创建对象：定义了类之后要想使用，则需要创建对象，创建之后一定有一块空间存放对象的数据信息

    创建对象的格式为:
        
        对象名 = 类名()
        
```python
# 定义一个类
class Person():

    def sleep(self):
        print("人类可以休息")

    def work(self):
        print("人类可以工作")

    def info(self):
        #注意类的方法中不要忘记添加self(self.name)
        print("我的姓名叫%s,今年%s岁了"%(self.name , self.age))

# 构建一个对象,并用p1进行接收
p1 = Person()
#再次构建一个对象,不同的对象同属于一个类
p2 = Person()

#调用对象的方法
p1.sleep()

#给对象添加属性,可以定义多个属性
p1.name = "xiao zhu"
p1.age = 23

p1.info()
```

    总结：

    p1 = Person()，这样就产生了一个Person的实例对象，此时也可以通过实例对象p1来访问属性或者方法
    第一次使用p1.name = "xiao zhu"表示给p1这个对象添加属性，如果后面再次出现p1.name = xxx表示对属性进行修改
    
    p1是一个对象，它拥有属性（数据）和方法（函数）
    当创建一个对象时，就是用一个模子，来制造一个实物
    
3、理解self

    self表示：调用这个方法本身的对象
        比如：上述的p1.Person()其中p1就表示这个self
        
```python
# 定义一个类
class Animal:

    # 方法
    def __init__(self, name):
        self.name = name

    def printName(self):
        print('名字为:%s'%self.name)

# 定义一个函数
def myPrint(animal):
    animal.printName()


dog1 = Animal('西西')
myPrint(dog1)

dog2 = Animal('北北')
myPrint(dog2)
```

    总结

    所谓的self，可以理解为自己
    可以把self当做C++中类里面的this指针一样理解，就是对象自身的意思
    某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可


