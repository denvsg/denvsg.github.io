# cat 命令使用

### 1. 查看文件内容

```shell
$ cat file.txt
This is a line inside file.txt
```

### 2. 查看多个文件

```shell
$ cat file.txt file1.txt
This is a line inside file.txt
This is a line inside file1.txt
```

### 3. 标准输入和文件同时输出

```shell
$ echo "hello world" | cat - file.txt
hello world
This is a line inside file.txt
```

### 4. 去掉多余的空白行

```shell
$ cat -s file.txt
This is a line inside file.txt
```

### 5. 显示制表符

```shell
$ cat -T file.txt
This is a line inside file.txt
```

### 6. 显示行号

```shell
$ cat -n file.txt
1 This is a line inside file.txt
```
