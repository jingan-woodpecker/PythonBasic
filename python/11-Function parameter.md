1、函数返回值(本质上利用了元组)
    
    函数可以有多个返回值
    
```python
def test(a , b):
    shang = a/b
    yushu = a%b
    return shang , yushu

shang, yushu = test(100 , 20)
print("多个返回值有%s和%s"%(shang , yushu))

#多个返回值有5.0和0
```

2、函数的参数

    * 缺省参数
    