Python3����֪ʶ3���ַ����ĸ�ʽ�����û����룩

#�򵥵����
name = 'tom'
height = 190

print('�ҵ�������' + name + ',�����' + str(height) + 'cm')

print ('age is' + str(16))

��1���˱�������ʹ�����������ʽ�������ʽ�����

print('�ҵ�������%s, �����%scm' %('tom',190))

ע�⣺tom ���������൱�ڱ����ᱨ��%s���൱�� string���ͣ�������ֵ 190 ����Ҫ������
%('tom',190)) ����ӵ���Ԫ�飬�����Խ��б��ʽ

ʶ�ǣ����õ��ַ�����ʽ������
1�� %s ��str()���������ַ���ת����
2�� %d ת���з���ʮ���������������С�����Զ����ԣ�
>>>print('age is %x' % 3.14159269)
age is 3

3�� %f ת�ɸ�������С��������Ȼ�ضϣ���Ĭ�ϱ�����λ��
#��Ҫ���������λ��
>>>print('age is %.7f' % 3.14159269)
age is 3.1415927

4�� %x ת���޷���ʮ�����ƣ�x/X����ת�����ʮ�������ַ��Ĵ�Сд����
>>>print('age is %0x' % 64)
age is 40

#���䣺
a = [('tom',7000),('jack',20000)]
fs = '''
%s salary: %d $
%s salary: %d $
'''

print(fs % (a[0][0],a[0][1],a[1][0],a[1][1]))

#��ӡ���
tom salary: 7000 $
jack salary: 20000 $

#Ŀ��Ϊ����н�ʶ���ķ���

a = [('tom',7000),('jack',20000)]
fs = '''
%10s salary: %d $
%10s salary: %d $
'''

# sǰ���������10����ʾ�������˿ո񣬴�ӡ�������
tom salary:7000 $
jack salary: 20000 $

#�������˸����������ұ���ӿո񣬴�ӡ�������
tom salary: 7000 $
jack salary: 20000 $

#Ҳ����н��ǰ�油�㣬��ӡ�������
%-10s salary: %6d $
%-10s salary: %6d $

tom salary: 007000 $
jack salary: 020000 $

ע�⣺��������6��ָ����7000ֻ����λ���Ȳ���6λ������ո���ٲ���

#ָ�����
>>>'%10d' % 56 #��С��ȣ�����ո���
' 56'

#����
>>>'010d' % 56 #����
'0000000056'

#ʮ������(��#�ʹ�Сдx������
>>>"%#X" % 108
'0X6C'

>>>"%#x" % 108
'0x6c'

#С��ע���
>>>print('date is %8.2f' %123.456789)
date is 123.46

>>>print('date is %08.2f' %123.456789)
date is 00123.46


��2��format��ʽ������

>>>print('name is {} and {} years old'.format('tom',18)) #{}�൱����ռλ��Ȼ���ٰ�tom�����ȥ
'name is tom and 18 years old'

#����ʹ�������±�ķ���(.�ǵ��õ���˼��

>>>'I am {1} years old, my name is {0}'.format('tom',18)
'I am 18 years old, my name is tom'
format % values

>>>'{1} - {0}'.format('tom',18)
'tom 18'

#ָ�����
>>>'{}'.format(56)
'56'

>>>'{:10}'.format(56)
' 56'

>>>'{:<10}'.format(56) #�����
'56 '

>>>'{:010}'.format(56)
'0000000056'

#ʮ������
>>>'{:x}'.format(108)
'6c'

>>>'{:X}'.format(108)
'6C'

>>>'{:#x}'.format(108)
'0x6c'

#С��
>>> '{}'.format(123.456789)
'123.456789'

>>>'{:.2f}'.format(123.456789)
'123.46'

>>>'{:9.2f}'.format(123.456789)
' 123.46'

>>>'{:09.2f}'.format(123.456789)
'000123.46'

>>>'{:09.2f} {{}}'.format(123.456789) #����ַ���������л�����
'000123.46 {}'

Python3������ʽ��ע���������д��
>>>name = 'tom'
>>>f'name is {name}'
'name is tom'

��3���ַ������ת���

>>>'name is \'tom\''
"name is 'tom'"

>>>print('line1\nlime2') #���з�
line1
line2

>>>print('\x4F\x50\x51\x52\x53\x54')
OPQRST

>>>print(r'\x4F\x50\x51\x52\x53\x54')
\x4F\x50\x51\x52\x53\x54

��4���ַ��ն�����
input() ���ú��������ص���string����

>>>name = input('shuru:')
shuru:123
>>>name
'123'

>>>int(name) #ת������
123

��д
>>>int(input('shuru:'))
shuru:123
123

- python 3 ִ�������ʽ���ַ����Ĵ��룬��Щ�ǻᱨ��� (b)
A) "my name is {0}, I'm {1} years old.".format('Mike',5) 
B) "my name is {}, I'm {1} years old.".format('Mike',5) 
C) "I'm {1} years old, my name is {0}".format('Mike',5) 
D) "my name is {0}, his name is also {0}".format('Mike') 
E) f"my name is {'Mike'}, his name is also {{Mike}}"

 