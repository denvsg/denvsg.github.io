# Golang 学习

<br />

##### [进入目录](contents_page.md)

<br />

## Golang 介绍
[下载 golang sdk](https://golang.google.cn/dl/)  

[镜像站下载](https://mirrors.aliyun.com/golang/?spm=a2c6h.13651104.0.0.203872b6cMGlp7)

### go 设置代理
`go env -w GOPROXY=https://goproxy.cn,direct` 

```shell
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,https://goproxy.io,direct
```

> GOPROXY，目前国内常用的go代理
goproxy.io    
https://goproxy.io,direct  
七牛云     
https://goproxy.cn  
阿里云  
https://mirrors.aliyun.com/goproxy/  

在Go 1.13+ 中，可以通过GOPROXY来控制代理，以及通过GOPRIVATE控制私有库不走代理。

设置GOPROXY代理：  
go env -w GOPROXY=https://goproxy.cn,direct  
设置GOPRIVATE来跳过私有库，比如常用的Gitlab或Gitee，中间使用逗号分隔：  

go env -w GOPRIVATE=*.gitlab.com,*.gitee.com  
如果在运行go mod vendor时，提示Get https://sum.golang.org/lookup/xxxxxx: dial tcp 216.58.200.49:443: i/o timeout，
则是因为Go 1.13设置了默认的GOSUMDB=sum.golang.org，这个网站是被墙了的，用于验证包的有效性，可以通过如下命令关闭：

go env -w GOSUMDB=off  
可以设置 GOSUMDB="sum.golang.google.cn"， 这个是专门为国内提供的sum 验证服务。   

go env -w GOSUMDB="sum.golang.google.cn"  

<br />
<br />
<br />
<br />
<br />

......   
[回到主目录](../README.md)   
......    


