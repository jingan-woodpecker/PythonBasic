1、局部变量

    
    局部变量，就是在函数内部定义的变量
    不同的函数，可以定义相同的名字的局部变量，但不会产生影响
    局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储，这就是它的作用

```python
def test():
    a = 100
    a += 10
    print("a的值是:%s"%a)
    
test()
print(a)
"""
因为定义的变量a为局部变量作用范围在该函数中，print(a)不在该函数中，所以并不执行。
"""
```
2、全局变量

    * 如果一个变量，既能在一个函数中使用，也能在其他的函数中使用，这样的变量就是全局变量
 
```python
a =300 #全局变量
def test():
    a = 100
    a += 10
    print("a的值是:%s"%a)#有局部变量，就优先使用

def test01():
    a = 200 #如果局部变量和全局变量的变量名一样，优先使用局部变量
    print("test01的值是:%s"%a)

def test02():
    print("test02的值是:%s"%a)#没有局部变量所以就调用了全局变量

test()
test02()
test01()
print(a)
"""
a的值是:110
test02的值是:300
test01的值是:200
300
"""
``` 

    * 如果要使用其他函数中的值，可以先用return返回，然后再作为参数传入
 
```python
a =300
def test():
    a = 100
    a += 10
    print("a的值是:%s"%a)
    return a

def test01():
    a = 200
    print("test01的值是:%s"%a)

def test02(a):
    print("test02的值是:%s"%a)

b = test()
test02(b)
print(a)
```  

    * 如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
    
```python
a = 666

def test1():
    global a
    print("全局变量修改前a的值是%s"%a)
    a = 100
    print("全局变量修改后a的值是%s"%a)

def test2():
    print("最后全局变量a的值是%s"%a)

test1()
test2()
'''
全局变量修改前a的值是666
全局变量修改后a的值是100
最后全局变量a的值是100
'''
```

    *可变类型的全局变量
    
```python
a = 666

def test():
    a += 100
    print(a)
test()
'''
    a += 100
UnboundLocalError: local variable 'a' referenced before assignment
'''

test_list = [1,]

def test1():
    test_list.append(2)
    print(test_list)
test1()

#[1, 2]
```

    总结：
        在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
        
        对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
        
        对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。

