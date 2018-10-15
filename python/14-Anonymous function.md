匿名函数：用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。

    lambda函数的语法只包含一个语句，如下：
    lambda [arg1 [,arg2,.....argn]]:expression
    
    * Lambda函数能接收任何数量的参数但只能返回一个表达式的值

    * 匿名函数不能直接调用print，因为lambda需要一个表达式
    
```python
#匿名函数一定要可以接收，才可以调用
func = lambda x , y : x+y
print(func(10 , 48))
```

应用场合

    * 动态传入，将列表中的字典按value进行排序
    
```python
students = [{"name":"小竹" , "age":24 , "sex":"女"},
            {"name":"王贤" , "age":19 , "sex":"男"},
            {"name":"陈东" , "age":25 , "sex":"男"},
            {"name":"李琴" , "age":34 , "sex":"女"}
            ]
#按key的值，取value的值，进行排序比较
students.sort(key=lambda x:x["name"])
print(students)
```

1、打印乘法表

```python
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d\t"%(j, i, i*j),end="")
        j += 1
    print("")
    i += 1
```

2、判断闰年

    请用函数实现一个判断用户输入的年份是否是闰年的程序

    提示：
    1.能被400整除的年份 
    2.能被4整除，但是不能被100整除的年份
    以上2种方法满足一种即为闰年

```python
num = int(input("请输入年份："))
if (num%400 == 0) or (num%4 == 0 and num%100 !=0):
    print(num)
else:
    print("你输入的%s不是闰年"%num)
```
    