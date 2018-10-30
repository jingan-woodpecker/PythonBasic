多进程

    电脑上同时打开qq、浏览器、观看视频等称为多任务
     linux中使用ps -aux或top命令；查看运行的进程
     
进程：程序的一次运行

    程序是一个指令的集合；
    进程：(正在执行的程序)是一个静态的概念
        * 进程是程序的一次静态的执行过程，占用特定的地址空间
        * 每个进程都是独立的，由3部分组成cpu,date,code
        * 缺点：内存的浪费，cpu的负担
        
        *数据区 、代码区、队长、堆(对象、数组)、栈(函数调用)
        
多进程：同一个程序可以有多个进程(比如打开多个笔记本)
    
    操作系统轮流让各个任务交替执行，由于CPU的执行速度实在太快了，我们感觉就像同时执行一样
    真正的并行执行多任务只能在多核 CPU上实现，但是由于任务数量远远多于CPU的核心数量，所以，
    操作系统也会自动把很多任务轮流调度到每个核心上执行。
    
1、fork()

    * Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回
    一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份
    称为子进程），然后，分别在父进程和子进程内返回。
    
    * 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
    所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
   
```python
import os
pid = os.fork()
if pid < 0:
    print("fork调用失败")
elif pid ==0:
    print("我是子进程(%s),我的父进程是(%s)"%(os.getpid(),os.getppid()))
else:
    print("我是父进程(%s),我的子进程是(%s)" % (os.getpid(),pid))

print("父子进程都可以执行这里的代码")
```    
    由于Windows没有fork调用，上面的代码在Windows上无法运行。
    
    有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache
    服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
    
2、进程不能共享全局变量

```python
import os
import time
num = 100
pid = os.fork()
if pid < 0:
    print("fork调用失败")
elif pid ==0:
    time.sleep(2)
    num+=1
    print("我是子进程(%s),我的父进程是(%s),num:%s"%(os.getpid(),os.getppid(),num))
else:
    time.sleep(3)
    print("我是父进程(%s),我的子进程是(%s),num:%s" % (os.getpid(),pid,num))
    
'''
我是子进程13993,我的父进程是13992，num:101
我是父进程13992,我的子进程是13993，num:100
'''
```
    打印的结果num值是不一致的，因为进程是有独立的内存空间的,所以创建的num
    都存储在自己的数据区，某一个进程修改了值，不影响其它进程，自己的数据都
    放在自己的空间。
    
3、Process类创建进程

    Windows没有fork调用，但是Python是跨平台的，自然也应该提供一个跨平台的
    多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
    
    multiprocessing模块提供了一个Process类来代表一个进程对象
    
```python
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print("子进程的id:%s，父进程id:%s, name:%s"%(os.getpid(),os.getppid(),name))

if __name__ == "__main__":
    #注意：父进程里面包含着子进程
    print("父进程")
    #创建子进程
    p = Process(target=run_proc,args=("test",))
    #开始执行子进程
    p.start()
    #父进程等待子进程结束
    p.join()
    print("子进程已结束")
    
 '''
父进程
子进程的id:6196，父进程id:3452, name:test
子进程已结束
 '''
```
Process的常用方法和属性Process([group[,traget[,name[,args[,kwargs]]]]])

    (1)创建子进程时，只需要传入一个执行函数和函数的参数
        targe:表示这个进程实例所调用的对象；args:表示调用对象的位置参数元组
        p = Process(target=run_proc,args=("test",))
     
    (2)创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
        p.start()
        
    (3)join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
        p.join()
        
    (4)name:为当前进程实例的别名，默认为Process-N,N为从1开始递增的整数
    
    (5)kwargs:表示调用对象的关键字参数字典
    
    (6)group:大多数情况用不到

    (7)is_alive():判断进程实例是否还在执行(死掉)
    
    (8)join([timeout]):是否等待进程实例执行结束，或等待多少秒
    
    (9)run():如果没有给定target参数，对这个对象调用start()方法时，就执行对象中的run()方法
    
    (10)terminate():不管任务是否完成，立即终止
    
    (11)pid: 当前进程实例的PID值
    
```python
from multiprocessing import Process
import time

#子进程要执行的代码
def run_proc(name,num,**kwargs):
    time.sleep(2)
    print("子进程：name:%s, num:%d"%(name,num))
    for k,v in kwargs.items():
        print("%s:%s"%(k,v))

if __name__ == "__main__":
    #注意：父进程里面包含着子进程
    print("父进程")
    #创建子进程,注意args传入的是元组，最后要加个逗号，字典使用{}
    p = Process(target=run_proc,name="pro",args=("test",29,),kwargs={"age":22,"sex":"male"})
    #开始执行子进程
    p.start()
    #父进程等待子进程结束
    p.join()
    print("子进程的名字：%s,id: %s"%(p.name,p.pid))
    print("子进程已结束")
    
'''
父进程
子进程：name:test, num:29
age:22
sex:male
子进程的名字：pro,id: 9080
子进程已结束
'''
```

4、创建新的进程还能够使用类的方式，可以自定义一个类，继承Process类
每次实例化这个类的时候，就等同于实例化一个进程对象

