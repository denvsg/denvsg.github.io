# uniq 命令使用

## uniq 命令可以对文件或标准输入找出唯一的行，进行输出或者删除

uniq 是能对排过序的文件进行操作，因此，大多时候 uniq 和 sort 配合使用

### 1. 生成唯一的行

```shell
$ cat sorted1
csh
csh
bash
bash
ksh
zsh
shell
shell

$ uniq sorted1 # 也可 cat sorted1 | uniq
csh
bash
ksh
zsh
shell
```

### 2. 只显示唯一的行

```shell
$ cat sorted1
csh
csh
bash
bash
ksh
zsh
shell
shell

$ uniq -u sorted1 # 也可 cat sorted1 | uniq -u
ksh
zsh
```

### 3. 统计各行出现的次数

```shell
$ cat sorted1
csh
csh
bash
bash
ksh
zsh
shell
shell

$ uniq -c sorted1 # 也可 cat sorted1 | uniq -c
      2 csh
      2 bash
      1 ksh
      1 zsh
      2 shell
```

### 4. 找出重复的行

```shell
$ cat sorted1
csh
csh
bash
bash
ksh
zsh
shell
shell

$ uniq -d sorted1 # 也可 cat sorted1 | uniq -d
csh
bash
shell
```

### 5. 从第三个字符开始过滤

```shell
$ cat sorted1
csh
csh
bash
bash
ksh
zsh
shell
shell

$ uniq -s2 -w2 sorted1 # 也可 cat sorted1 | uniq -d
csh
bash
ksh
shell
# -s 2 跳过前两个字符
# -w 2 指定后续的两个字符
```



......    
[返回](../README.md)   
......    
