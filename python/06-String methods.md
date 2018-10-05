1、字符串通过下标取字符的基本方式

```python
#通过下标的方法取字符
title = "ZhongGuoJianShi"
print("字符串的第一个字符是%s"%title[0])
print("字符串的最后一个字符是%s"%title[-1])
```

2、切片：指对操作的对象截取其中一部分的操作，字符串、列表、元组都支持切片操作。

    切片的语法:[起始:结束:步长]  注意：包头不包尾的原则
    
```python
title = "Zhong Guo JianShi"

print("截取字符串hong的:%s"%title[1:5])
#注意空格也要计算在内
print("截取字符串Guo的:%s"%title[5:9])
#从后面开始截取的方式
print("截取字符串JianShi的:%s"%title[-7:])
#截取全部字符的方式
print("截取全部字符:%s"%title[0:])

#使用步长隔一个字符开始截取
print("使用步长字符:%s"%title[0::2])

#面试题：给定一个字符串翻转字符串(每次从最后一个字母往前步长-1)
print("翻转字符串:%s"%title[-1::-1])
```

3、字符串常用函数调用的操作

    a、find()和index()   查找字符串
    
```python
title = "hello I will print hello world"
#打印结果为"8"表示该字符串的下标从第八开始
print(title.find("will"))
#查找不存在的字符串就会返回"-1"
print(title.find("dkkd"))
#如果有多个相同的，只从左边开始查找第一个
print(title.find("hello"))
#从右边查找"hello"使用rfind()
print(title.rfind("hello"))

#另一种查找方式与find()不同之处在于，这种方式查找不存在的字符串会报错
print(title.index("print"))
#从右边开始查找
print(title.rindex("print"))
```

    b、count()  统计字符串出现的次数
    
```python
title = "hello I will print hello world"
print(title.count("hello"))
```

    c、replace() 查找替换字符串，并且如果有多个相同的字符串，也会被全部替换
    
```python
title = "hello I will print hello world"
print(title.replace("hello", "python"))

#只替换一个
print(title.replace("hello", "python" , 1))
```

    d、split() 按照某个字符进行分隔成多个字符的列表，进行分割的字符不再显示
               也可指定分隔多少个字符串，比如输入参数"2"则表示分割成三个字符串
                
```python
title = "hello I will print hello world"

print(title.split("I"))
#要想使选中的分隔符显示，则使用partition()函数
print(title.partition("I"))
print(title.split(" " , 2))
```          
    

