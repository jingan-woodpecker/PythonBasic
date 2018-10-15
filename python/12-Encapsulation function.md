简单封装函数

```python
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
    while True:
        operate = input("请输入你想要进行的操作:")
        if operate == "1":
            add_student()

        if operate == "2":
            name = input("请输入要查找的学生姓名:")
            search_student(name)

        if operate == "3":
            pass
        if operate == "4":
            pass
        if operate == "5":
            print_all_students()
        if operate == "6":
            break

stus = []
main()
```