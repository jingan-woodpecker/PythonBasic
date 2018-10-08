1、输入

    input()方法可以让用户输入字符串，并放到一个变量里
    
```python
#encoding=UTF-8
#python3中输入的内容是作为字符串的,而python2输入的内容是作为表达式的
name = input("请输入姓名为：")
age = input("输入你的年龄：")

print("我的姓名是%s,年龄%s岁"%(name,age))
```

2、运算符

    a  加(+)、减(-)、乘(*)、除(/)、取整除(//)、取余(%)、幂(**)
    b  赋值运算符(=)
    c  复合赋值运算符(+=、-=、*=、/=、%=、//=、**=)
    
```python
a = 3
a *= 4+6-7
print(a)

#以上运行结果为：9  
#是先将右边的表达式执行完了，再赋值给左边的a
```

```python
#让用户输入自己的姓名、年龄、地址，并且判断输入的年龄是偶数
name = input("请输入姓名为：")
age = int(input("输入你的年龄："))
address = input("家庭住址是：")

if age%2==0:
    print("我的姓名是%s,年龄%s岁,地址是%s"%(name,age,address))
else:
    print("年龄不是偶数")
```