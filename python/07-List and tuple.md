1、列表:list是一种有序的集合，可以随时添加和删除其中的元素。

    * 用len()函数可以获得list元素的个数

```python
lines = ["人生", "苦短" , "我要学" , "python" , "01"]
print(len(lines))
```    
    * 用索引来访问list中每一个位置的元素，记得索引是从0开始的
    
2、列表的相关操作(增、删、改)

    * 添加元素(append, extend, insert)
        append 可从列表的末尾添加
        extend 可将令一个集合中的元素逐一添加到列表中(两个列表的合并)
        insert 在指定的index位置前面插入元素
     
```python
lines01 = ["人生", "苦短" , "我要学" , "python"]
lines02 = ["html", "css"]

# lines01.append("java")
lines01.extend(lines02)

print(lines01)

lines02.insert(1 , "and")
print(lines02)
``` 

    * 查找元素(in , not in , index , count)： 根据下标位置查找元素
      in 和 not in 是判断是否存在某个元素的；
      index 用来查找元素下标；
      count 因为列表元素可以相同，所以可以使用count查找有几个
      
```python
lines01 = ["人生", "苦短" , "我要学" , "python"]
print(lines01[2])

print(lines01.index("苦短"))
```  

    * 删除元素(del , pop , remove)
      del 是python的内置函数，不是列表中的函数，可根据下标进行删除
      pop() 默认删除最后一个元素,并把删除的元素返回
      remove() 根据列表的内容进行删除
      
  ```python
lines01 = ["人生", "苦短" , "我要学" , "python"]
del lines01[3]

lines01.pop()

lines01.remove("人生")
```

    * 排序(sort , reverse)
      sort() 是将list按照特定的顺序重新排列，默认为从小到大即升序，参数reverse=True,可改为倒序。
      
  ```python
lines01 = ["人生", "苦短" , "我要学" , "python"]
lines01.sort(reverse=True)
print(lines01)
``` 

```python
print("*"*30)
print("学生名字管理系统".center(50))
print("输入1：表示添加学生")
print("输入2：查找学生名字")
print("输入3：修改学生名字")
print("输入4：删除学生名字")
print("输入5：退出")

stus = []
while True:
    operate = input("请输入你想要进行的操作:")
    if operate == "1":
        name = input("请输入添加的学生姓名:")
        stus.append(name.strip())
    if operate == "2":
        pass
    if operate == "3":
        pass
    if operate == "4":
        name = input("请输入要删除的学生姓名:")
        if  name not in stus:
            print("你输入的学生%s不存在"%name)
            continue
        else:
            stus.remove(name)
            print(stus)
    if operate == "5":
        break
```

3、元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

    它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
    * 访问元组可通过下标；
    一、 定义一个只有1个元素的tuple
```python
t = (1,)
```
    二、元组是不可变的，如果要想变的可变，可在元组中添加list列表

```python
t = ("a" , "b" , ["100" , "200"] , "c")
```  

```python
i = 1
while i <= 5:
    j = 0
    while j < i:
        print("*" , end="")
        j += 1
    print("")
    i += 1

k = 5
while k >= 1:
    w = 1
    while w <= k:
        print("*" , end="")
        w += 1
    print("")
    k -= 1
    
#结果如下
'''
*
**
***
****
*****
*****
****
***
**
*
'''
```  

```python
#只有调用了才会显示里面的元素
c = range(1 , 10)
```


