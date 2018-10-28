生成器： 一边循环一边计算的机制(或者说使用yield的函数称为生成器)

    特点：因为调用一次才生成一次，所以节约内存；
          迭代到下一次的调用时，所使用的参数都是第一次所保留下的

    创建生成器
    
```python
g = (x for x in range(5))
print(g)
#<generator object <genexpr> at 0x00000000024DA780>
```

    * 可以通过next()函数获得生成器的下一个返回值
    * 没有更多元素是，抛出StopIteration"停止迭代"的异常
    
```python
g = (x for x in range(3))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
0
1
2
Traceback (most recent call last):
  File "D:/python3/webdriverAPI/pratices/forward/test.py", line 5, in <module>
    print(next(g))
StopIteration
'''
```
    * 生成器也可以使用for循环，因为生成器也是可迭代对象
    
```python
g = (x for x in range(3))
for x in g:
    print(x)
'''
0
1
2
'''
```

创建生成器的另一种方法

    先了解yield:每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
    并在下一次执行 next() 方法时从当前位置继续运行。
    
    执行了yield，相当于交出了cpu的控制权交给别的程序
    
```python
def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        print("迭代")
        yield b
        a,b = b,a+b
        n += 1
    return "done"

get_num = fib(5)
#可以用next()或者for循环
print(next(get_num))
for i in get_num:
    print(i)
```

__next__()和send()方法

    两种方法的不同之处在于，使用send()方法时，第一次调用时要传入None即send(None)
    
```python
def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        print("迭代")
        yield b
        a,b = b,a+b
        n += 1
    return "done"

get_num = fib(4)
print(get_num.__next__())
print(get_num.__next__())

'''
迭代
1
迭代
1
'''
```

```python
def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        print("迭代")
        yield b
        a,b = b,a+b
        n += 1
    return "done"

get_num = fib(5)
print(get_num.send(None))
#可以通过传入的参数进行逻辑上的控制
print(get_num.send("一定要传入参数"))
print(get_num.send("一定要传入内容"))

'''
迭代
1
迭代
1
迭代
2
'''
```

迭代器

    迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象。
    迭代器只能往前，不会后退
    
可迭代对象(Iterable)
    
    集合数据类型， 如list、tuple、dict、set、str等
    生成器和带yield的generator function
    
如何判断对象可迭代？

    先判断是否是可迭代的，只有是可迭代的再处理
```python
from collections import Iterable
isinstance([],Iterable)
#True    
```

迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器
    
```python
from collections import Iterable
isinstance((x for x in range(10)),Iterable)
```

```python
#只有生成器才是迭代器
a = [1,2,3,4]
next(a)
'''
TypeError: 'list' object is not an iterator
'''
```
如何将字典、元组、列表等可迭代对象变成迭代器
    
    iter()函数：可将迭代对象转换成迭代器
    导入Iterator模块判断是不是生成器
    
```python
from collections import Iterator
a = [1,2,3,4]
it = iter(a)
#判断是不是生成器
print(isinstance(it,Iterator))
print(next(it))
'''
True
1
'''
```

    总结：可迭代对象不一定是迭代器
        


    