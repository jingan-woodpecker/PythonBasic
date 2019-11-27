1、定义函数和调用函数

    定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
    要让这些代码能够执行，需要调用它调用函数很简单的，通过 函数名() 即可完成调用
    
    函数格式如下：
    
    def 函数名():
        代码
        
```python
def round_area(r): #形参,把参数当做实际存在的值来用
    s = 3.14*(r**2)
    print("圆的面积是%s"%s)
    return s

round_area(7) #调用函数的时候传给函数的数据叫做实参
```

2、函数参数

    * 形参的特点：不用在前面定义，也不会和之前定义的变量冲突
    
```python
a = 1
def test_sum(a , b):
    sum = a + b
    print("和为%s"%sum)
    return sum

test_sum(a , 10)
```

3、函数的返回值

    * 下面的函数中没有返回值(return get)即调用函数test_sum(num1,num2)后赋值给s1的是空值，会返回None
	注意调用函数赋予一个值后，才能打印这个结果，否则报错
	如果本身参数是传数值类型的，结果传了字符串，运行的时候报错，那查看错误信息的时候，看最后一行

```python
a = 1
def test_sum(a , b):
    get = a + b
    print("和为%s"%get)
    # return get

num1 = 10
num2 = 13
s1 = test_sum(num1,num2)
print(s1)
#打印结果
#和为23
#None
``` 
    * return被执行之后，不管return后面还有什么，都不会执行，即print("sum")不会被执行
        
```python
a = 1
def test_sum(a , b):
    get = a + b
    return get
    print("sum")

num1 = 10
num2 = 13
s1 = test_sum(num1,num2)
print(s1)
```   
	定义了一个函数可能不知道是谁要调用，所以别人无法知道你传的参数是什么类型（整数，字符串等）
	所以需要在函数前面先加判断,如果你先传的参数是数值类型,就先加判断保证它是数值,如下所示:

```python
def test_sum(a , b):
    if not isinstance(a ,(int ,float)):#isinstance()判断是什么类型,加入(int,float)表示传入的参数值只能是整数或浮点数
        print("传入的a是%s,不是数字类型"%a)
        return #判断不是数字类型了,后面的代码不需要执行,只需要加上return即可
    elif not isinstance(b ,(int ,float)):
        print("传入的b是%s,不是数字类型"%b)
        return
    get = a + b
    return get

s1 = test_sum("dd",23)
print(s1)
```

    *打印一条横线
    *打印多条横线
    
```python
def print_one_line():
    print("-"*30)

def print_num_lines(num):
    i = 0
    while i < num:
    
    # 因为printOneLine函数已经完成了打印横线的功能，
    # 只需要多次调用此函数即可
        print_one_line()
        i += 1

print_num_lines(5)
```

    *写一个函数求三个数的和
    *写一个函数求三个数的平均值
    
```python
def three_sum(a, b, c):
    result = a + b + c
    return result


def average_num(a, b, c):

    sum3Result = three_sum(a, b, c)
    averageResult = sum3Result/3
    return averageResult

s1 = three_sum(3, 5, 5)
print("三个数的和是%s"%s1)

s2 = average_num(10, 20, 30)
print("三个数的平均值是：%s"%s2)
```
```python
#求三个数的平均数
 
 def avgSum(a,b,c):
   #如果调用的函数返回结果是True和False，则可以作为if后面的条件表达式进行判断
   if is_number(a) and is_number(b) and is_number(c):
     avg_result = (a+b+c)/3
     return avg_result
   else:
     print("无法计算平均值")
 
 def is_number(a):
   if not isinstance(a,(int,float)):
     print("输入的数值%s,不是数值或浮点数"%a)
     return False
   else:
     return True
 
 avg = avgSum(10,80,20)
 print(avg)
```

了解代码的执行顺序

    比如上述代码：先执行def three_sum(a, b, c),但只是先加载并不执行里面的内容，然后执行def average_num(a, b, c)
    也只是加载，接着执行s1 = (3, 5, 5)因为调用了上面的函数也先加载了，所以不会报错，然后就会执行函数里面的代码
    ...
