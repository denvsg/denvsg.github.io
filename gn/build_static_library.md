# 构建静态库

### 声明依赖关系
实现一个静态库，输入输出.    
该目录中有一个源文件hello.c，它具有执行此操作的功能.    
打开该目录下的BUILD.gn文件并将静态库实现代码添加到现有文件的底部:

```gn
static_library("hello") {
    sources = [
        "hello.c",
    ]
}
```

对该库生成一个依赖于这个库的可执行文件:

```gn
executable("say_hello") {
    sources = [
        "say_hello.c",
    ]
    deps = [
        ":hello",
    ]
}
```

这个可执行文件包含一个源文件，并依赖于前一个静态库.  
静态库在deps使用它的标签引用. 您可以使用完整的标签，从根路径 // 开始  
但是如果是在同一个构建文件中引用目标， 则可以使用快捷方式 :hello.  
 
```shell
ninja -C out/Default say_hello # 编译
out/Default/say_hello # 运行
```