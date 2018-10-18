工厂模式：给系统带来更大的可扩展性和尽量少的修改

    解决依赖关系，找第三方 ，创建一个工厂方法来提供实例
    
```python
class Person(object):
    def __init__(self , name):
        self.name = name

    def work(self , axe_type):
        print(self.name+"开始工作了")
        # create_axe为静态方法可以直接调用
        axe = Factory.creat_axe(axe_type)
        axe.cut_tree()

class Axe(object):
    def __init__(self, name):
        self.name = name

    def cut_tree(self):
        print("%s斧头开始砍树"%self.name)

class StoneAxe(Axe):

    def cut_tree(self):
        print("使用石斧来砍树")

class SteelAxe(Axe):

    def cut_tree(self):
        print("使用钢斧来砍树")

#工厂类
class Factory(object):

    #生产斧头，根据用户指定的类型来生产
    @staticmethod
    def creat_axe(type):
        if type == "stone":
            return StoneAxe("花岗岩斧头")
        elif type == "steel":
            return  SteelAxe("加爵斧头")
        else:
            print("传入的类型不正确")

p = Person("小西")
p.work("steel")
'''
小西开始工作了
使用钢斧来砍树
'''
```

当买车时，有很多种品牌可以选择，比如北京现代、别克、凯迪拉克、特斯拉等，那么此时该怎样进行设计呢？

```python
# 定义一个基本的4S店类
class CarStore(object):

    #仅仅是定义了有这个方法，并没有实现，具体功能，这个需要在子类中实现
    def createCar(self, typeName):
        pass

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        self.car = self.createCar(typeName)
        self.car.move()
        self.car.stop()

# 定义一个北京现代4S店类
class XiandaiCarStore(CarStore):

    def createCar(self, typeName):
        self.carFactory = CarFactory()
        return self.carFactory.createCar(typeName)


# 定义伊兰特车类
class YilanteCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义索纳塔车类
class SuonataCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义一个生产汽车的工厂，让其根据具体得订单生产车
class CarFactory(object):

    def createCar(self,typeName):
        self.typeName = typeName
        if self.typeName == "伊兰特":
            self.car = YilanteCar()
        elif self.typeName == "索纳塔":
            self.car = SuonataCar()

        return self.car

suonata = XiandaiCarStore()
suonata.order("索纳塔")    
```

    定义了一个创建对象的接口(可以理解为函数)，但由子类决定要实例化的类是哪一个，工厂方法模式让类的实例化推迟到子类，抽象的CarStore提供了一个创建对象的方法createCar，也叫作工厂方法。

    子类真正实现这个createCar方法创建出具体产品。 创建者类不需要直到实际创建的产品是哪一个，选择了使用了哪个子类，自然也就决定了实际创建的产品是什么。


