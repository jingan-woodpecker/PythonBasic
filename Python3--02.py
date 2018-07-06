Python3基础2（简单的对象方法）

（1）字符串对象的常用方法
#❶计算字符串中包含的多少个指定的子字符串
>>>'123 123 4454'.count('123')

#❷startswith 检查字符串是否以指定的字符串结尾
#❸endswith 检查字符串是否以指定的字符串开头
tel = '18824123101'
if tel.startswith('188') \
　　or tel.startswith('139'):
　　print("中国移动号码！")
else:
　　print("联通/电信！")

if tel.endswith('8'):
　　print("幸运客户")
else:
　　print("不是幸运客户！")

#❹find 返回指定的子字符串在字符串中出现的位置（下标），如果返回值是-1，则内容不在字符串中
>>>'123455778834456'.find('455')
3

注意：如果有多个返回第一个，还可以指明从什么位置开始查找
>>>'ok, good,name'.find(',')
2
#从‘，’后面开始查找，3这个数字在这里没关系
>>>'ok, good,name'.find(',',3)
8

用途
001 come in, the name is Jack, level 9;
00451 come in, the name is Mike, level 39;
前面的ID号和后面的等级号都是变动的

#❺isalpha 检查字符串是否都是字母
#❻isdigit检查字符串中是否都是数字

>>>'adc1'.isalpha()
False
>>>'12345'.isdigit()
True

#❼str.join将 sepuence类型的参数的的元素字符串合并（连接）到一个字符串，string作为分隔符
>>>';'.join(['I','like','play','football'])
'I;like;play;football'

#❽split将字符串分隔为几个字符串。参数为分隔符
#返回结果存放在一个list对象里

>>>'123 456 789'.split('3')
['12' '456 789']

注意：用什么分隔就去掉什么

#❾lower 将字符串里面如果有大写字母的全部转为小写字母
#❿upper 将字符串里面如果有小写字母的全部转为大写字母

>>>'China'.lower()
'china'

>>>'China'.upper()
'CHINA'

#replace 替换字符串里面指定的子字符串

>>>'Tom is dog. Snoopy is a dog'.replace('dog', 'pig')
'Tom is a pig. Snoopy is a pig'

#⑪strip 将字符串前置空格和后置空格删除
#⑫lstrip将字符串前置空格删除
#⑬rstrip将字符串后置空格删除

>>>' good '.strip()
'good'

>>>' good '.lstrip()
'good '

>>>' good '.rstrip()
' good'

注意：这个方法只可以删除前后空格，中间的空格不会删除

（2）List对象的常用方法

#空list
>>> a = []

#❶append, 给列表尾部添加一个元素

>>>a.append(1)
>>>a
[1]

#从列表中删除一个元素
#方法一 ❷del关键字

>>>a = [3, 5, 1, 2]
>>>del a（1）
>>>a
[3, 1, 2]

注意：是根据下标来删除的

#❸ remove关键字

>>>a = [3, 5, 1, 2]
>>>a.remove（1）
[5, 1, 2]

注意：是根据元素来删除的

#方法二 ❹pop 方法
>>> a = [3, 4, 1, 2]
>>> b = a.pop(1)
>>> b
4
>>> a
[3, 1, 2]

注意：是根据下标来删除的，在删除掉元素的同时，会得到元素的值

#❺reverse, 将列表里面元素倒序排序

>>> a = [1,2,4,5,6]
>>> a.reverse()
>>> a
[6,5,4,2,1]

注意：不是从大到小排序

注意的练习：

- 定义这样一个函数

def e1():
　　print('in e1')
　　return False


- 下面说法正确的是 (b,d) 

A) 执行 False and e1() 屏幕会 显示 'in e1'
B) 执行 e1() and False 屏幕会 显示 'in e1' #先执行el()就会先打印出‘in el’，所以是正确的
C) 执行 True or e1() 屏幕会 显示 'in e1' #先执行了True，因为是or ，一真全真，后面的el()不执行，故不会打印‘in el’
D) 执行 False or e1() 屏幕会 显示 'in e1'


- 有一个列表a，里面的内容分别是从0 到99999，要删除其中99998这个数字元素，下面的代码耗时最长的是 (d)

A) del a[99998]

B) del a[-2]

C) a.pop(99998)

D) a.remove(99998) #需要根据元素内容一个个进行比较，耗时较长


- 下面的代码执行完后，变量b 的值仍然为 'a' (对)
def t2(para):
　　para = 3 #只是局部变量，将3赋值给para后就失效了

b= 'a'
t2(b)

- 下面的代码执行完后，变量b 的值仍然为 [1] (错)
def t2(para):
　　para[0] = 3 #列表中的元素是可以改变的

b= [1]
t2(b)

- 下面的代码执行完后，变量b 的值仍然为 [1] (对)
def t2(para):
　　para = 3 #局部变量

b= [1]
t2(b)

解析：
因为函数里面 para=3 ， 这句代码
创建了新的对象数字3， 并将 para这个变量指向从原来的 列表对象 换成了 数字对象3
这个并不会影响 变量b 指向的对象。

我们记住一个规则， 多个变量指向一个对象， 然后其中一个变量 因为赋值语句而改变了指向关系。 
并不会影响别的变量 ，别的变量还是指向 原来的对象


现有一个游戏系统的日志文件，记录内容的字符串 的格式 如下所示

A girl come in, the name is Jack, level 955;

其中包含的 the name is 后面会跟着人名，随后紧跟一个逗号， 这是固定的格式。

其它部分可能都是会变化的，比如，可能是下面这些

A old lady come in, the name is Mary, level 94454

A pretty boy come in, the name is Patrick, level 194

请大家实现一个函数，名为getName，如下所示

def getName(srcStr):
　　函数体

答案：
def getName (srcStr):
　　return srcStr.split('the name is')[1].split(',')[0]

 