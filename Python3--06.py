Python3基础知识6（循环嵌套、列表生成式、简单冒泡排序）

（1）循环嵌套

girls = ['YuShan','ChenZi','LuoQian']
boys = ['Mike','Jack','Tom']
for boy in boys:#外循环
　　for girl in girls: #内循环
　　　　print('%s shakes %s' %(boy,girl))

#先执行外循环一次取到“Mike”，再执行内循环一遍，就是依次取出girls的值，才第二次执行外循环 打印结果如下：
Mike shakes YuShan
Mike shakes ChenZi
Mike shakes LuoQian
Jack shakes YuShan
Jack shakes ChenZi
Jack shakes LuoQian
Tom shakes YuShan
Tom shakes ChenZi
Tom shakes LuoQian

#员工税前工资列表：[10000, 15000, 8000, 4000, 5000]
#每个员工扣税10%
#请计算出所有员工的税后工资，存储在列表中

beforetax = [10000, 15000, 8000, 4000, 5000]
aftertax =[]
for one in beforetax:
　　aftertax.append(one*0.9)
print(aftertax)


（2）列表生成式 List comprehensions
#典型的从源列表生成目标列表的处理场景
#从源列表中，一次取出元素
#做同样的处理
#放入另一个列表中

beforetax = [10000, 15000, 8000, 4000, 5000]
aftertax = [one*0.9 for one in beforetax]
aftertax = [int(one*0.9) for one in beforetax]
print(aftertax)

#注意：如果想小数变成整数可以使用转换数据类型方法
#总结就是for循环放在后面，处理语句结果放在前面

#加上过滤条件

beforetax = [10000, 15000, 8000, 4000, 5000]
aftertax = [one*0.9 for one in beforetax if one>= 10000]
print(aftertax)

（3）简单冒泡排序
'''
[3,5,7,26,4]假设总共n个元素
第一轮：
对所有的n个元素（从a[0]到a[n-1]),比较流程：
依次比较，相邻的两个元素，大的移到后面，先
a[0]和a[1]比较，如果a[0]>a[1]，交换位置，然
后a[1]和a[2]
得出最大的元素就到了a[n-1]

第二轮：
除了最后一个元素，剩余的n-1个元素（a[0]到a[n-2]）里面比较流程
得出最后第二大的元素就到了a[n-2]

以此类推，直到第n-1轮
'''
alist = [3,5,7,26,4]
def bubble(alist):
　　# j代表元素的下标，从最后一个元素到第二个元素,确定循环次数
　　for j in range(len(alist)-1,0,-1):
　　　　# 第一轮的比较是所有元素的比较，第二轮是n-1个元素
　　　　for i in range(0, j): #从0到5，就是4次比较...
　　　　　　if alist[i] > alist [i+1]:
　　　　　　　　alist[i],alist[i+1] = alist[i+1],alist[i]#调换位置
　　return alist
bubble(alist)
#还需要打印
print(alist)

另外一种排序

#1、创建一个新的列表newList[]
#2、先找出所有元素中最小的，append在newList里面-----min
#3、再找出剩余的所有元素中最小的，append在newList里面--找到了就删除存入
#4、依次类推，直到所有的元素都放到newList里面

alist = [2,4,11,156,88,9,6,19]
countNum = len(alist)#固定!
outList = []#存储排序后的排序
i = 0
while i < countNum:
　　minNum = min(alist)#取列表最小值
　　outList.append(minNum)#添加进新列表
　　alist.remove(minNum)#删除原列表中取出的最小值，否则循环后一直取到这个值
　　i += 1
print(outList)

注意：如果列表中元素相同，则下标小的排在前.

补充：pass关键字（定义一个空语句）
def meth_a(self):
　　pass

def meth_b(self):
　　prit('hello')

函数里面调用函数

def fun():
　　pass
　　test()

def test():
　　print('hahhaha')
　　fun()


练习：
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面


def sort(inList):
　　newList = []

　　# 设计一个循环，每个循环做如下事情（直到 inlist 没有元素）：
　　# 找出当前inlist中所有元素中最小curMin的，append在newList里面

　　# inList 去掉 curMin

　　while len(inList) > 0:
　　　　theMin = inList[0] # 记录当前循环最小元素
　　　　minIdx = 0 # 记录当前最小元素的下标
　　　　idx = 0 # 指向当前元素下标
　　　　for one in inList:
　　　　　　if theMin > one:
　　　　　　　　theMin = one
　　　　　　　　minIdx = idx

　　　　　　idx += 1

　　　　inList.pop(minIdx)
　　　　newList.append(theMin)

　　return newList

print (sort([1,3,5,7,34,23,55,56,2,3,4]))


练习：

现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下

name: Jack ; salary: 12000
name :Mike ; salary: 12300
name: Luk ; salary: 10030
name :Tim ; salary: 9000
name: John ; salary: 12000
name: Lisa ; salary: 11000

每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格

现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示

name: Jack    ;     salary:   12000 ;   tax:  1200   ;  income:   10800
name: Mike    ;     salary:   12300 ;   tax:  1230   ;  income:   11070
name: Luk      ;    salary:    10030 ;   tax:  1003   ;  income:     9027
name: Tim      ;    salary:      9000 ;   tax:    900   ;  income:    8100
name: John    ;    salary:    12000 ;   tax:  1200   ;  income:   10800
name: Lisa     ;    salary:    11000 ;   tax:   1100   ;  income:     9900

要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数

#因为路径中\的显示需要用到转义字符，或者路径前面添加 r
inFileName = r'D:\learn\file1.txt'
outFileName = r'D:\learn\file2.txt'
#打开文件1只读，文件2可写并重新命名
with open(inFileName) as ifile, open(outFileName,'w') as ofile:
　　#清除换行符
　　beforeTax = ifile.read().splitlines()
　　for one in beforeTax:
　　　　#判读不等于一个分号的时候coutinue
　　　　if one.count(';') != 1:
　　　　　　continue
　　　　# name Part like name: Jack | salaryPart like salary: 12000]
　　　　#以';'分隔两边的信息
　　　　namePart,salaryPart = one.split(';')
　　　　if namePart.count(':') !=1:
　　　　　　continue
　　　　if salaryPart.count(':') !=1:
　　　　　　continue
　　　　#名字和薪资信息都以':'分隔，再取下标为1的名字和薪资，并且清除前后的空格
　　　　name = namePart.split(':')[1].strip()
　　　　salary = int(salaryPart.split(':')[1].strip())
　　　　#将税后薪资和扣税金额存入变量中
　　　　income = int(salary*0.9)
　　　　tax = int(salary*0.1)
　　　　#格式化输出内容
　　　　outPutStr ='name:{:10} ; salary:{:6} ; tax:{:6} ; income:{:6}'.format(name,salary,tax,income)
　　　　print (outPutStr)
　　　　#将输入内容写入file2.txt文件中
　　　　ofile.write(outPutStr + '\n')