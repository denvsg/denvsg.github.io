# GN

<br />

##### [进入目录](contents_page.md)

<br />

## GN 介绍

[下载 gn 工具](https://github.com/timniederhausen/gn/releases)    
[下载 ninja 工具](https://github.com/ninja-build/ninja/releases)    
[官方文档](https://gn.googlesource.com/gn/+/master/docs/)

GN是谷歌为构建chromium的附产物。  
GN是一个元构建系统,可以为ninja生成构建文件。

## 构建gn

执行以下命令，会自动生成 `out/build` 目录

```shell
gn gen out/build
```

## 跨平台构建

GN有一个host和一个target的概念.主机host是运行构建的平台,目标target是代码实际运行的平台。  
添加一下参数，可以构建对应的操作系统和芯片平台
> 如果为设置 **target_os和target_cpu** 的值，将使用主机的值即 **host_os和host_cpu**

```shell
target_os = "chromeos"
target_os = "android"
target_os = "linux"

target_cpu = "arm"
target_cpu = "x86"
target_cpu = "x64"
```

```shell
# 示例命令，构建 在x64 Linux机器上运行 的程序
gn gen out/Default --args='target_os="linux" target_cpu="x64"'
```

<br />
<br />
<br />
<br />
<br />

......   
[回到主目录](../README.md)   
......    


