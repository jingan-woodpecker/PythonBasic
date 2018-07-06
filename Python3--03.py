Python3基础知识3（字符串的格式化和用户输入）

#简单的输出
name = 'tom'
height = 190

print('我的名字是' + name + ',身高有' + str(height) + 'cm')

print ('age is' + str(16))

（1）了避免批量使用这种输出方式，引入格式化输出

print('我的名字是%s, 身高有%scm' %('tom',190))

注意：tom 不加引号相当于变量会报错，%s就相当于 string类型，所以数值 190 不需要加引号
%('tom',190)) 后面接的是元组，不可以接列表格式

识记：常用的字符串格式化符号
1、 %s 用str()函数进行字符串转换；
2、 %d 转成有符号十进制数；（如果有小数会自动忽略）
>>>print('age is %x' % 3.14159269)
age is 3

3、 %f 转成浮点数（小数部分自然截断）；默认保留六位数
#若要输出超出六位数
>>>print('age is %.7f' % 3.14159269)
age is 3.1415927

4、 %x 转成无符号十六进制（x/X代表转换后的十六进制字符的大小写）。
>>>print('age is %0x' % 64)
age is 40

#补充：
a = [('tom',7000),('jack',20000)]
fs = '''
%s salary: %d $
%s salary: %d $
'''

print(fs % (a[0][0],a[0][1],a[1][0],a[1][1]))

#打印结果
tom salary: 7000 $
jack salary: 20000 $

#目标为了让薪资对齐的方法

a = [('tom',7000),('jack',20000)]
fs = '''
%10s salary: %d $
%10s salary: %d $
'''

# s前面添加整数10，表示左边添加了空格，打印结果如下
tom salary:7000 $
jack salary: 20000 $

#如果添加了负数，则在右边添加空格，打印结果如下
tom salary: 7000 $
jack salary: 20000 $

#也可在薪资前面补零，打印结果如下
%-10s salary: %6d $
%-10s salary: %6d $

tom salary: 007000 $
jack salary: 020000 $

注意：其中数字6是指本来7000只有四位数先补到6位，多出空格后再补零

#指定宽度
>>>'%10d' % 56 #最小宽度，不足空格补齐
' 56'

#补零
>>>'010d' % 56 #补零
'0000000056'

#十六进制(加#和大小写x的区别）
>>>"%#X" % 108
'0X6C'

>>>"%#x" % 108
'0x6c'

#小数注意点
>>>print('date is %8.2f' %123.456789)
date is 123.46

>>>print('date is %08.2f' %123.456789)
date is 00123.46


（2）format格式化方法

>>>print('name is {} and {} years old'.format('tom',18)) #{}相当于先占位，然后再把tom导入进去
'name is tom and 18 years old'

#可以使用输入下标的方法(.是调用的意思）

>>>'I am {1} years old, my name is {0}'.format('tom',18)
'I am 18 years old, my name is tom'
format % values

>>>'{1} - {0}'.format('tom',18)
'tom 18'

#指定宽度
>>>'{}'.format(56)
'56'

>>>'{:10}'.format(56)
' 56'

>>>'{:<10}'.format(56) #左对齐
'56 '

>>>'{:010}'.format(56)
'0000000056'

#十六进制
>>>'{:x}'.format(108)
'6c'

>>>'{:X}'.format(108)
'6C'

>>>'{:#x}'.format(108)
'0x6c'

#小数
>>> '{}'.format(123.456789)
'123.456789'

>>>'{:.2f}'.format(123.456789)
'123.46'

>>>'{:9.2f}'.format(123.456789)
' 123.46'

>>>'{:09.2f}'.format(123.456789)
'000123.46'

>>>'{:09.2f} {{}}'.format(123.456789) #如果字符串本身就有花括号
'000123.46 {}'

Python3新增方式（注意大括号书写）
>>>name = 'tom'
>>>f'name is {name}'
'name is tom'

（3）字符串里的转义符

>>>'name is \'tom\''
"name is 'tom'"

>>>print('line1\nlime2') #换行符
line1
line2

>>>print('\x4F\x50\x51\x52\x53\x54')
OPQRST

>>>print(r'\x4F\x50\x51\x52\x53\x54')
\x4F\x50\x51\x52\x53\x54

（4）字符终端输入
input() 内置函数，返回的是string类型

>>>name = input('shuru:')
shuru:123
>>>name
'123'

>>>int(name) #转换类型
123

简写
>>>int(input('shuru:'))
shuru:123
123

- python 3 执行下面格式化字符串的代码，哪些是会报错的 (b)
A) "my name is {0}, I'm {1} years old.".format('Mike',5) 
B) "my name is {}, I'm {1} years old.".format('Mike',5) 
C) "I'm {1} years old, my name is {0}".format('Mike',5) 
D) "my name is {0}, his name is also {0}".format('Mike') 
E) f"my name is {'Mike'}, his name is also {{Mike}}"

 