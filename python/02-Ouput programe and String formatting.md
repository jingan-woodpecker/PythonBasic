1、命名规则

    a、小驼峰命名(第一个单词首字母小写，其余首字母大写)----userName
    b、大驼峰命名(所有单词首字母大写，一般只有类命名才这样)---UserName
    c、python习惯命名方式(用下划线分割每个单词，不区分大小写)---user_name

2、python中查看关键字(保留字)
方式

```python
import keyword

print(keyword.kwlist)  # 不可输入print(keyword.kwlist())
```

3、输出

*print函数可以接收多个字符串，用
","
逗号隔开就可以连成一串输出(但遇到逗号会打印一个空格)

```python
print("liao", "jing", "an")
```

*如果print()
中包含表达式，则会直接输出表达式的结果

```python
print(399 + 4949)
```

*print()
中还可以接收
"变量的替换"
或
"参数的替换"

```python
# 输出我的年龄以及姓名
age = 22
age_1 = 2
name = "xiaozhu"
print("我的年龄是：%s岁，我的名字叫：%s" % (age + age_1, name))

# 输出金额是四位数，不足的补0
money = 30
print("我还剩下金额：%04d" % (money))

#输出的数字包含两位小数，如果没有用0补充
w = 3.1415926
print("圆周率是：%.2f"%(w))
print("今晚中奖的概率是：%d%%"%(w))

# 总结：1、多个变量替换需要加小括号，并且每个变量用逗号隔开
#       2、%d %s : d数值的变量替换， s所有类型的变量替换
#       3、若要显示"%"，则需要再添加两个"%%"进行转义
```

```python
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
before_score = 72
now_score = 85
rising_percentage_point = (now_score-before_score)/now_score*100
print("小明成绩提升的百分点是：%.1f%%"%(rising_percentage_point))
```






