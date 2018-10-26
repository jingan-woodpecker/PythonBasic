1、查看模块搜索路径
```python
import sys
print(sys.path)

'''
['D:\\python3\\webdriverAPI\\pratices\\forward',
 'D:\\python3\\webdriverAPI',
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip']
'''
```

    * 会在原有的搜索路径后面添加你所加入的搜索路径
    
```python
import sys
sys.path.append("D:\\python3\\webdriverAPI")
print(sys.path)

'''
['D:\\python3\\webdriverAPI\\pratices\\forward',
 'D:\\python3\\webdriverAPI',
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',
 'D:\\python3\\webdriverAPI']
'''
```
    * 可以确保先搜索这个路径
```python
import sys
sys.path.insert(0,"D:\\python3\\webdriverAPI")
print(sys.path)

'''
['D:\\python3\\webdriverAPI'
 'D:\\python3\\webdriverAPI\\pratices\\forward',
 'D:\\python3\\webdriverAPI',
 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',]
'''
```

2、模块的安装和查看

    a、windows的系统下，可以使用pip安装第三方库，安装方式有：
        (1) 方式一：下载、拷贝到项目工程目录下
        (2) 方式二：官方源使用pip安装类似于yum、apt-get、npm
        
        比如安装selenium，先找到python的安装在那个目录下，然后在当前目录打开cmd命令窗口
        输入：pip install selenium，若要安装其他库比如requests可以输入：pip install requests
        
注意安装前可以先在cmd命令窗口输入：where pip 查看有多少pip,若是有多个pip则需要在命令前添加Python3.6.4

    卸载的方式： 比如卸载requests库，只需要输入；pip uninstall requests
    
指定版本安装

    pip install SomePackage==1.0.4  #specific version
    pip install 'SomePackage>=1.0.4 #minimum version
    
更新安装

    pip install selenium -U
        

3、is 和 ==

    is和==这两种运算符区别之前，首先要知道Python中对象包含的三个基本要素，
    分别是：id(身份标识)、type(数据类型)和value(值)。

    * == 是比较两个对象的value值是否相等(值比较)
    
在linux系统下查看已经安装的python模块

    方式一： 在命令行下使用pydoc命令
        在命令行下运行$ pydoc modules查看
        
    方式二、在python交换解释器中使用help()查看
        在交互器解释器中输入：>>>help("modules")即可，和上述方式效果一致
        
    方式三、
        在python解释器下导入sys模块来查看
        >>>import sys
        >>>sys.modules.keys()

linux 中安装pip工具
    
    1、首先检查linux有没有安装python-pip包,直接执行yum install python-pip
    2、没有python-pip包就执行命令yum -y install epel-release
    3、执行成功之后,再次执行yum install python-pip
    4、对安装好的pip进行升级pip install --upgrade pip

```python
a = "1233445"
b = "1233445"
print(a == b)
#True
```   

    * is 是比较两个引用(即id值是否相等)是否指向了同一个对象(引用比较)    

```python
a = 1
b = 1
print(a is b)

a = "123"
b = "123"
print(a is b)

a = [1,2,3]
b = [1,2,3]
print(a is b)

a = [1,2,3]
b = a
print(a is b)

a = (4,5,6)
b = (4,5,6)
print(a is b)

a = {"name":"xiaozhu","age":22}
b = {"name":"xiaozhu","age":22}
print(a is b)

'''
True
True
False
True
False
False
'''
```  

    总结只有数值型和字符串型的情况下，a is b才为True，当a和b是tuple，list，dict或set型时，a is b为False      
     
      
