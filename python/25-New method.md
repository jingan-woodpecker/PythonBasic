1、__new__()构建对象的方法 ：在类的对象构造的时候调用的(其实是重写父类的静态方法)

    默认传入的参数是self的，就是成员方法
    
```python
class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("对象已构建好，由解释器自动回调init方法，对象初始化")

    #new方法是当前对象构建时由解释器自动回调的方法，该方法必须返回当前类的对象
    def __new__(cls, username, password):
        print("User类的对象开始创建")
        return object.__new__(cls)

u = User("lisi" , 124455)
print(u)
'''
User类的对象开始创建
对象已构建好，由解释器自动回调init方法，对象初始化
<__main__.User object at 0x00000000024CB9E8>
'''
```

    总结

    __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

    __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

    __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

    我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节
