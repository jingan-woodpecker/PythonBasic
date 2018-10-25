1、给程序传参数

```python
import sys
#argv保存了传递给程序的参数，第一个参数就是文件本身
print(sys.argv)

#['D:/python3/webdriverAPI/pratices/forward/test.py']
```

2、列表推导式也称为集合推导式(书写一个表达式，专门生成列表/字典/元组的)

    * 使用轻量级的循环生成列表
```python
#每次循环都打印数字i
get_num = [i for i in range(1,10)]
print(get_num)

#[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
#每次循环都打印数字i的平方的值
get_num = [i**2 for i in range(1,10)]
print(get_num)

#[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
#两个for循环，注意嵌套关系
get_num = [i for i in range(1,4) for j in range(0,3)]
print(get_num)

#[1, 1, 1, 2, 2, 2, 3, 3, 3]
```

```python
get_num = [(i,j) for i in range(1,4) for j in range(0,3)]
print(get_num)

#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
```

```python
get_num = [(i,j,z) for i in range(1,3) for j in range(0,2) for z in range(6,8)]
print(get_num)
#[(1, 0, 6), (1, 0, 7), (1, 1, 6), (1, 1, 7), (2, 0, 6), (2, 0, 7), (2, 1, 6), (2, 1, 7)]
```

```python
get_num = [i for i in range(1,30) if i%2==0 ]
print(get_num)

#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
```

总结：

    列表推导式中，先看for循环的内容，再看条件判断的代码，最后才看输出结果
  
3、set:集合类型(a = {})

```python
a = {1,2,4,3,6,6,2,4,1}
print(a)
#{1, 2, 3, 4, 6}

#空set
b = set{}
```
    
    使用set,可以快速的完成对list中元素去重复的功能
    注意：set集合  没有先后顺序，没有下标，不可重复，可变类型  
练习

    1、生成一个[[1,2,3],[4,5,6]...]的列表最大值在100以内
    2、在python中类和对象有什么区别？对象如何访问类的方法？创建一个对象时做了什么？
    3、写出一段python代码实现删除一个list里面的重复元素
    4、设计实现遍历目录与子目录，抓取.pyc文件
    5、写出一个函数给定参数n生成n个元素值为1到n的列表，元素顺序随机，但值不重复
    6、在不用其他变量的情况下，交换a,b变量的值
    7、如何在function里面设置一个全局变量
    8、如下代码会输出什么？
    
```python
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,['a','b','c'])
list3 = extendList('a')
print("list1 = %s"%list1)
print("list2 = %s"%list2)
print("list3 = %s"%list3)
```

```python
#第一题
import pprint
a = [1, 2, 3]
get_num = [[a[0]+i , a[1]+i , a[2]+i] for i in range(0,97) if i%3==0 ]
pprint.pprint(get_num)
```

第二题
    
    类实际上就好比一个事物的模型，对象就是用这个模型创建出来的具体事物，
    对象可以直接访问类，创建对象首先回调new，再回调__init__方法
    
第三题(不使用set方法)

```python
def change_list(li):
    temp = []
    for i in li:
        if i not in temp:
            temp.append(i)
    return temp

if __name__  == "__main__":
    a = [1,3,6,5,6,7,1,55,3,7,55,3]
    print(change_list(a))
    
    #[1, 3, 6, 5, 7, 55]
```

第五题
```python
import random
def creat_list(n):
    temp = []
    while True:
        if len(temp) == n:
            break
        i = random.randint(1,n)
        if i not in temp:
            temp.append(i)
    return temp
if __name__ == "__main__":
    print(creat_list(8))
```

第八题

    list1 = [10, 'a']
    list2 = ['a', 'b', 'c', 123]
    list3 = [10, 'a']
    
    首先参数list是可变类型的，当list1接收到值后，原先默认的参数list=[],被改为了list=[10]
    所以，在list3接收值的时候追加了字符串"a"，然后返回list3=[10,'a'],又因为内存地址不变list1的值也一样
    