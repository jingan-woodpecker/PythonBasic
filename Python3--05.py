Python3基础知识5（文件的读写）

（1）文件对象
#不同类型，会产生不同类型的对象
整数类型的对象
字符串类型的对象
字典类型的对象
元组类型的对象
布尔类型的对象
range类型的对象（序列的一种）

#文件的读写通过文件操作对象进行
Python2 File Python3 TextOWrapper

#内置函数open打开文件，获取文件操作对象

#文件的打开
file_object = open(file_name, access_mode ='r') #

>>>file_object = open('./a.java','r') #只是打开文件，并不读，所以无法看到内容, 也可这样写： file_object = open('./a.java')这叫缺省的文件打开方式
<_io.TextIOWrapper name='a.java' mode='r' encoding='cp936'> 

注意： file_name 为文件路径：相对路径和绝对路径;
access_mode 可分为：读（定义时等于号指定的值，缺省参数）、写、读+写

补充：（./表示当前文件， ../表示上一层）
windowns系统中一些常用cmd 命令
cd # 显示当前目录
cd .. # 进入父目录
cd /d d: # 进入上次d盘所在的目录（或在直接输入：d:）
cd /d d:\ # 进入d盘根目录
dir #显示当前目录中的子文件夹与文件

（2）文件指针的概念：文件对象的.tell方法获取文件指针的位置

>>>file_object.tell() #这样默认指针在0起始位置
0

假设a.java文件内容为：
abcdef
1235445d
廖竞安

#读取前三个操作
>>>file_object.read(3)
'abc'

#读取当前指针位置全部内容
>>>file_object.read()
'def\n1235445d\n廖竞安\n' #因为上一次读取了前三个后光标没有归零，所以现在读取的内容缺少‘abc’

#关闭文件
>>>file_object.close()

#seek参数：文件指针的移动
>>>file_object = open('bac')
>>>file_objeck.seek(2)
2

注意：不可以使用负号移动回原来的位置，要想移动回起始位置直接输入
>>>file_objeck.seek(0)
0

os.SEEK SET or 0 (absolute file positioning);
os.SEEK CUR or 1 (seek relative to the current position)
os.SEEK END or 2 (seek relative to the file's end).

#Python3里面，后两种定位方式，打开文件时，一定要以二进制的方式打开
例如： open('a.java', 'br')

>>> file_object = open('a.java','br')
>>> file_object.seek(-2,2) #数字2表示在模式二中打开的文件，并从后面算起且换行符算2个元素，所以-2表示倒数第二个元素
24

总结：
>>>file_object = open('a.java','rb')
>>>file_object.seek(0,2) #移动到文件末尾，后面的第二个数都是表示模式
>>>file_object.seek(-2,2) #移动到文件倒数第二个字符
>>>file_object.read()

>>>file_object.seek(0) #移动到头
>>>file_object.seek(2,1) # 移动到当前指针后两个字符
# readline 读取一行

>>> file_object = open('a.java')
>>> str1 = file_object.readline()
>>> str1
'123456\n' 

>>> str2 = file_object.readline()
>>> str2
'abcdef\n'

>>> file_object.close()

# readlines 读取所有行

>>> file_object=open('a.java')
>>> lines = file_object.readlines()
>>> lines
['123456\n', 'abcdef\n', '更新换代\n', '\n']

#去掉\n的方法 

>>> file_object=open('a.java')
>>> lines = file_object.read().splitlines()
>>> lines
['123456', 'abcdef', '更新换代', '']

#写打开方式
# w 只是为了写文件而打开文件。如果文件已经存在，其内容将被清空，如果不存在，则创建一个文件
>>> file_object = open('a.java','w')
>>> file_object.write('49558')
5 #只是显示你写入了多少字符，实际文件中并不显示‘49558’内容，因为它被写到缓存区中了

#强行写入方法
>>> file_object.flush() #file_object.close()关闭的时候也会将内容写入

#追加打开方式 a
只是为了在文件末尾追加内容而打开文件
如果文件存在，文件指针在文件的结尾
如果文件不存在， 则创建一个文件

注意：很多OS强制写都在末尾，不管文件指针被seek到了什么地方

>>> file_object = open('a.java','a')
>>> file_object.write('sjdl')
4

#读写打开方式
# r+ 为了读取并写文件而打开文件，不存在会报错，文件指针在开头

# w+ 为了读取且写文件而打开，不存在会创建，指针在开头，存在内容被清空

# a+ 为了读取并写文件而打开， 不存在会创建，指针在末尾。

注意：上面三种方法不常用

（3）文件打开的另外一种方法
with open 方法
with open('a.java','r') #跟上一种方法的不同之处在于，这种方式关闭不需要.close()


>>> file.close() 

---------------------------------------------------------------------练习

两个文件。 一个叫 'gbk编码.txt',
该文件是gbk编码的。
另一个文件叫 'utf8编码.txt', 该文件是utf8编码的。
两个文件里面的内容都包含中文。

要求大家编写一个python程序，该程序做到以下2点

1. 将两个文件内容读出， 合并内容到一个字符串中，
并能用print语句将合并后的内容正确显示

2. 然后，程序用中文提示用户“请输入 新文件的名称”，
用户输入文件名可以包含中文
将上面合并后的内容存储到一个新文件中，以utf8格式编码。
新文件的文件名就是上面用户输入的名字。
---------------------------------------------------------------------------
cfile文件夹中的gbk编码.txt文件中包含的内容是“李老师年龄：32
utf8编码.txt文件包含的内容是“张老师年龄：28”


# 根据不同的编码格式，指定参数
with open('D:/cfiles/gbk编码.txt',encoding='gbk') as f1, \
open('D:/cfiles/utf8编码.txt',encoding='utf8') as f2:

# read后，自动转化成unicode
content1 = f1.read()
content2 = f2.read()

newContent = content1 + content2
print(newContent)

newFile = input('请输入新文件的名称:')

with open(newFile,'w',encoding='utf8') as f:
f.write(newContent)

#打印结果
李老师年龄：32张老师年龄：28
请输入新文件的名称: