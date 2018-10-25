1、模块的导入

    模块好比工具包，要想使用这个工具包(好比函数)，就需要导入这个模块
    
    * 方法一：用关键字import来引入某个模块，比如导入random模块，import random
    要导入多个模块用逗号","分隔开，import module1,module2,...
    
    要调用random模块的时候，必须这样引用(模块名.函数) random.randint(0 , 10)
```python
import random
print(random.randint(0 , 10))
```

    * 方法二：from...import ,其中from语句让你从模块中导入一个指定的部分到当前命名空间中
    例如，要导入模块random中的randint函数，不会把整个模块都导入到命名空间，只会单个引入randint
    
```python
from random import randint
print(randint(0 , 10))
```

    * 方法三：from...import *  导入一个模块中所有项目，一般不使用这种方法
    因为，如果导入的不同模块中有相同函数名的，后面的会覆盖前面的
    
2、as 给导入的模块重新命名

```python
from selenium.common.exceptions import NoSuchAttributeException as NE
print(NE.args)
```    

3、模块的调用
 
    以下为test.py文件   
```python
#工具方法：判断字符串是否为null,当字符串为None，或者''为null,并且'    '这样也为null
def isnull(str):
    if not str:
        return True
    elif str.strip()=='':
        return True
    else:
        return False
def module1():
    print("module1模块的调用")
```

    以下为test1.py文件
```python
# test.py和test1.py文件都在同一目录下进行模块的导入使用
import test
a = ""
get_end = test.isnull(a)
print(get_end)

from test import isnull , module1
b = " sdf"
get_end1 = isnull(b)
print(get_end1)
c = module1()
```

4、测试模块(__main__):表示python解释器主动调用代码测试

```python
#工具方法：判断字符串是否为null,当字符串为None，或者''为null,并且'    '这样也为null
def isnull(str):
    if not str:
        return True
    elif str.strip()=='':
        return True
    else:
        return False
def module1():
    print("module1模块的调用")

if __name__ == "__main__": #由python解释器主动执行该模块代码是为了测试
    print(isnull("a"))
```

5、模块中的__all__

```python
__all__ = [] #括号中写入允许调用的，但只在python2中生效
```

6、python中的包(本质上就是目录，主要是用来对文件分组的)

    比如用目录(my_package),放入两个模块module1、module2，其中my_package这个目录就是包
    
    * 如果现在在当前目录调用模块是无法使用的 ，原因在于调用模块时，是先在当前目录下找，
    如果当前目录不存在，就会在python的系统目录下(即在python-3.6.1home目录下找)，如果没
    找到，就会报错。
    
```python
#如果直接这样导入包使用，可以识别包my_package，但无法识别到里面的模块module1
import my_package
my_package.module1.test1()

'''
AttributeError: module 'my_package' has no attribute 'module1'
'''
``` 

    * 解决上述问题的方法：在使用import的同时将包和模块名一起导入，例如： import my_package.module1 或者
    from my_package import module1
    
```python
import my_package.module1
my_package.module1.test1()
```
    * 但上述解决方法只在python3中生效，在python2中依然会报错，还需要在包目录中创建一个"__init__.py"文件才叫包
    __init__.py文件控制着导入包的方式
    
总结：
    
    在python3中创建"__init__.py"文件不会报错，并且兼容python2,所以最好创建包的时候都加入"__init__.py"文件
    在"__init__.py"中也可以写入代码，例如可在该文件中写入如下内容
    
```python
from . import module1
from . import module2
```
    调用代码的时候，就可以直接导入包了
```python
import  my_package
```

7、模块的发布和安装

    要想创建的包在任何其它目录下都可以找到，就模块发布到python的系统目录下即可

比如test_pub目录结构如下,有suba一个包

    |----- setup.py
    |----- suba
    |     |----- aa.py
    |     |----- bb.py
    |     |----- __init__.py
        
    比如我要发布suba这个包的步骤
        1、在和包相同的目录下建立一个setup.py文件
        2、setup.py文件输入两行代码
```python
from distutils.core import setup
setup(name="压缩包的名字",version="1.0",description="描述",author="作者",py_modules=["suba.aa","suba.bb"])
```
        3、创建一个新目录(test_pub)
        4、将my_module包放入到新目录(test_pub)当中
        5、构建模块(即打成压缩包)：进入到test_pub目录下，输入python3 setup.py build ，这样就会生成一个build目录
        6、生成压缩包：还在当前目录下，输入python3 setup.py sdist 这样就生成dist目录下
        7、现在就可以进入dist目录下，找到压缩包了。(可拷贝到其它机器上或发布到python系统中)
        8、可拷贝到其它目录下并解压出来
        9、在setup.py目录下输入：python3 setup.py install
        注意：如果在install的时候，执行目录安装，可以使用python3 setup.py install --prefix==安装路径
        
        
   