装饰器：其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数

    特性：1、可以把被装饰的函数替换成其他函数
          2、可以在加载模块时立即执行
          
    功能：1、引入日志；
          2、函数执行时间统计；找出那些程序运行较慢，函数前后定时，再相减
          3、执行函数前预备处理；
          4、执行函数后清理功能；
          5、权限校验等场景；
          6、缓存
 
不使用装饰器的情况         
 ```python
def doca(func):
    def wrapper():
        print("wrapper")
        func()
    return wrapper

def fun():
    print("装饰器")

ret = doca(fun)
print(ret())
'''
wrapper
装饰器
None
'''
```

使用装饰器:原来doca()函数的的内容执行了装饰到fun1()函数中

    写代码要遵循：开放封闭性原则即代码可以拓展，但尽量不要修改
```python
#func()函数作为参数
def doca(func):
    def wrapper():
        print("wrapper")
        func()
    return wrapper

@doca
def fun1():
    print("装饰器")

print(fun1())
'''
wrapper
装饰器
None
'''
```
```python
#定义函数，完成包裹数据
def make_bold(fn):
    def wrapped():
        return "<br>" + fn() + "</br>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@make_bold
def test1():
    return "hello world-1"

@make_italic
def test2():
    return "hello world-2"

@make_italic
@make_bold
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())

'''
<br>hello world-1</br>
<i>hello world-2</i>
<i><br>hello world-3</br></i>
'''
```

通用装饰器

    需要满足两个条件才可以通用：
    1、不定长参数
    2、带返回值
    
```python
from time import ctime,sleep
def timefun(func):
    #设置不定长参数
    def wrappedfunc(*args , **kwargs):
        print("%s called at %s"%(func.__name__,ctime()))
        #传的参数要和wrappedfunc中的一致，并且有返回值
        ret = func(*args , **kwargs)
        return ret
    return wrappedfunc

@timefun
def foo(name , age , sex):
    print("my name is %s ,I am %s years old and I am a %s"%(name,age,sex))

@timefun
def getInfo():
    return "---hahaha---"

print(foo("xiaozhu" , 22 , "boy"))
sleep(2)
print(getInfo())

'''
foo called at Sun Oct 28 12:01:56 2018
my name is xiaozhu ,I am 22 years old and I am a boy
None
getInfo called at Sun Oct 28 12:01:58 2018
---hahaha---

'''
```
