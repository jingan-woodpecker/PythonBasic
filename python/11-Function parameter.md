1、函数返回值(本质上利用了元组)
    
    函数可以有多个返回值
    
```python
def test(a , b):
    shang = a/b
    yushu = a%b
    return shang , yushu

shang, yushu = test(100 , 20)
print("多个返回值有%s和%s"%(shang , yushu))

#多个返回值有5.0和0
```

2、函数的参数

    * 缺省参数 :调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
    
        a、 带有默认值的参数一定要位于参数列表的最后面;
        b、 除非有默认参数，否则定义多少个参数，就要一一对应传入多少值;
        c、 可以定义多个缺省参数的值;
    
```python
def test(a , b , c=20):
    sum_3num = a + b + c
    print("三个数的和是%s"%sum_3num)

#因为调用test()函数时，缺省参数"c"没有重新传入，所以使用默认值20
test(20 , 39)

#可定义多个缺省值参数的值，但调用时新传入了值则会覆盖默认值
def test1(name , age=23 , sex="男"):
    print("name: %s"%name)
    print("age: %s"%age)
    print("sex: %s"%sex)

test1("小竹" , 25)


#注意：带有默认值的参数一定要位于参数列表的最后面，下面的定义时错误的
def test1(name , age=18 , sex):


```

    * 不定长参数： 有时可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名。
    
        a、 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
        b、 加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
        
```python
#*args 也叫可变参数即可以传入多个参数
def test(a , b , *args):
    sum = a + b
    for i in args:
        sum = sum + i
    print("和的值为：%s"%sum)

test(10, 40, 50, 20, 40)
```

```python
def test(a , b , *args , **kwargs):
    sum = a + b
    for i in args:
        sum = sum + i
    for i in kwargs.values():
        sum += i
    print(sum)

test(10, 40, 50, 20, num=20 , num1=89)

def test1(x , y , **kwargs):
    print(x)
    print(y)
    for key, values in kwargs.items():
        print(key, "=" , values)

test1(20, 49, name="小轩", sex="女", age="24")
'''
229
20
49
name = 小轩
sex = 女
age = 24
'''
```

    c、:集合的拆包：就是把一堆的值拆开，比如列表、字典中的值
    
```python
def test1(x , *args):
    sum = x
    for i in args:
        sum += i
    print("和的值为：%s"%sum)

def test2(**kwargs):
    for key, values in kwargs.items():
        print(key, "=" , values)

num1 = [20, 40]
num2 = {"name":"小轩", "sex":"女", "age":24}
test1(*num1)
test2(**num2)    
```

    下面的代码：x，a的不可变类型内存地址一样的原因，在于x.replace("a","A")没有用值接收，所以并没有指向"Akjlj"
              y，b的可变类型内存地址一样的原因是，在于可变，所以指向都一样。
```python
def test(x , y):
    x.replace("a" , "A")
    y.append(49)
    print("x变量指向的内存地址为：%s"%id(x))
    print("y变量指向的内存地址为：%s"%id(y))

a = "akjlj"
b = [4, 6, 69, 2]
print("a变量指向的内存地址为：%s"%id(a))
print("b变量指向的内存地址为：%s"%id(b))

test(a , b)
'''
a变量指向的内存地址为：34587064
b变量指向的内存地址为：39371208
x变量指向的内存地址为：34587064
y变量指向的内存地址为：39371208
'''

```
    