类装饰器

    * 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
    * 一般callable对象都是函数，也有例外，只要某个对象重写了__call__()方法，那么这个对象就是callable的。
    
```python
class Test(object):
    def __init__(self,func):
        print("func:%s"%func.__name__)
        self.func = func
        
    def __call__(self):
        print("附加功能")
        self.func()
        
@Test #生成Test的一个对象，所以会先调用__init__方法，并且把下面装饰的函数做为参数传进去
def fun():
    print("fun")

fun() #调用Test的一个对象的__call__方法

'''
func:fun
附加功能
fun
'''
```

对象池

    * Python为了优化速度，使用了小整数[-5,257)对象池，避免为整数频繁申请和销毁内存空间(即内存地址全是一样的)
    * 同理，单个字符也提供对象池，常驻内存
    * 对于字符串，单个单词，不可修改，默认开启intern机制，采用计数机制公用对象，引用计数为0则销毁

```python
c = "a"
b = "b"
print(id(c))
print(id(b))

s = "hello"
s1 = "hello"
print(id(s))
print(id(s1))

'''
38207304
38205904
38380128
38380128
'''
```    