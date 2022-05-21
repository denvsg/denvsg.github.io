# 构建一个可执行文件

添加一个构建文件  
在源文件目录创建一个BUILD.gn文件并添加以下内容:

```gn
executable("hello_world") {
    sources = [
        "hello_world.c",
    ]
}
```

在目标目录中应该存在一个hello_world.c的文件，包含你期望的内容。  
现在我们仅仅需要告诉编译器需要处理这个编译文件就行了。  
打开根目录(src)下的BUILD.gn文件，将新创建的编译文件添加到其中一个根group的依赖项中：

```gn
group("root") {
    deps = [
        ...
        "//url",
        "//src:hello_world",
    ]
}
```


### 构建执行

```shell
gn gen out/Default  # 生成 ninja 
ninja -C out/Default hello_world # 编译可执行文件
out/Default/hello_world # 执行 hello_world
```