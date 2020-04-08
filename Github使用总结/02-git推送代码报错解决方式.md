1、执行git push推送代码报错：

    error setting certificate verify locations
    本地证书验证错误，这个我理解了，因为我下载的是HTTPS的内容，需要配置证书

解决方案：

    打开git bash，直接关闭证书校验
    git config --system http.sslverify false

2、如何解决failed to push some refs to git

    出现错误的主要原因，github中的README.md文件不在本地代码目录中
    需要通过下面的命令进行代码合并pull = fetch + merge
    git pull --rebase origin master

    这样代码库中就多了README.md文件了
    这时再次推送代码就可以了：git push -u origin master