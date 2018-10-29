内建函数

    菜鸟教程内建函数详细讲解：http://www.runoob.com/python3/python3-built-in-functions.html
    
range(start,stop[,step])

    计数从start开始，默认从0开始，到stop结束，但不包括stop;每次的步长，默认为1
    
map(function,sequence[,sequence,...])

    根据提供的函数对指定序列做映射
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    Python 2.x 返回列表。
    Python 3.x 返回迭代器。
    
```python
get_one = map(lambda x:x*x,[1,2,3])
for get in get_one:
    print(get)
'''
1
4
9
'''
```
```python
get_one = map(lambda x,y:x+x,[1,2,3],[4,5,6])
for get in get_one:
    print(get,end=" ")
# 2 4 6
```

```python
def fun(x,y):
    return (x,y)
k1 = [0,1,2,3,4,5,6]
k2 = ["Sun","M","T","W","T","F","S"]
k3 = map(fun,k1,k2)
print(list(k3))

'''
[(0, 'Sun'), (1, 'M'), (2, 'T'), (3, 'W'), (4, 'T'), (5, 'F'), (6, 'S')]
'''
```
filter(function or None, sequence)

    对指定序列执行过滤操作
    过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
    接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
    
    filter(function, iterable)
        function -- 判断函数。
        iterable -- 可迭代对象。

```python
def is_odd(n):
    return n%2 == 0

tmplist = filter(is_odd , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

#[2, 4, 6, 8, 10]
```
reduce(function,sequence,[,initial])

    对参数序列中元素进行累加
    Python3中reduce()函数已经被从全局名字空间里移除了，它现在被放置在functools模块里
    
```python
from functools import reduce
num = reduce(lambda x,y:x+y,[1,2,3,4])
print(num)

#注意这个打印出来的结果的顺序
get = reduce(lambda x,y:x+y,["aa","bb","cc"],"dd")
print(get)

'''
10
ddaabbcc
'''
```

partial函数(偏函数)
    
    把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更加简单
      
```python
import functools
def showarg(*args,**kwargs):
    print(args)
    print(kwargs)

p1 = functools.partial(showarg, 1,2,3)
p1()
p1(4,5,6)
p1(a="python",b="java")

'''
(1, 2, 3)
{}
(1, 2, 3, 4, 5, 6)
{}
(1, 2, 3)
{'a': 'python', 'b': 'java'}
'''
```

wraps函数

    * 使用装饰器时，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性会发生改变)
    * wraps的装饰器可以消除这样的副作用
  
    下面的代码如果不加入@functools.wraps(func)以及导入functools模块，
    打印的信息为wrapper function，而不是有装饰器的函数中的test function，这就是副作用引起的。
    
```python
import functools
def note(func):
    "note function 文档说明"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper

@note
def test():
    "test function"
    print("I am test")

test()
print(test.__doc__)

'''
note something
I am test
test function
'''
```  