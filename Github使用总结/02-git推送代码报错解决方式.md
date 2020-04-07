1、执行git push推送代码报错：

    error setting certificate verify locations
    本地证书验证错误，这个我理解了，因为我下载的是HTTPS的内容，需要配置证书

解决方案：

    打开git bash，直接关闭证书校验
    git config --system http.sslverify false