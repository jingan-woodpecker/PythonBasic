Python基础知识12（对象的方法、组合、继承）

（1）对象的方法: 是描述对象相关的行为的
      #通过定义在类里面的函数
      #初始化方法__init__函数
        
类的方法包括
   #实例方法：每个具体实例相关的方法
    
    class People: #一个类
    'this is people class'
    typePro = 'people'
    def __init__(self, weight = 100):  #初始化方法==构造方法,注意self代表对象本身
        self.weight = weight #其中weight就是实例属性---变量
        print('this is init!')
    def tell(self): #简单来讲self就代表一个实例化方法（self就是t1、t2、t3）
        print('体重：', self.weight)
t1 = People()
t1.tell()

t2 = People(300)
t2.tell()

t3 = People(200)
t3.tell()
#打印结果如下
this is init!
体重： 100
this is init!
体重： 300
this is init!
体重： 200

-----------------------------------------------------------------------------------------
   #静态方法：共有的方法，与每个具体实例无关
    
class People: #一个类
    'this is people class'
    typePro = 'people'
    def __init__(self, weight = 100):  #初始化方法==构造方法,注意self代表对象本身
        self.weight = weight #其中weight就是实例属性---变量
        print('this is init!')
    def tell(self): #简单来讲self就代表一个实例化方法（self就是t1、t2、t3）
        print('体重：', self.weight)
        
    #静态方法通过装饰器@staticmethod来定义（不需要传入self这样的参数，描述的是类所共有的方法）
    @staticmethod
    def classTell():
        print('静态方法')
t1 = People()
t1.tell() #实例方法【这样写的方式是一样的：People.tell(t1)】
t1.classTell() #静态方法

People.classTell() #静态方法属于类的，所以可以调用。实例方法只能通过实例调用

#打印结果如下
this is init!
体重： 100
静态方法
静态方法

--------------------------------------------------------------------------------------------------

（2）对象的组合
现实世界中的对象可以是大对象里面有小对象，同样OOD里面对象也可以是相互组合的
   #通过对象的属性表示这种组合关系
   #在类定义的初始化函数里面表示对象的组合关系
class Room:
    def __init__(self):
        self.num = 1
        self.animal = Tiger(300)
   #用类的属性，指向另一个对象，表示对象的组合关系
   #表示：Room对象拥有一个animal对象
   #房间对象由老虎对象和其它对象组成（这里是房间号，一个int对象）
   #这就是对象的组合
    
补充：
#获取随机数
from random import randint
print(randint(0, 1))
print(randint(1, 10))

#获取当前系统时间
import  time
curTime = time.time()
print(curTime)

#得到的结果是从1970到现在总共的秒数
1529313216.4224925

#如果要得到现在的时间
time1 = time.localtime(time.time())
print(time1)

#结果如下
time.struct_time(tm_year=2018, tm_mon=6, tm_mday=18, tm_hour=17, tm_min=13, tm_sec=36, tm_wday=0, tm_yday=169, tm_isdst=0)

#如果要转换成更加规范的格式
time2 = time.asctime(time.localtime(time.time()))
print(time2)
#结果如下
Mon Jun 18 17:17:13 2018
        
-------------------------------------------------------------------------

（3）对象的继承
比如现实中： 桌子----可以是电脑桌、书桌；    恐龙------可以是暴龙、霸王龙；
可以看出无论是电脑桌，还是霸王龙，都具有各自桌子、恐龙的特性，只是他们各自演变
后都具有了自己一些独特的性质。对象的继承也是一样的，继承之后只需要在子类中定义
自己的属性，其它的继承父类即可

class Father:
    name = ''
    age = ''
    __last = 300000;#私有属性不可继承
    
class Mor:
    pl = 'meili'
    
class Son(Father,Mor): #多继承
    socre = 100
    
s = Son()
s.name = 'tom'
print(s.name)
print(s.pl)
print(s._Father__last)#强制调用私有属性，常用的是在类中直接调用，下面示例可知

#打印结果
tom
meimei
300000
    
#观察上面定义的类
#括号里面的Father叫做父类（基类），Son就是继承类，它具有自己的属性socre=100,同时还继承了name,以及age属性    
#多继承的时，只需要用逗号隔开；但是不可以父类继承子类
#私有属性不可继承（由双下划线定义）
#如果一定要调用私有属性，格式为：print(s._Father__last)由一个下划线开头

----------------------------------------------------------------
重定义：
#子类的属性和行为和父类有些不一样
#比如：重新定义下面父类的方法
#子类实例调用这些属性、方法会使用新的定义
#多态（同样的方法调用，在不同的类型的对象上表现出不同的特性，称之为多态）

class People:
    #定义基本属性
    name = "PeopleName"
    age = 23

    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 200
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):#实例方法
        print("%s 说： 我 %d 岁。" % (self.name, self.age))

    def __find(self):#私有方法
        print("父类私有方法！")

    def printFind(self):
        self.__find()

class Male():
    sex = 'male'
#单继承示例
class Student(People):
    sorce = 88
    def __init__(self, n, a, w, s):
        #首先一定要调用父类的构造函数
        People.__init__(self, n, a, w)
        self.sorce = s

    #重写父类的方法
    def speak(self):
        print("%s 说： 我 %d 岁了， 我考了 %d 分" % (self.name, self.age, self.sorce))

p1 = People('tom', 30, 120)#实例化中有参数，则必须填写
p1.speak()
#调用父类方法
p1.printFind()

s1 = Student('luoli', 20, 100, 88)
s1.speak()

#打印结果如下
tom 说： 我 30 岁。
父类私有方法！
luoli 说： 我 20 岁了， 我考了 88 分

 

