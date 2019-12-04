文件操作-os模块

    os模块包含普遍的操作系统功能
    
    1、os.name()----判断现在正在使用的平台，windows显示"nt",linux显示"posix"
       rename(需要修改的文件名，新的文件名)，也可以做剪切
    2、os.getcwd()----获取当前工作目录
    3、os.listdir()----指定所有目录下所有的文件和目录名(以列表的形式全部列举出来，其中没有区分目录和文件)
    4、os.remove()----删除指定文件
    5、os.rmdir()----删除指定目录(该目录不能为空)
    6、os.mddir()----创建目录(只能创建一层目录，要想递归创建目录，需要使用os.makedirs())
    7、os.path.isfile()----判断指定对象是否为文件。是返回True,否返回False
    8、os.path.isdir()----判断指定对象是否为目录。是返回True,否返回False
    9、os.path.exists()----判断指定对象是否为存在。是返回True,否返回False
    10、os.path.split()----返回路径的目录和文件名
    11、os.system()----执行shell命令
    12、os.chdir()----改变目录到指定目录
    13、os.path.size()----获取文件的大小(如果是目录返回 0)
    14、os.path.abspath()----获得绝对路径
    15、os.path.join(path,name)----连接目录和文件
    16、os.path.basename(path)----返回文件名
    17、os.path.dirname(path)----返回文件所在目录
    
    * 重命名文件

```python
import os
os.rename("test1.txt" , "test2.txt")
```

    *获取文件的绝对路径
    
```python
import os
get_abspath = os.path.abspath("test2.txt")
print(get_abspath)
```

    *获取文件大小
    
```python
import os
get_size = os.path.getsize("test2.txt")
print(get_size)
```

    * 批量修改文件名
   
```python
import os 

file_list = os.listdir(r"D:\UnitTest\test")
# print(file_list)

for file in file_list:
    #定义最后批量修改的文件名：每个文件名前面加上"re-"
    dest_file="re-"+file
    #获取test目录的绝对路径
    parent_dir = os.path.abspath("test")
    #将test目录中的绝对路径和文件名相连
    source_file = os.path.join(parent_dir , file)
    #重命名
    os.rename(source_file , dest_file)
``` 
 
 ```python
import os
import sys
#!/usr/bin/env Python
# coding=utf-8

#查找某个目录中包含hello的.py文件有哪些
file_list = []
def find_hello(parent_dir , file_name):
		#连接目录和文件名
    file_abspath = os.path.join(parent_dir , file_name)
		#判断上面指定连接的还是目录，就进入循环
    if os.path.isdir(file_abspath):
				#遍历出该目录下的所有目录和文件，形成一个列表
        for f in os.listdir(file_abspath):
						#递归遍历，直到不是目录
            find_hello(file_abspath , f)

    else:
		#如果上面连接的目录直接就是.py结尾的文件就调用其他函数
        if file_abspath.endswith(".py"):
            if read_and_find_hello(file_abspath):
                file_list.append(file_abspath)

def read_and_find_hello(py_file):
    flag = False
    f = open(py_file)
    while True:
        line = f.readline()
        if line == "":
            break
        elif "hello" in line:
            flag = True
            break
    f.close()
    return flag
# print(read_and_find_hello(r"D:\UnitTest\test\Select.py"))
find_hello("D:\learn" , "python")
```

```python

#把数据写入文件，把数据读出来
import os
def read_stus():
    if os.path.exists(file_name):
        f = open(file_name , "r" ,encoding='utf-8')
        while True:
            student_str = f.readline()
            if student_str == "":
                break
            else:
                student_str_list = student_str.split("\t")
                student = {"name":student_str_list[0] , "age":student_str_list[1] ,"sex":student_str_list[2]}
                stus.append(student)
        print(stus)

def write_stus_to_file():
    if os.path.exists(file_name):
        if os.path.exists(backup_file):
            os.remove(backup_file)
        os.rename(file_name, "backup-"+file_name)
    f = open(file_name , "w" ,encoding='utf-8')
    for student in stus:
        student_str = "%s\t%s\t%s\n"%(student["name"],student["age"],student["sex"])
        f.write(student_str)
    else:
        f.close()

def print_menu():
    print("*"*30)
    print("学生名字管理系统".center(50))
    print("输入1：添加学生")
    print("输入2：查找学生")
    print("输入3：修改学生")
    print("输入4：删除学生")
    print("输入5：查看所有学生")
    print("输入6：退出")

def add_student():
    name = input("请输入添加的学生姓名:")
    age = int(input("请输入添加的学生年龄:"))
    sex = input("请输入添加的学生性别:")
    # 用字典存放每个学生的所有信息
    stu = {}
    stu["name"] = name
    stu["age"] = age
    stu["sex"] = sex
    # 将所有学生信息都添加到列表中
    stus.append(stu)
    print("添加学生成功")

def search_student(name):
    for item in stus:
        if item["name"] == name:
            print("%s该学生存在"%name)
            #调用打印学生信息
            print_studentinfo(item)
    else:  # 注意这个eles的位置，考虑清楚逻辑错误和语法错误
        print("%s该学生未找到"%name)

def del_student(name):
    student = search_student(name)
    stus.remove(student)

#封装打印学生信息函数
def print_studentinfo(item):
    print("%s\t%s\t%s\t" % (item["name"], item["age"], item["sex"]))

def print_all_students():
    print("序号\t姓名\t年龄\t性别")
    for i, item in enumerate(stus, 1):
        print("%s\t"%i , end="")
        #调用打印学生信息
        print_studentinfo(item)

def main():
    print_menu()
    read_stus()
    while True:
        operate = input("请输入你想要进行的操作:")
        if operate == "1":
            add_student()
            write_stus_to_file()
        if operate == "2":
            name = input("请输入要查找的学生姓名:")
            search_student(name)
        if operate == "3":
            pass
        if operate == "4":
            name = input("请输入你要删除的学生姓名:")
            del_student(name)
            print("删除学生成功%s"%name)
            write_stus_to_file()
        if operate == "5":
            print_all_students()
        if operate == "6":
            break

file_name = "stus.txt"
backup_file ="backup-stus.txt"
stus = []
main()
```
