一、本地vscode拉取远程仓库到本地

1、到VSCode里新建一个文件夹;

2、组合键 Ctrl+` 呼出集成终端，或者点击——查看>点击集成终端 ;

3、在终端输入代码git clone  https://github.com/jingan-woodpecker/PythonBasic.git

![克隆http](../images/clone.png)

4、等待克隆完成;

5、然后就可以写代码了;

二、本地vscode推送代码到远程仓库

1、切换到对应目录 cd PythonBasic

2、先用 git status 看你更改了哪些文件；

3、然后 git add 你想要提交的更改的文件 或者 git add . 所有的文件；

4、再git commit -m ‘提交信息’；

5、最后 git push origin master/你的分支 。

三、markdown语法格式

[markdown语法格式](https://www.cnblogs.com/alantao/p/8521929.html)

四、已连接远程仓库，需拉取其它仓库到本地的方式

	输入命令：git clone 仓库地址（例如：https://github.com/jingan-woodpecker/PythonBasic.git）


五、如何解决在linux上每次git push都要输入账号密码的问题

	1、先cd到根目录，然后执行git config --global credential.helper store命令

	2、执行完上面的命令后，就可以再次使用git push 提交了，不过第一次还需要密码，第二次提交就不需要了
