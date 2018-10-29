属性访问拦截器(重定向)

```python
class School(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = "cpp"

    #属性访问拦截器，打log
    def __getattribute__(self, obj):
        if obj == "subject1":
            print("log subject1")
            #如果满足上面的条件就重定向到...
            return "redirect python"
        #下面的两行代码不可省略
        else:
            return object.__getattribute__(self,obj)

s = School("python")
#调用subject1就会传入到obj执行属性访问拦截器，按照规则运行 
print(s.subject1)
#不等于subject1就按照初始化方式运行
print(s.subject2)

'''
log subject1
redirect python
cpp
'''
```

使用属性访问拦截器的注意点

```python
class Person(object):
    def __getattribute__(self, obj):
        print("---test---")
        if obj.stratswith("a"):
            return "hahaha"
        else:
            return self.test
        
    def test(self):
        print("heihei")
t = Person()
print(t.a) #返回hahaha
print(t.b)#程序会崩溃
```
    上面的程序调用t.b的时候，程序就会崩溃，原因在于else后面的语句(return self.test)
    当执行了return self.test语句后，相当于又去访问对象的属性了，然后又执行属性访问
    拦截器了，陷入无限死循环当中。