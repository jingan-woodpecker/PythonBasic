1、while循环 当某个条件成立时，一直执行某个动作，语法如下：

    while 条件表达式:
            循环代码
    print("循环外")

    条件表达式结果为True的时候 循环代码会一直执行，直到条件表达式结果为False
    注意：上面的print内容不在循环内，即无论循环执不执行都会执行print()内容.
    
```python
#从1加到100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("从1加到100的和是：%s"%sum)
#若是"i+=1"忘记书写，则会进入死循环
```
```python
#从1到100之间偶数的和
i = 1
sum =0
while i <= 100:
    if i%2 == 0:
        sum += i
    i += 1
print("从1加到100的偶数和是：%s"%sum)
```

2、while嵌套循环

        while 条件表达式1:
                  条件1满足时，做的事情1
                  条件1满足时，做的事情2
                  条件1满足时，做的事情3
                  ..(省略)...
                  
                  while 条件表达式2:
                  条件2满足时，做的事情1
                  条件2满足时，做的事情2
                  条件2满足时，做的事情3
                  ..(省略)...

```python
#用"*"打印5行5列的矩形
i = 1
while i <= 5:
    j = 1  #注意：需要在这里重置j=1
    while j <= 5:
        print("*",end="")  #print函数默认情况下输出就换行，若要不换行加入end=""
        j += 1
    print("")  #换行
    i += 1
print("5行5列的矩形打印完成")
```

```python
#打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d\t"%(j , i , i*j),end="" )
        j += 1
    print("")
    i += 1
print("九九乘法表打印完成")
```

```python
#用"*"打印一个等边的倒三角形，并且行数由用户输入
i = int(input("输入的行数是:"))
j = 0   #循环次数
while j < i:
    x = 0   #空格数
    while  x < j:
        print(" " , end="")
        x += 1

    y = i-j  #注意
    while y > 0:
        print("*" , end=" ")
        y -= 1
    print("")
    j += 1
print("倒三角打印完成")
```
    总结：
        1、循环的次数(while循环次数由条件决定)
        2、在循环过程中做什么
        3、变量怎么变化

3、循环中常用关键字：break和continue用法

    (1)break 可以提前(强制)退循环

```python
age = int(input("请输入年龄："))
i = 1
while True:
    if i == age:
        print("你的年龄为：%d"%i)
        break
    else:
        print("猜错了")
    i += 1
```

    (2)continue 终止当前这次循环，开始下一次循环
    
```python
#打印1-10之间的奇数
i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        # print("当前数字%s是偶数"%i)
        continue #满足条件后，终止本次循环，后面的代码也不运行。
    print("当前数字%s是奇数"%i)
```