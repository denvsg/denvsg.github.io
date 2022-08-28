# tr 命令使用

## tr 命令可以对标准输入的内容进行转换

tr 只能通过stdio标准输入接收输入，无法通过命令行参数接收.  
格式: `tr [options] set1 set2`  
输入的字符从set1映射到set2,字符一一对应，  
如果set1长度较长，则一直set2最后的字符直到与set1长度相同   
如果set2长度较长，则忽略超出set1长度的部分

### 1. 将小写字母转换成大写字母

```shell
$ echo "hello world" | tr 'a-z' 'A-Z'
HELLO WORLD

```

> 'A-Z'和'a-z'都是字符组。我们可以按照需要追加字符或字符类来构造自己的字符组。  
'ABD-}'、'aA.,'、'a-ce-x'以及'a-c0-9'等均是合法的集合。  
> 定义集合也很简单，不需要书写一长串连续的字符序列，  
> 只需要使用“起始字符终止字符”这种格式就行了。  
> 这种写法也可以和其他字符或字符类结合使用。  
> 如果“起始字符终止字符”不是有效的连续字符序列，  
那么它就会被视为含有3个元素的集合（起始字符、和终止字符）。  
> 你也可以使用像'\t'、'\n'这种特殊字符或其他ASCII字符。

#### 1.1. 示例.简单的数字加密

```shell
$ echo 12345 | tr '0-9' '9876543210'
87654

$ echo 87654 | tr '9876543210' '0-9'
12345
```

#### 1.2. 示例.简单的字符加密

```shell
$ echo "hello world" | tr 'a-z' '0-9a-p'
74bbe mehb3


$ echo "74bbe mehb3" | tr '0-9a-p' 'a-z'
hello world
```

#### 1.3. 示例.制表符回车转换成空格

```shell
$ echo -e "hello\tworld,hello\tshell."
hello   world,hello     shell.

$ echo -e "hello\tworld,hello\tshell." | tr '\t' ' '
hello world,hello shell.

$ echo -e "hello\nworld,hello\nshell." | tr '\n' ' '
hello world,hello shell.

```

### 2. 使用tr删除字符

> tr有一个选项-d，可以通过指定需要被删除的字符集合，将出现在stdin中的特定字符清除掉

```shell
$ echo "hello world" | tr -d 'aeiou'
hll wrld
```

### 3. 字符补集

格式: `tr -c [set1] [set2]`
> 如果只给出了set1，那么tr会删除所有不在set1中的字符。  
> 如果也给出了set2，tr会将不在set1中的字符转换成set2中的字符。  
> 如果使用了-c选项，set1和set2必须都给出。  
> 如果-c与-d选项同时出现，你只能使用set1，其他所有的字符都会被删除。

```shell
$ echo "hello 123 world 456" | tr -c -d '0-9 \t\n'
 123  456
 
$ echo "hello 123 world 456" | tr -c '0-9' ' '
      123       456
```

### 4. 使用tr压缩字符

格式: `tr -s [set] # set 表示需要压缩的字符`
> tr命令能够完成很多文本处理任务,它可以删除字符串中重复出现的字符。

```shell
$ echo "hellooo      wooooorld" | tr -s 'o '
hello world

$ echo -e "hello\n\n\nworld,hello\n\n\n\nshell."
hello


world,hello



shell.

$ echo -e "hello\n\n\nworld,hello\n\n\n\nshell." | tr -s '\n'
hello
world,hello
shell.
```

### 5. 巧用tr实现数字相加

```shell
$ echo "1 2 3 4 5 3 78 " | echo sum: $[ $(tr ' ' '+')]
sum: 96

$ cat data.txt
1
2
3
4
5

$ echo "1 2 3 4 5 3 78 " | echo sum: $[ $(tr ' ' '+') 0 ]
sum: 15
# 最后多出一个 0 是因为5后面有个`\n` 被替换成 `+`,加 0 抵消最后的加号.
```

#### 5.1. 巧用tr实现文件中数字相加

```shell
$ echo "hello 123 world 456" | tr -d 'a-z' | echo "sum: $[$(tr ' ' '+')]"
sum: 579

```

### 6. 字符类

tr可以将不同的字符类作为集合使用，所支持的字符类如下所示。  
     alnum：字母和数字。  
     alpha：字母。  
     cntrl：控制（非打印）字符。  
     digit：数字。  
     graph：图形字符。  
     lower：小写字母。  
     print：可打印字符。  
     punct：标点符号。  
     space：空白字符。  
     upper：大写字母。  
     xdigit：十六进制字符。  
可以按照下面的方式选择所需的字符类：

```shell
$ tr [:class:] [:class:]

$ tr '[:lower:]' '[:upper:]'

$ echo "hello 123 world 456" | tr '[:lower:]' '[:upper:]'
HELLO 123 WORLD 456
```

......    
[返回](../README.md)   
......    
