1、可变类型和不可变类型

可变类型：列表、字典
不可变类型：数值、字符串、元组

```python
a = 100
a = 200
print(id(a))
print(id(a))
print(a)
"""
结果如下:因为数值是不可变类型，所以它由刚开始的a指向100，到a指向200,a=100并没有消失，只是换了一个指向；如果长时间没有指向a=100后，python则会回收
1697744576
1697744576
200
"""
```

2、字典：dict全称dictionary，在其他语言中也称为map，

    使用键-值（key-value）存储，缺一不可，具有极快的查找速度
    特点：键是不允许重复的；值可以重复，字典没有顺序，所以没有下标的概念。
    
    * 通过键访问字典的方式，如果访问的键不存在会报错，使用get()方法就不会报错
    
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
print(student["age"])

print(student.get("dddd"))
```

3、字典的常见操作

    * 新增元素
    
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
student["address"]="guangdong"
print(student)
```

    * 查找元素(in not): 注意是判断一个键是否在字典中
    
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
print("sex" in student)
```

    * 删除元素(del): 可以根据键删除,使用clear内存不回收
    
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
del student["name"]
```

```python
student = ["zhangsan" , 23 , "男"]
student01 = ("小竹" , 20 , "女")

i = 0
#第一种迭代，显示序号
print("序号\t学生信息")
for stu in student:
    i += 1
    print("%s\t%s"%(i , student))

print("="*30)
#第二种枚举法
for st , item in enumerate(student01 , 1):
    print("%s\t%s" % (st , item))
```

3、字典中常见函数
    
    * len() 测量键值对的个数
    * keys() 返回一个包含字典所有key的列表:主要用来查询看键然后判断，新插入的键会不会重复
    
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
print(student.keys())
```
    * values() 返回一个包含字典所有value的列表
    
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
print(student.values())
```

    * 打印key和value
```python
student = {"name":"zhangsan" , "age": 23 , "sex":"男"}
for item in student.items():
    print("key为%s,value为%s"%item)#item其实就是元组，包含两个值
    
'''
key为name,value为zhangsan
key为age,value为23
key为sex,value为男
'''
```