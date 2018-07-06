Python基础知识10（模块与包库的安装使用）

（1）使用标准库
#标准库： Python安装包里面提供的功能模块和包
主要包括
内置类型和函数
   #比如len、int、open等
   #直接使用，无需import

功能模块
   #包含程序设计所需的常用的功能
   #需要用import导入他们就可以使用

import time
print(time.strftime("%Y_%m_%d %H:%M:%S"))

#打印结果如下
2018_06_17 11:06:16
   
----------------------------------------------

#调用外部的计算器程序，只需哟导入OS操作库os
import os
os.system("calc")

注意：需要了解更多的函数、功能查看文档即可

（2）模块搜索规则
#用import或者from...import来导入模块的时候，Python是根据sys模块的一个变量内容sys.path的列表值来决定的
>>> import os
>>> os.__file__
'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\os.py'
>>> import sys
>>> sys.path
['', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib', 
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36',
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages']

而sys.path的值又是python解释器启动过程中一般会将下面的路径添加到sys.path里面去
1、启动脚本所在的目录；
2、PYTHONPATH环境变量里包含的目录。如果没有设置则忽略。该环境变量设置和PATH环境变量的设置方法类似；
3、标准库目录，已经随着Python的安装进入到计算机中的lib/site-packages目录；
4、lib/site-package下面.path文件里指定的路径。

上面就是Python解释器启动过程自动得到搜索路径，我们也可以自行修改那个sys.path里面的内容，动态的改变模块搜索路径。
 
-----------------------------------------------------------------------------
#比如我们搜索os模块的路径
>>> import os
>>> os.__file__
'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\lib\\os.py'

自定义模块
如果不在当前工作目录
   可以加到PYTHONPATH中
   也可以直接写入sys.path中

（3）pip安装第三方库
第三方库和标准库的区别：不是解释器安装后内置的。
安装好以后，其导入使用的方式和标准库、自己开发的库没有任何区别

#zhi安装方式：
#1、下载，拷贝到项目工程目录下面
#2、官方源PyPI（Python Package Index）
     #目前可以使用Pip安装
     #类似yun、apt-get、npm
        
#命令格式
pip install 第三方库名称

比如：安装selenium

C:\Users\asus>pip install selenium
    
Requirement already satisfied: selenium in c:\users\asus\appdata\local\program
python\python36\lib\site-packages
上面显示说我已安装过selenium

或者安装其他：pip install requests
-----------------------------------------------------------------------------------

安装前先用命令：C:\Users\asus>where pip   查看有多少pip，若有多个pip则需要先在命令前添加Python3.6.4
    
#卸载方式

pip uninstall requests

#指定版本安装
pip install SomePackage==1.0.4  #specific version
pip install 'SomePackage>=1.0.4 #minimum version

#更新安装
pip install selenium -U


