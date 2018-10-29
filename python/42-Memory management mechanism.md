垃圾回收GC

    Garbage collection
    (1) 为新生成的对象分配内存
    (2) 识别那些是垃圾对象从垃圾对象那回收内存
    
引用计数机制

    python采用的是引用计数机制(算法)为主，标记-清除和分代收集两种机制为辅的策略
    如果没有垃圾回收就容易造成内存泄漏
    
python里面一切皆对象，他们的核心就是一个结构体：PyObject
    
    typedef struct object{
    int ob refcnt;
    struct_typeobject*ob_type;
    }PyObject;

    define Py INCREF(op)((op)->ob_refcnt++) //增加计数
    define Py DECREF(op)\                   //减少计数
    if(--(op)->ob_refcnt != 0)\ //不等于0就计数
        ;\
        \
    else\
        _Py_Dealloc((PyObject*)(op)) //等于0就清除
        
引用计数机制的优点：

    * 简单
    * 实时性： 一旦没有引用，内存直接释放了，不用想其它机制需要等到特定时机，
               实时性还有一个好处：处理回收内存的时间分摊到平时

引用计数机制的缺点：

    * 维护引用计数消耗资源(忽略不计)
    * 循环引用(注意点)
    
导致引用计数+1的情况

    1、对象被创建，例如a = 22
    2、对象被引用，例如b = a
    3、对象被作为参数，传入到一个函数中，例如func(a)
    4、对象作为一个元素，存储在容器中，例如list1 = [a,a]
    
导致引用计数-1的情况

    1、对象的别名被显示销毁，例如del a
    2、对象的别名被赋予新的对象，例如a = 22
    3、一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量(全局变量不会)
    4、对象所在的容器被销毁，或者从可变的容器中删除对象
    
查看一个对象的引用计数
    
```python
import sys
z = "python"
print(sys.getrefcount(z))
```
引用计数的缺陷：循环引用--->可以使用分代收集解决

```python
import gc
class ClassA():
    def __init__(self):
        print("object born,id:%s"%str(hex(id(self))))
        
def f2(self):
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
#把python的gc关闭
gc.disable()
f2()
#执行f2()，进程占用的内存会不断增大
```
总结：
    
    三种情况会触发垃圾回收：
        * 调用gc.collect()
        * 当gc模块的计数器达到阀值
        * 程序退出的时候
        
垃圾回收后的对象会放在gc.garbage列表里面

    a、gc.get_threshold()获取的gc模块中自动执行垃圾回收的频率；
    b、gc.set_threshold(threshold0[,threshold1[,threshold2]])设置自动执行垃圾回收的频率
    c、gc.get_count()获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表
    d、gc.collect([generation])显式进行垃圾回收，可以输入参数，0代表只检查第一代对象，1
       代表检查一、二代的对象，2代表检查一、二、三代的对象，如果不传入参数，执行一个full 
       collection,也就是等于传入2，返回不可达(unreachable objects)对象的数目
    e、gc模块唯一处理不了的是循环引用的类都有-__del__方法，所以项目中要避免定义__del__方法
    
```python
import gc
print(gc.garbage)
#[]
print(gc.get_count())
#(605, 10, 0)表示第一代605个对象，第二代10个对象，第三代0个

print(gc.get_threshold())
#(700, 10, 10)阀值，第一代不可超过700个
```