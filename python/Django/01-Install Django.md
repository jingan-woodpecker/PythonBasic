windows下安装Django

    参考网站
http://www.runoob.com/django/django-install.html

    1 如果你还未安装Python环境需要先下载Python安装包。

    Python 下载地址：https://www.python.org/downloads/
    Django 下载地址：https://www.djangoproject.com/download/
    
注意：Python和Django版本的对应关系

    2、已安装Python3.6
    
    3、安装Djangon-1.11.16
       * 下载Django安装包解压
       * cmd命令窗口下进入到解压后的目录中执行：python setup.py install
         Django将要被安装到Python的Lib下site-packages。
         
       * 配置Path环境变量将C:\Users\asus\AppData\Local\Programs\Python\Python36\Scripts；
       C:\Users\asus\AppData\Local\Programs\Python\Python36\Lib\site-packages\django放入即可
       * 检查是否安装成功命令；
         import django
         django.get_version()
         
        如果输出版本号则安装成功