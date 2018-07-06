Python3基础知识9（模块与包简单概念）

（1）模块
#简单来讲：一个.py文件就称之为模块（Module）
　　注意：模块名就是py文件名（不包括.py） 比如test.py

模块化的好处：
#1、以库（比如selenium库）形式封装功能，方便给别的代码调用；
　　　　库其实就是模块和包
　　　　可以使用自己写的库，Python标准库，第三方库

#2、避免变量名冲突（包括函数名）
　　如果一个代码文件特别的大，变量的名字容易发生重复
　　需要想出不同的变量名或者函数名
　　如果采用模块分割代码，每个模块文件代码都不是很多，就可以大大的缓解这个问题
　　每个模块中的变量名作用域只在本模块中

（2）函数的调用
#不同模块之间的调用
#mathFunction.py模块中的内容

print('***begin mathFunction!***')
VERSION = 0.1
BUILDOATA = '2018.02.08'

def sumFun(a,b):
　　print('%d + %d = %d' %(a, b, a+b))

def difFun(a,b):
　　print('%d - %d = %d' %(a, b, a-b))

print('***end mathFunction***')

---------------------------------------------下面的为导入模块的方法一

#statTest.py模块中的内容

print('this is starts!')
#strrTest模块中调用mathFunction模块中的函数
import mathFunction #导入了模块
#导入后就可执行里面的函数求和
mathFunction.sumFun(1, 2)
#求差
mathFunction.difFun(3, 4)

#调用mathFunction.py模块中的属性
print(mathFunction.VERSION)

注意：此方法缺点是调用时需要写模块名
-------------------------------------------下面是调用多个模块方法（用逗号分隔即可）

import mathFunction,moudule1,moudule2,moudule3 #导入多个模块

------------------------------------------给模块取别名，防止同名以及方便记忆（使用as）

import mathFunction as fun #起别名（注意：后面调用就要使用别名，否则会报错）

---------------------------------------------下面为导入模块的方法二
#明确的导入模块中指定的函数方法
from mathFunction import sumFun，difFun
#不需要写前缀mathFunction模块名
sumFun(34, 5)
difFun(33, 6)

#同样的针对性导入属性也一样
from mathFunction import VERSION
print(VERSION)

注意：此方法的缺点是当被调用的模块中方法名改动了，就会报错，比如说sumFun改为sumF就会报错；

注意：如果在一个模块中从调用了两个模块中的方法，但是方法名是一样的，会导致后面的覆盖前面，所以使用别名可以减少这种情况出现）

----------------------------------------全部导入（不建议使用,潜在的污染名字空间的危险）
from module import *

（3）自定义包
#简单来讲：组织存放模块文件的目录就称之为包（Package）

#包的结构如下

Phone/ #顶层的包 
　　_init_.py #可以初始化文件，也可以是空文件（Python3.3之前必须添加）
　　commom_util.py
　　Voicedta/ #子包
　　　　_init_.py
　　　　Pots.py
　　　　Isdn.py
　　Fax/ #子包
　　　　_init_.py
　　　　G3.py
　　Mobile/ #子包
　　　　_init_.py
　　　　Analog.py
　　　　Digital.py

-------------------------------------------------------------调用包内模块的方法
目录结果如下：
> Phone
　　﹀Mobile
　　　　_init_.py
　　　　mobile.py

注：mobile.py文件中存在若干方法， 比如mobilefun()、dial()
-----------------------------------------------------------------

方法一： 
import Phone.Mobile.mobile as mFun
mFun.mobilefun()

方法二：
from Phone.Mobile import mobile
mobile.dial()

方法三：
from Phone.Mobile.mobile import dial
dial()

 