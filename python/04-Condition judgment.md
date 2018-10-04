1、条件判断(if-elif-else)

    特殊的真和假
        值              真和假
        
        非0               真
        0                 假
        ""                假
        None              假
        []                假
        ()                假
        {}                假
        

```python
age = int(input("我的年龄是："))
if age:
    print("age是非0")
else:
    print("age是0")
```

```python
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖
用if-elif判断并打印结果：
'''
height = float(input("小明的身高是:"))
weight = float(input("小明的体重是:"))
BMI = weight/height**2
if BMI < 18.5:
    print("过轻")
elif BMI >= 18.5 and BMI < 25:
    print("正常")
elif BMI >= 25 and BMI < 28:
    print("过重")
elif BMI >= 28 and BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")

print("小明的BMI指数是%.1f"%BMI)
```