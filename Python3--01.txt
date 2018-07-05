#1、数据类型注意点
Pyton中没有double、long类型

查看用什么数据类型用type()

次方
>>>2**4
>>>16

保留小数点的方法
6.0/7 6/7 6.0//7

#2、数值运算注意点：
计算 4534减78 其结果 乘以53 ， 最终结果输出到终端，写在文件中的代码应该是 C
A) 4534-78*53
B) print (4534-78*53)
C) print ((4534-78)*53)
D) (4534-78)*53

#3、我们可以用type内置函数，显示数据的类型，比如 type(3)

#4、- python3 执行下面的代码，不会报错 (错) 注意字母的大小写
yourname = 'Jack'
print (Yourname)

#5、Python 中的一切数据都是对象 (对)

#6、变量的注意点:
下面哪几组包含了错误的变量命名 (B C D)

A)
a
abc

B)
a_3
2a

C)
a2c
3_a

D)
a-1
a1_b

（1）一般以字母（大写、小写）开头，不以数字开头，后面可以使用下划线或数字；
（2）大小写敏感；
（3）不能与关键字相同；
（4）不能与内置函数相同。

- 没有任何变量引用的对象，最终会被Python解释器清除 (对)

#7、列表的注意点：
定义tuple 中只有一个元素 3， 可以这样定义 (3,) （对）

#8、sequence切片操作注意点：
下面的字符串列出了人的名字 和体重，

# str1 = 'name: Micle, weight: 130kg'

#要用切片的方式从str1中取出体重（包括kg部分） 可以是 str1[-5:] （对） 注意：单引号不要计算入内


下面的字符串列出了人的名字 和体重，

str1 = 'name: Jack, weight: 130kg'

要用切片的方式从str1中取出人名 可以是 str1[7:11] （错误，应该是str1[6:10]）

注意：当字母之间只有一个空格的时候，进行切片时不计算入内，如果大于一个空格则要计算入内；
切片操作都是谁创建了一个新的列表对象作为返回值；

#列表中一些常用的内置函数与方法
len(list) #计算元组元素个数
max(list) #返回最大值
min(list) #返回最小值
list.reverse() #反向列表中的元素
list.remove() #移除列表中的元素，第一个元素数值为1

#8、元组的注意点：
列表中的内置函数元组同样适用
但比较字符串的大小时，要注意首先是比较长度若是长度相同，则一个个比较编码的大小

#9、运算顺序注意点：
and 且 or 或 not 不
不添加括号的情况下，运算顺序为：not and or

#10.条件语句的注意点：
Pytho不支持switch 语句，所以多个条件判断只能用elif实现
if score>80 \
　　and score<85\
　　or score<85;
这样操作可以使代码更清晰

通常我们在一个条件前面加上not表示反义
if not(age >= 60 or age <18):
　　print('you can play this game')
　　
if判断条件还可简写
x = 9
if x:
　　print('x is not zero')
只要x是非零数值、非空字符串、非空list等，就判断为True,否则为False.

#11、判断某字段是否包含在变量中注意点：
- 一个变量a定义如下
a = ['this', 'test', 4.56, ['inner', 'list']]
下面的表达式结果为False 的有 (d)

A) 'this' in a

B) 'test' in a

C) 't' not in a

D) 'inner' in a

['inner','list'] in a 这样才会打印True


- 下面的两种代码写法，执行效果是相同的（T）

方法一： 
if a>1:
　　if b>2:
　　　　print('a,b both > 1')

方法二：

if a>1 and b>2:
　　print('a,b both > 1')


- 下面的两种代码写法，执行效果是相同的（T）

方法一： 
if a>1:
　　if b>2:
　　　　print('a,b both > 1')

方法二：

if a>1 and b>2:
　　print('a,b both > 1')




- 下面的代码一，和代码二 是等价的 (T)

代码一： 
score = 90
if score >= 90:
　　print('your score is', score)
　　print('excellent')
elif score >= 60:
　　print('your score is', score)
　　print('ok')
else:
　　print('your score is', score)
　　print('you have trouble') 
代码二： 

score = 90
print('your score is', score)

if score >= 90:
　　print('excellent')
elif score >= 60:
　　print('ok')
else:
　　print('you have trouble') 


#12、函数
（1）函数的定义
def playball():#先定义，后调用
　　print("来哦")
　　print("廖竞安")
playball()#调用
print(type(playball))#类型
print(playball)#内存地址
print(playball())#返回值，因为现在没有返回值，所以打印None

（2）参数
def foo(a,b):
　　addSum = a*b
　　print(addSum)
foo(10,33)#调用

注意：当形参个数多于实参个数，运行程序会报错，不符合格式要求

关键字参数调用
def foo(a, b,):
　　sum = a*b
　　print(sum)
foo(10,33)#调用
foo(a=10, b=33)
foo(3, b=4)
#下面的表示方法会报错，一旦前面使用了关键字参数，后面就必须也使用
foo(a=3, 4)

返回值
def foo(a, b):
　　sum = a*b
　　return sum #有返回值
date = foo(3, 4) + 32 
print(date)

全局变量和局部变量
sum = 2 #全局变量，作用域不同，
def foo(a, b):
　　sum = a*b #局部变量，计算完之后就失效，所以不打印12，只打印出2
　　return sum #有返回值
date = foo(3,4) +12
print(date)
print(sum)

注意点：return 后面函数里面的语句都不打印

可以返回多种类型
sum = 2 
def foo(a, b):
　　sum = a*b 
　　return sum
date = foo(3,4) +12 , 12, '竞安' #返回元组
print(date)
print(sum)

内置函数: str、int、float
>>>str(1)
>>>str(2.44)
>>>str('4.454')
>>>int('54')
>>>float('34.5')
>>>float('33')
例如：把数值转成字符串再连接
'data=' + str(5)

 

#实际运用
date = 200
def foo(a, b):
　　sumdata = a*b
　　return sumdata
print(foo(3,4))
print("date的值是" + str(date))

 