1、线程同步问题

    主要涉及线程安全问题，线程访问全局变量时，不加控制有可能产生紊乱的情况
    
    多个线程对一个变量进行频繁操作时，因为对数据进行计算时都要先把内存当中的
    数据读取到寄存器上，然后在寄存器对这些数据进行操作，操作完后还要把结果写
    回到内存中去。所以下面程序中
    
        第一步：先到内存中读g_num的值到寄存器；
        第二步：然后它在寄存器当中，把它读来的值加1；
        第三步：再把这个值写回到内存中。
        
    上面的三步是不可分割的，但在下面程序中，第一个线程先读出100，到加1，每次
    运行到第二步(由运行状态转为就绪状态)后，切换到另一个线程开始执行(重读100
    再加1)后，又停止了，重新切换到第一个线程，执行第三步写101回内存，又切换到
    第二个线程执行第三步，也写101回内存，值就加了两次，正常情况应该是102
    
```python
from threading import Thread

g_num = 0
def worker1():
    global g_num
    for x in range(200000):
        g_num += 1

for i in range(2):
    t = Thread(target=worker1)
    t.start()

print("main thread:g_num=%d"%g_num)

'''
main thread:g_num=211138
'''
```

2、线程同步-给线程加锁

    * 当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制
    
    * 线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁
    
    * 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性
    
    * 某个线程要更改共享数据时，先将其锁定，此时资源的状态为"锁定",其它线程不能更改；
      直到该线程释放资源，将资源的状态变成"非锁定",其它线程才能再次锁定该资源
      
    * threading模块中定义了Lock类，可以方便的处理锁定
    
互斥锁的创建和锁定、释放

    (1)创建锁
    mutex = threading.Lock()
    
    (2)锁定
    mutex.acquire([blocking])
    如果设定blocking为True，则当前线程会堵塞，直到获取到这个锁为止(如果没有指定，那么默认为True)
    如果设定blocking为False，则当前线程不会堵塞
    
    (3)释放
    mutex.release()
    
```python
from threading import Thread,Lock
import time

g_num = 0
def test1():
    global g_num
    for i in range(200000):
        #上锁后返回一个布尔变量
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            #释放锁
            mutex.release()
    print("tes1---g_num = %s"%g_num)

if __name__ == "__main__":
    #创建一个互斥锁,默认是未上锁状态
    mutex = Lock()
    t1 = Thread(target=test1)
    t1.start()
    
'''
tes1---g_num = 200000
'''
```

3、死锁的问题

    * 在线程之间共享多个资源的时候，如果两个线程分别占有一部分资源，并且同时
      等待对方的资源，就会造成死锁
    
    * 进入到了死锁状态，可以使用ctrl+z退出
    
```python
from threading import Thread,Lock
import time

class MyThread1(Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name + "---do1---up---")
            time.sleep(1)
            if mutexB.acquire():
                print(self.name + "---do1---down---")
                mutexB.release()
            mutexA.release()

class MyThread2(Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name + "---do2---up---")
            time.sleep(1)
            if mutexA.acquire():
                print(self.name + "---do2---down---")
                mutexA.release()
            mutexB.release()


if __name__ == "__main__":
    #创建互斥锁,默认是未上锁状态
    mutexA = Lock()
    mutexB = Lock()
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
```

4、多个线程有序执行，相互锁定

```python
from threading import Thread,Lock
import time

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("---Task1---")
                time.sleep(0.5)
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            #因为lock2刚创建锁的时候就锁上了,所以只有等待任务1执行
            #完成后释放了lock2的锁才执行任务2
            if lock2.acquire():
                print("---Task2---")
                time.sleep(0.5)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            #同理lock3刚创建锁就锁上了，所以也要等lock2执行完释放lock3
            if lock3.acquire():
                print("---Task1---")
                time.sleep(0.5)
                lock1.release()

if __name__ == "__main__":
    #创建锁默认没锁上
    lock1 = Lock()
    #创建另外一把锁，并且锁上
    lock2 = Lock()
    lock2.acquire()
    #再次创建锁，并且锁上
    lock3 = Lock()
    lock3.acquire()
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()
```

5、线程同步--队列

    python中的Queue模块中提供了同步的的，线程安全的队列类，包括：
    
    * FIFO(先入先出)队列Queue
    * LIFO(后入先出)队列LifoQueue
    * 优先级队列 priorityQueue
    
    这些队列都实现了锁原语（可以理解为原子操作，要么不做，要么做完）
    能够在多线程中直接使用
    
```python
from queue import Queue
from threading import Thread
import time

class Producer(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            #如果产品小于500就生产，并放入到队列中
            if queue.qsize() < 500:
                for i in range(100):
                    count = count+1
                    msg = "生产产品"+str(count)
                    #使用put()默认底层已经加好锁
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    #使用get()默认底层已经加好锁
                    msg =self.name+ "生产产品"+queue.get()
                    print(msg)
            time.sleep(0.5)

if __name__ == "__main__":
    #创建队列
    queue = Queue()
    #先给队列加入300个产品
    for i in range(300):
        queue.put("初始产品"+str(i))
    #创建两个生产者线程
    for i in range(2):
        p = Producer()
        p.start()
    #创建五个消费者线程
    for i in range(5):
        c = Consumer()
        c.start()
```

6、ThreadLocal变量

    * 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的
      独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间
      相互传递的问题。
      
    * 可以理解为全局变量local_school是一个dict字典，可以绑定其它变量
    
    * ThreadLocal最长用的地方就是为每个线程绑定一个数据库连接，HTTP请求，
      用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便的
      访问这些资源。
      
  ```python
import threading

#创建全局变量 ThreadLocl对象
local_school = threading.Lock()
def process_student():
    #获取当前线程关联的学生
    std = local_school.student
    print("hello, %s (in %s)"%(std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocl的student
    local_school.student = name
    process_student()

if __name__ == "__main__":
    t1 = threading.Thread(target=process_thread,args=("zhangsan",),name="t1")
    t2 = threading.Thread(target=process_thread,args=("lisi",),name="t2")
    t1.start()
    t2.start()
```
    
    
    