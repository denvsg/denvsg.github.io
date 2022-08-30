# find 命令使用

## find 命令原理

> 沿着文件层次结构向下遍历，匹配符合条件的文件，执行相应的操作。  
> 默认的操作是打印出文件和目录，这也可以使用-print选项来指定。

### 1. 列出给定目录下所有的文件和子目录

```shell
$ find base_path 
```

#### 1.1 bash_path可以是任意路径，find会从该位置开始向下查找。

> . 指定当前目录，.. 指定父目录。
> print选项使用\n（换行符）分隔输出的每个文件或目录名。而-print0 选项则使用空字符'\0'来分隔。
> -print0的主要用法是将包含换行符或空白字符的文件名传给xargs命令。

```shell
$ find . -print
.history
Downloads
Downloads/tcl.fossil
Downloads/chapter2.doc
```

### 2. 根据文件名或正则表达式进行搜索

-name选项指定了待查找文件名的模式。这个模式可以是通配符，也可以是正则表达式。  
在 下面的例子中，'*.txt'能够匹配所有名字以.txt结尾的文件或目录。

```shell
$ find /home/slynux -name '*.txt' -print
```

> 注意*.txt两边的单引号。shell会扩展没有引号或是出现在双引号（"）中 的通配符。  
> 单引号能够阻止shell扩展*.txt，使得该字符串能够原封不动地传给 find命令。

#### 2.1 忽略大小写 -iname 参数

find命令有一个选项-iname（忽略字母大小写），该选项的作用和-name类似，只不过在匹配名字时会忽略大小写

```shell
$ ls 
examples.txt EXAMPLE.txt data.txt 

$ find . -iname "example*" -print 
./example.txt 
./EXAMPLE.txt
```

#### 2.2 find命令支持逻辑操作符

-a和-and选项可以执行逻辑与（AND）操作  
-o和-or选项可以执行逻辑或（OR）操作

```shell
$ ls 
file.txt some.jpg text.pdf stuff.png text.log

$ find . \( -name '*.log' -o -name '*.pdf' \) -print 
./text.pdf 
./text.log

$ find . \( -name '*e*' -and -name 's*' \) 
./some.jpg
```

#### 2.3 find -path参数可以限制所匹配文件的路径及名称。

```shell
$ find /home/users -path '*/log/*' -name '*.txt' –print
# 能够匹配文件/home/users/log/readme.txt，
# 但无法匹配/home/users/log.txt。
```

#### 2.4 find -regex 参数可以限制所匹配的文件。

> -iregex选项可以让正则表达式在匹配时忽略大小写。

```shell
$ ls 
new.PY next.jpg test.py script.sh 

$ find . -regex '.*\.(py\|sh\)$'
./test.py 
./script.sh

$ find . -iregex '.*\(\.py\|\.sh\)$' # 忽略大小写
./test.py 
./new.PY 
./script.sh 
```

### 3. 否定参数

> 可以用!排除匹配到的模式：`find . ! -name "*.txt" -print`

```shell
$ ls 
list.txt new.PY new.txt next.jpg test.py 

$ find . ! -name "*.txt" -print 
. 
./next.jpg 
./test.py 
./new.PY 
```

### 4.基于目录深度的搜索

> find命令在查找时会遍历完所有的子目录。  
> 默认情况下，find命令不会跟随符号链接。

**maxdepth 和 –mindepth 选项可以限制find命令遍历的目录深度。**

```shell
$ find -L /proc -maxdepth 1 -name 'bundlemaker.def' 2>/dev/null 
#  -L选项告诉find命令跟随符号链接
#  从/proc目录开始查找
#  -maxdepth 1将搜索范围仅限制在当前目录
#  -name 'bundlemaker.def'指定待查找的文件
#  2>/dev/null将有关循环链接的错误信息发送到空设备中

$ find . -mindepth 2 -name "f*" -print 
./dir1/dir2/file1 
./dir3/dir4/f2 
# 当前目录或dir1和dir3中包含以f开头的文件，它们也不会被打印出来。 
```

> maxdepth和-mindepth应该在find命令中及早出现。  
> 如果作为靠后的选项，有可能会影响到find的效率，因为它不得不进行一些不必要的检查。  
> 例如，如果-maxdepth出现在-type之后，find首先会找出-type所指定的文件，然后再在匹配的文件中过滤掉不符合指定深度的那些文件。  
> 但是如果反过来，在-type之前指定目录深度，那么find就能够在找到所有符合指定深度的文件后，再检查这些文件的类型，这才是最有效的搜索之道。

### 5. 根据文件类型搜索

> 类Unix系统将一切都视为文件。文件具有不同的类型，
> 例如普通文件f、目录d、字符设备c、块设备b、符号链接l、硬链接l、套接字s以及FIFO(p)等。

find命令可以**使用 -type 选项**对文件搜索进行过滤.  
借助这个选项，我们可以告诉find命令只匹配指定类型的文件.

```shell
$ # 只列出所有的目录（包括子目录）
$ find . -type d -print 

$ # 将文件和目录分别列出可不是件容易事。不过有了find就好办了。例如，只列出普通文件
$ find . -type f -print 

$ # 只列出符号链接
$ find . -type l -print
```

### 6. 根据文件的时间戳进行搜索

> Unix/Linux文件系统中的每一个文件都有3种时间戳。  
 访问时间（-atime）：用户最近一次访问文件的时间。  
 修改时间（-mtime）：文件内容最后一次被修改的时间。  
 变化时间（-ctime）：文件元数据（例如权限或所有权）最后一次改变的时间。

