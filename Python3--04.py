Python3基础知识4（循环和注释）

（1）while循环

#当某个条件成立时，一直执行某个动作，语法如下：

while 条件表达式:
　　循环代码

#条件表达式结果为True的时候 循环代码会一直执行
#知道条件表达式结果为False

while True:
　　if(input('input is a ?')=='a'):
　　　　break
注意：上面代码为死循环，只有输入a时才会终止程序。

#简单打印出1到100数字

cur = 1
while cur <= 100:
　　print(cur)
　　cur += 1

#打印所有学生信息['Mike','Jack','Luoqian','Chenzi','Liqian']
arr1 = ['Mike','Jack','Luoqian','Chenzi','Liqian']
i=0
while i < len(arr1):
　　print(arr1[i])
　　i += 1

（2）for循环

#打印所有学生信息['Mike','Jack','Luoqian','Chenzi','Liqian']
arr1 = ['Mike','Jack','Luoqian','Chenzi','Liqian']
for stu in arr1:
　　print(stu)#stu就代表列表中的元素

注意：以上两个实例对比可以看出while循环需要变量，需要自增1.

补充：Python2 range xrange 两者的区别
#range 函数返回的是一个列表，而xrange 像一个生成器
#如果需要遍历一个很庞大的数字范围，用xrange，因为节省内存
#Python3 中的range 类似Python2 中的xrange

for stu in range (1,101,10):
# 包左不包右，取1到100,后面的10为步进数,即每隔10位数打印一次
#打印结果为：1，11， 21， 31， 41...
　　print(stu)
　　
注意：如果步进数为负数的情况
for stu in range (101,1,-10):
#打印结果为：101， 91， 81, 71...
　　print(stu)

（3）break语句：本层循环到了指定条件后不再往后循环，如果还有其它外层或内层循环并不影响

sumdata = 0
for i in range(1, 101):
　　sumdata += i
　　if i == 50:
　　　　break#结束本层循环
print(sumdata)

（4）contiune语句：结束本次循环，之后的再往后循环，如果还有其它外层或内层循环并不影响

（5）注释
#注释方法一：使用“#”

#注释方法二：多行注释用三引号''' '''

#注释方法三：函数的注释

def fun():
　　#函数的属性
　　"this is doc"
　　print("函数！")
print(fun.__doc__)

#打印后会显示里面的"this is doc"属性解释

 