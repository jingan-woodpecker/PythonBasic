局部变量和全局变量的冲突(LEGB原则)
    
    locals-->enclosing function-->globals-->builtins
    
查看内建模块dir(__builtin__)

闭包

    满足两个条件才成为闭包：
    (1)一个函数里面再定义一个函数,并且将里面的函数作为返回值；
    (2)内部函数对外部函数作用域里的变量进行了引用，通俗的说就是用到了外边的变量(非全局变量)。
    注意：函数的参数也是变量
    
闭包相当于将外边函数作用域在局部的变量的生命周期变长了，实际上是解释器把局部变量绑定到函数
内部，相应的延长了它的生命期

```python
def straight_line(a , b):
    #在函数内部再定义了一个函数line
    def line(x):
        #用到了外边的函数变量a,b
        return  a*x + b
    #返回内部函数
    return line
sl = straight_line(10 , 5)
l = sl(5)
print(l)
#也可以一起赋值，就是先赋值外面的，再赋值里面的
get = straight_line(5,5)(10)
print(get)

'''
55
55
'''
```
    总结：可以将一些固定的内容写入内部的函数保留下来，并作为返回值形成闭包