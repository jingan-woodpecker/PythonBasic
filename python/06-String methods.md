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

    e、capitalize()  将字符串的第一个字母转换成大写
    
```python
title = "hello I will print hello world"
print(title.capitalize())
```  

    f、title() 将字符串的每个单词首字母大写
    
```python
title = "hello I will print hello world"
print(title.title())
```

    g、startswith() 检查字符串是否以什么开头，是则返回True,否则返回False
       endswith()  检查字符串是否以什么结尾，是则返回True,否则返回Fal
       比如检查是否是指定的.txt、.css文件结尾等  
       
```python
title = "hello I will print hello world.txt"
print(title.startswith("h"))
print(title.endswith(".txt"))
```    

    h、lower() 将所有大写字符转换为小写
       upper() 将所有小写字符转换为大写
       
    比如用于当用户输入验证码后先将其全部转换为大写或小写
    
```python
title = "HeadFirst Html and CSS"
print(title.lower())
print(title.upper())
```
    i、ljust() 返回一个字符串左对齐，并使用空格填充指定长度的新字符串
       rjust() 返回一个字符串右对齐，并使用空格填充指定长度的新字符串
       center() 返回一个字符串居中，并使用空格填充指定长度的新字符串
         
```python
title = "HeadFirst Html and CSS"
print(title.ljust(50))
print(title.rjust(50))
#可使用0填充
print(title.center(50 , "0"))
```
    j、rstrip() 删除右边空白字符
       lstrip() 删除左边空白字符
       strip() 删除前后空白字符

```python
title = "      HeadFirst Html and CSS  "
print(title.rstrip())
print(title.lstrip())
print(title.strip())
```
    k、splitlines() 按照换行符分隔，返回一个包含各行作为元素的列表
    
```python
lines = "HeadFirst\nHtml and CSS\nZhongGuo JianShi"
print(lines.splitlines())

#结果如下
#['HeadFirst', 'Html and CSS', 'ZhongGuo JianShi']
```

    l、isalpha() 判断所有字符是否都是字母，是返回True,否返回False
       isdigit() 判断所有字符是否都是数字，是返回True,否返回False
       isalnum() 判断所有字符是否是字母或数字，是返回True,否返回False
       isspace() 判断是否只包含空格，是返回True,否返回False

```python
lines = "    "
lines_one = "alphaANDnumber1245345"
lines_two = "53465543737"
print(lines_one.isalnum())
print(lines_two.isdigit())
print(lines.isspace())
```

    o、 join()  在每个字符的后面定义用什么连接起来，形成一个新的字符串
    
```python
lines = ["人生", "苦短" , "我要学python"]
print("".join(lines))
print("--".join(lines))

#结果如下
#人生苦短我要学python
#人生--苦短--我要学python
```