-atime、-mtime和-ctime可作为find的时间选项。  
它们可以用整数值来指定天数。  
这些数字前面可以加上-或+。-表示小于，+表示大于。

```shell
$ # 打印出在最近7天内被访问过的所有文件。
$ find . -type f -atime -7 -print 

$ # 打印出恰好在7天前被访问过的所有文件。
$ find . -type f -atime 7 -print 

$ # 打印出访问时间超过7天的所有文件。
$ find . -type f -atime +7 -print
```

-atime、-mtime以及-ctime都是以“天”为单位来计时的。  
find命令还支持以“分钟”为计时单位的选项。这些选项包括：

+ -amin（访问时间）；
+ -mmin（修改时间）；
+ -cmin（变化时间）；

```shell
$ # 打印出7分钟之前访问的所有文件：
$ find . -type f -amin +7 -print 

# –newer选项可以指定一个用于比较修改时间的参考文件，
# 然后找出比参考文件更新的（更近的修改时间）所有文件。

$ # 找出比file.txt修改时间更近的所有文件：
$ find . -type f -newer file.txt -print 
```

> find命令的时间戳处理选项有助于编写系统备份和维护脚本。

### 7. 根据文件大小的搜索

```shell
$ # 大于2KB的文件
$ find . -type f -size +2k 

$ # 小于2KB的文件
$ find . -type f -size -2k 

$ # 大小等于2KB的文件
$ find . -type f -size 2k 
```

除了k之外，还可以用其他文件大小单位。  
 b：块（512字节）。  
 c：字节。  
 w：字（2字节）。  
 k：千字节（1024字节）。  
 M：兆字节（1024K字节）。  
 G：吉字节（1024M字节）

### 8. 根据文件权限和所有权的匹配

-perm 参数指明find应该只匹配具有特定权限值的文件。

用参数 -user USER 就能够找出由某个特定用户所拥有的文件。  
参数USER可以是用户名或UID。

```shell
# -perm选项指明find应该只匹配具有特定权限值的文件。
$ # 打印出权限为644的文件
$ find . -type f -perm 644 -print 

$ # 打印出用户 user 拥有的所有文件
$ find . -type f -user user -print 
```

### 9. find 目录排除

find的执行过程中，跳过某些子目录能够提升性能和查找效率。   
在搜索时排除某些文件或目录的技巧叫作修剪。  
如何使用-prune选项排除某些符合条件的文件

```shell
$ find devel/source_path -name '.git' -prune -o -type f -print
```

-name ".git" –prune是命令中负责进行修剪的部分，它指明了.git目录应该被排除在外。  
-type f –print描述了要执行的操作。

#### 9.1 -prune参数

语法：`find <path> [-path <path> -prune -o] [...] -print`
> 中括号是可选项，[...] 代表前面的可选项可以多次重复  
> 注意: 多个部分需使用 -o 连接起来

```shell
$ # 查找当前目录下的 *.py, 排除掉 ./venv 和 ./build 目录
$ find . -path ./venv -prune -o -path ./build -prune -o -name "*.py" -print 
```

#### 9.2 使用 -prune 及括号

语法：`find <path> \( [-path <path> -o] [...] \) -prune -o -print`
> 和上一种类似，只不过将多个排除的路径放在了 () 中，注意括号用 \ 转义

```shell
$ find . \( -path ./venv -o -path ./build \) -prune -o -name "*.py" -print
```

#### 9.3 使用 not

语法：`find <path> [-not -path <path_pattern>] [...]`
> 这里的 <path_pattern> 是一个带通配符的模式，还需要加上引号，如：'./venv/*'

```shell
$ find . -not -path './build/*' -not -path './venv/*' -name "*.py"
```

#### 9.4 使用 ！

语法和第三种一样，只不过 -not 可以用 ! 来替换：

`find <path> [ ! -path <path_pattern>] [...] -print`

```shell
$ find . ! -path './build/*' ! -path '*/venv/*' -name "*.py"
```

### 10. find 执行相应操作

#### 10.1. 删除匹配的文件

find命令的-delete选项可以删除所匹配到的文件。

```shell
$ # 下面的命令能够从当前目录中删除.swp文件
$ find . -type f -name "*.swp" -delete # 只能删除文件或者空目录
```

#### 10.2. 执行命令

利用-exec选项，find命令可以结合其他命令使用。

**find命令使用一对花括号{}代表文件名。**

```shell
$ # 如果find命令找到了root所拥有的两个文件，那么它会将其所有者改为 user：
$ find . -type f -user root -exec chown user {} \; 
# 注意该命令结尾的\;。必须对分号进行转义，否则shell会将其视为find命令的结束，而非chown命令的结束。
```

> 为每个匹配到的文件调用命令可是个不小的开销。   
> 如果指定的命令接受多个参数（如chown），你可以换用加号（+）作为命令的结尾。   
> 这样find会生成一份包含所有搜索结果的列表，然后将其作为指定命令的参数，一次性执行。

##### 10.2.1 文件拼接

```shell
$ # 将给定目录中的所有C程序文件拼接起来写入单个文件all_c_files.txt。
$ find . -type f -name '*.c' -exec cat {} \;>all_c_files.txt
$ find . -type f -name '*.c' -exec cat {} > all_c_files.txt \;
$ fine . -type f -name '*.c' -exec cat {} >all_c_files.txt +
```

> 使用 > 操作符将来自find的数据重定向到all_c_files.txt文件，   
> 没有使用>>（追加）的原因是find命令的全部输出就只有一个数据流（stdin），   
> 而只有当多个数据流被追加到单个文件中时才有必要使用>>。


......    
[返回](./README.md)   
......    
