Python3基础知识8（变量作用域、函数的缺省参数、可变参数、关键字可变参数）

（1）变量的作用域

#函数里面的x和函数外面的x
x = 2
def func():
　　#这个（local）局部变量x,在这里调用后就失效了
　　x = 9
　　print("this x is in the func:",x)

func()
print("----------------------")
#这里打印的x是调用的全局变量（gloabal） 
print("this x is out of func:",x)

#打印结果如下
this x is in the func: 9
----------------------
this x is out of func: 2

#只引用，不修改
x = 2
def func():
　　print("this x is in the func:",x)

func()
print("----------------------")
print("this x is out of func:",x)

#打印结果如下：

this x is in the func: 2
----------------------
this x is out of func: 2

#修改全局变量 ，添加global关键字

x = 2
def func():
　　global x
　　x = 10
　　print("this x is in the func:",x)

func()
print("----------------------")
print("this x is out of func:",x)

#打印结果如下：

this x is in the func: 10
----------------------
this x is out of func: 10
（2）函数的缺省参数

#统计超过指定年龄的男女生人数
students = [
　　{'age': 18, 'name': 'Chen1', 'gender': 'male'},
　　{'age': 19, 'name': 'Chen2', 'gender': 'female'},
　　{'age': 22, 'name': 'Chen3', 'gender': 'male'},
　　{'age': 25, 'name': 'Chen4', 'gender': 'female'},
　　{'age': 20, 'name': 'Chen5', 'gender': 'male'},
]
def statmf(students,minage=18):
　　malelist = []
　　femalelist = []
　　for student in students:
　　　　if student['age'] > minage:
　　　　　　if student['gender'] == 'male':#通过取键值获取
　　　　　　　　malelist.append(student['name'])
　　　　　　elif student['gender'] == 'female':
　　　　　　　　femalelist.append(student['name'])
　　#格式化输出，用空格连接打印出的名字 
　　print('the male students are %s' % ' '.join(malelist))
　　print('the male students are %s' % ' '.join(femalelist))
　　
# 调用该函数的时候需要传入已给学生列表和年龄条件 
statmf(students, 19)

#打印结果如下：
the male students are Chen3 Chen5
the male students are Chen4

#总结：如果都满足条件，则不需要调用第二个参数，可以使用
#缺省函数改成:def statmf(students, minage = 0),这样minage这个参数
#就取缺省参数的值0，调用时直接写：statmf(students)即可

#重点：总的来说，如果下面调用函数的时候没有填第二个参数，那么就使用刚开始定义函数时定义的值，比如定义了minage =18,就用18

注意：没有缺省值的参数就叫做必填参数；
　　   必选参数在前，默认参数在后`；
　　   可以定义多个缺省参数。

（2）可变数量参数

#给定一组数字a,b,c....., 计算a² + b² + c² + ......
def calc(*numbers):
　　total = 0
　　for n in numbers:
　　　　total = total + n*n
　　return total
print(calc(1, 2, 3, 4))

#可以传入任意多的参数
#Python解释器会把传入的参数存入到一个tuple中，赋值给numbers

调用现成的list或者tuple中元素方法
def calc(*numbers):
　　total = 0
　　for n in numbers:
　　　　total = total + n*n
　　return total
nums = [1, 2, 4, 5, 6, 7, 2, 88, 9, 99, 66, 44]
#调用方法一:使用下标的方法
print(calc(nums[0], nums[1], nums[2]))

#如果参数已经在一个list（或者tuple）中，怎么调用nums = [1,2,4,5,6,...]
#方法二
print(calc(*nums))

#打印结果
21
24053

（3）关键字可变数量参数
#允许在调用函数时，传入一个含参数名的参数

def register_student(name, age, **kargs):
　　print('name:', name, 'age:', age, 'other:', kargs)

register_student('tom', 14, sorce = 80, city = 'Heyuan')

#打印结果如下：
name: tom age: 14 other: {'sorce': 80, 'city': 'Heyuan'}

#Python在调用的时候，会把这些关键字参数存到一个dict中，传给kargs;
#它的用处在于：比如在上面的注册学生函数中，我们必须有name、age这两个参数，但如果调用者愿意提供更多的参数，我们也可存储下来；
#当然我们也可以进行调用


#如果参数已经在一个dict中，怎么调用
students = {'city': 'Heyuan', 'job': 'IT'}
def register_student(name, age, **kargs):
　　print('name:', name, 'age:', age, 'other:', kargs)
#调用展开**students
register_student('jack', 23, **students)

#打印结果如下
name: jack age: 23 other: {'city': 'Heyuan', 'job': 'IT'}

总结：
#在Python中定义函数，可以用必填参数、缺省参数、可变参数和关键字参数，可以一起使用，也可使用某些；
#参数定义的顺序应该是：必填参数、缺省参数、可变参数和关键字参数（其中缺省参数可以放在可变参数后面）


def func(a, b, c=0, *args, **kw):
　　print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
func(3, 4)
func(1, 4, 5)
func(3, 5, 5, 'chenzi', 'Shenzhen')
func(4, 5, 2, 'Gushu', city='Guangzhou')
#注意这种调用方式
func(4, 5, c=3, city='Guangzhou')

#打印结果如下：
a= 3 b= 4 c= 0 args= () kw= {}
a= 1 b= 4 c= 5 args= () kw= {}
a= 3 b= 5 c= 5 args= ('chenzi', 'Shenzhen') kw= {}
a= 4 b= 5 c= 2 args= ('Gushu',) kw= {'city': 'Guangzhou'}

a= 4 b= 5 c= 3 args= () kw= {'city': 'Guangzhou'}

注意：可变参数的存储以-----元组方式；
关键字参数的存储以----字典方式。