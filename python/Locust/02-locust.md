关联

    在某些请求中，需要携带之前从Server端返回的参数，因此在构造请求时需要先从之前请求的Response中
    提取出所需的参数，常见场景就是session_id。
    
    Python脚本，通过官方库函数re.search就能实现所有需求。甚至针对html页面，我们也可以采用lxml库，
    通过etree.HTML(html).xpath来更优雅地实现元素定位。
    
    在LoadRunner中手动进行关联处理时，主要是通过使用注册型函数，例如web_reg_save_param，对前一个
    请求的响应结果进行解析，根据左右边界或其它特征定位到参数值并将其保存到参数变量，然后在后续请
    求中使用该参数。
    
```python
from lxml import etree
from locust import TaskSet,task,HttpLocust

class UserBehavior(TaskSet):

    @staticmethod
    def get_session(html):
        tree = etree.HTML(html)
        return tree.xpath("//div[@class='btnbox']/input[@name='session']/@value")[0]

    @task(10)
    def test_login(self):
        html = self.client.get('/login').text
        username = 'jing@mail.com'
        password = '123456'
        session = self.get_session(html)
        payload = {
                'username':username,
                'password':password,
                'session':session
        }

        self.client.post('/login', data = payload)

class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
```

参数化主要是用在测试数据方面，概括为三种类型

    * 循环取数据，数据可重复使用
    * 保证并发测试数据唯一性，不循环取数据
    * 保证并发测试数据唯一性，循环取数据
    
    在LoadRunner中是有一个集成的参数化模块，可以直接配置参数化策略
    
Locust 使用Python的list和queue数据结构即可

    具体做法是:在WebsiteUser定义一个数据集，然后所有虚拟用户在WebsiteTasks中就可以共享该数据集了
    
    * 如果不要求数据唯一性，数据集选择list数据结构，从头到尾循环遍历即可；
    * 如果要求数据唯一性，数据集选择queue数据结构，取数据时进行queue.get()操作即可，并且这也不会循环取数据；
    * 至于涉及到需要循环取数据的情况，那也简单，每次取完数据后再将数据插入到队尾即可，queue.put_nowait(data)。
    
 循环取数据，数据可以重复使用
 
    所有并发虚拟用户共享同一份测试数据，各虚拟用户在数据列表中循环取值。
    例如，模拟3用户并发请求网页，总共有100个URL地址，每个虚拟用户都会依次循环加载这100个URL地址；
    
```python
from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):

    def on_start(self):
        #设置参数下标初始值
        self.index = 0

    @task
    def test_visit(self):
        #读取share_data的参数
        url = self.locust.share_data[self.index ]
        #取余运算，循环遍历
        self.index = (self.index+1)%len(self.locust.share_data)
        self.client.get(url)

class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    share_data = ['url1','url2','url3','url4','url5']
    min_wait = 1000
    max_wait = 3000
```

保证并发测试数据唯一性，不循环取数据

    所有并发虚拟用户共享同一份测试数据，并且保证虚拟用户使用的数据不重复。
    例如，模拟3用户并发注册账号，总共有9个账号，要求注册账号不重复，注册完毕后结束测试
    
保证并发测试数据唯一性，循环取数据  
    
    所有并发虚拟用户共享同一份测试数据，保证并发虚拟用户使用的数据不重复，并且数据可循环重复使用。
    例如，模拟3用户并发登录账号，总共有9个账号，要求并发登录账号不相同，但数据可循环使用；加载示例如下表所示。
    
```python
from locust import TaskSet, task, HttpLocust
import queue


class UserBehavior(TaskSet):
    @task
    def test_register(self):
        try:
            # get_nowait() 取不到数据直接崩溃；get() 取不到数据会一直等待
            data = self.locust.user_data_queue.get_nowait()  # 取值顺序 ‘username‘: ‘test0000‘、‘username‘: ‘test0001‘、‘username‘: ‘test0002‘...
        except queue.Empty:  # 取不到数据时，走这里
            print('account data run out, test ended.')
            exit(0)
        print('register with user: {}, pwd: {}'.format(data['username'], data['password']))
        body = {
            'username': data['username'],
            'password': data['password']
        }
        r = self.client.post('/user/signin', data=body).text
        assert r.status_code == 200


class WebsiteUser(HttpLocust):
    host = 'https://passport.cnblogs.com'
    task_set = UserBehavior
    user_data_queue = queue.Queue(maxsize=100)  # 创建队列，先进先出
    for index in range(100):
        data = {
            "username": "test%04d" % index,
            "password": "pwd%04d" % index,
            "email": "test%04d@debugtalk.test" % index,
            "phone": "186%08d" % index,
        }
        user_data_queue.put_nowait(data)  # 循环加入队列<全部>,循环完，继续执行
    min_wait = 1000
    max_wait = 3000
```

检查点
    
    就是使用断言assert

集合点

    集合点可以简单得理解为一种控制虚拟用户行为的机制，该机制可以达到在一定时间范围内将一定数量的虚拟用户阻挡在一个操作行为点前的位置进行互相等待，在条件（达到虚拟用户数量或超时）到达后唤醒全部等待中的虚拟用户，从而达到使得一定数量的虚拟用户可以同时进入下一个操作行为点的目的。
    往往其使用初衷是为了实现最大意义上的并发来考察系统应对此种极端情况的表现。

```python
from locust import HttpLocust, TaskSet, task, events
from gevent._semaphore import Semaphore
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()
 
def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()
 
events.hatch_complete += on_hatch_complete
 
class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/1111")
 
    @task(1)
    def profile(self):
        self.client.get("/")
 
    def on_start(self):
        all_locusts_spawned.wait()
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 1000

```