```python
import time
import os

#定义自己的进程类
class MyProcess(Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    #子进程要执行的代码
    def run(self):
        print("子进程")
        #保存子进程当前时间
        startTime = time.time()
        time.sleep(self.interval)
        #保存子进程结束时间
        stopTime = time.time()
        print("子进程id: %s, 父进程id: %s, 执行了%ds"%(os.getpid(),os.getppid(),stopTime-startTime))

if __name__ == "__main__":
    print("主进程")
    #保存主进程当前时间
    startTime = time.time()
    p = MyProcess(2)
    #开始执行子进程
    p.start()
    #父进程等待子进程结束
    p.join()
    #保留主进程结束时间
    stopTime = time.time()
    print("子进程已结束，花费了%ds"%(stopTime-startTime))

'''
主进程
子进程
子进程id: 2012, 父进程id: 7408, 执行了2s
子进程已结束，花费了2s
'''
```

5、同时创建多个进程

    这种方式创建多个进程效率不高

```python
from multiprocessing import Process
import time
import os

#定义自己的进程类
class MyProcess(Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    #子进程要执行的代码
    def run(self):
        print("子进程")
        #保存子进程当前时间
        startTime = time.time()
        time.sleep(self.interval)
        #保存子进程结束时间
        stopTime = time.time()
        print("子进程id: %s, 父进程id: %s, 执行了%ds"%(os.getpid(),os.getppid(),stopTime-startTime))

if __name__ == "__main__":
    print("主进程")
    #保存主进程当前时间
    startTime = time.time()
    for x in range(4):
        p = MyProcess(x+1)
        #开始执行子进程
        p.start()
        #父进程等待子进程结束
        p.join()
    #保留主进程结束时间
    stopTime = time.time()
    print("子进程已结束，花费了%ds"%(stopTime-startTime))

'''
主进程
子进程
子进程id: 5372, 父进程id: 5588, 执行了1s
子进程
子进程id: 5052, 父进程id: 5588, 执行了2s
子进程
子进程id: 8924, 父进程id: 5588, 执行了3s
子进程
子进程id: 2864, 父进程id: 5588, 执行了4s
子进程已结束，花费了10s
'''
```
    把上述代码中的p.join()注释掉，父进程就不会等待子进程，打印结果如下：
    主进程
    子进程已结束，花费了0s
    子进程
    子进程
    子进程
    子进程
    子进程id: 9100, 父进程id: 9056, 执行了1s
    子进程id: 4232, 父进程id: 9056, 执行了2s
    子进程id: 2080, 父进程id: 9056, 执行了3s
    子进程id: 1516, 父进程id: 9056, 执行了4s
 
6、进程池(Pool)

    如果要启动大量的子进程，可以用进程池的方式批量创建子进程
    
    初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool
    时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；
    但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
    直到池中有进程结束，才会创建新的进程来执行。
    
 ```python
from multiprocessing import Pool
import time
import os
def worker(msg):
    print("子进程的pid:%d"%os.getpid())
    startTime = time.time()
    time.sleep(2)
    stopTime = time.time()
    print("子进程的msg:%s, 花费的时间%d"%(msg,stopTime-startTime))

if __name__ == "__main__":
    #创建进程池
    pool = Pool(3)
    for x in range(5):
        #异步请求
        pool.apply_async(worker,(x,))

    #关闭进程池
    pool.close()
    #父进程等待子进程结束
    pool.join()
    print("进程池已结束")
    
'''
子进程的pid:8692
子进程的pid:9196
子进程的pid:8288
子进程的msg:0, 花费的时间2
子进程的msg:1, 花费的时间2
子进程的pid:9196
子进程的pid:8692
子进程的msg:2, 花费的时间2
子进程的msg:3, 花费的时间2
子进程的msg:4, 花费的时间2
进程池已结束
'''
```
    观察上面的结果可以看出，我们是要获取5个进程，因为指定的进程池最大就三个
    所以先把进程池中所有的进程都取出来(三个)，也就是说Id号只有这三个，它会
    不断的用这三个，当三个申请完，只有等它们结束了，才可以继续申请这三个之中的一个。
   
上面的程序是异步请求，如果改为同步请求pool.apply(worker,(x,))打印结果如下

```python
'''
子进程的pid:3716
子进程的msg:0, 花费的时间2
子进程的pid:2828
子进程的msg:1, 花费的时间2
子进程的pid:2628
子进程的msg:2, 花费的时间2
子进程的pid:3716
子进程的msg:3, 花费的时间2
子进程的pid:2828
子进程的msg:4, 花费的时间2
进程池已结束
'''
```

    同步请求的情况下，请求了一个执行完，才可以请求下一个
    进程的id号还是这三个。
    
    注意；调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process

multiprocessing.Pool常用函数解析

    apply_async(func[,arg[,kwds]])：使用非阻塞(异步请求)方式调用
    func（并行执行，阻塞方式必须等待上一个进程退出才能执行下一个
    进程），args为传递给func的参数列表，kwds为传递给func的关键字
    参数列表
    
7、进程的消息队列(进程间通信)

    Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
    Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
    
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    
'''
Process to write: 5336
Put A to queue...
Process to read: 8204
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
'''
```