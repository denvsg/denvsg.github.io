# awk 命令使用

## awk命令可以对数据进行处理格式化展示

### awk指令是由模式，动作，或者模式和动作的组合组成。

格式: `awk [-F:] 'BEGIN {action} pattern {action} END {action}' file`

* 模式即pattern,可以类似理解成sed的模式匹配，可以由表达式组成，  
* 也可以是两个正斜杠之间的正则表达式。比如NR==1，这就是模式，可以把他理解为一个条件。
* 动作即action，是由在大括号里面的一条或多条语句组成，语句之间使用分号隔开。

> -F 定义列分隔符  
> -f 指定调用脚本  
> -v 定义变量  
> '  '引用代码块，awk执行语句必须包含在内  
> BEGIN{ } 初始化代码块，在对每一行进行处理之前，初始化代码，主要是引用全局变量，设置FS分隔符  
> { } 命令代码块，包含一条或多条命令  
> // 用来定义需要匹配的模式（字符串或者正则表达式），对满足匹配模式的行进行上条代码块的操作  
> END{ } 结尾代码块，在对每一行进行处理之后再执行的代码块，主要是进行最终计算或输出结尾摘要信息

#### **一些内置变量**

| 变量            | 意义                               |
|:--------------|:---------------------------------|
| $0            | 表示整个当前行                          |
| $1            | 每行第一个字段, $2... 依次类推              |
| NF            | 字段数量变量                           |
| NR            | 每行的记录号，多文件记录递增                   |
| FNR           | 与NR类似，不过多文件记录不递增，每个文件都从1开始       |
| \t            | 制表符                              |
| \n            | 换行符                              |
| FS            | BEGIN时定义分隔符                      |
| RS            | 输入的记录分隔符， 默认为换行符(即文本是按一行一行输入)    |
| ~             | 匹配，与==相比不是精确比较                   |
| !~            | 不匹配，不精确比较                        |
| ==            | 等于，必须全部相等，精确比较                   |
| !=            | 不等于，精确比较                         |
| &&　           | 逻辑与                              |
| &#124;&#124;  | 逻辑或                              |
| +             | 匹配时表示1个或1个以上                     |
| /[0-9][0-9]+/ | 两个或两个以上数字                        |
| /[0-9][0-9]*/ | 一个或一个以上数字                        |
| FILENAME      | 文件名                              |
| OFS           | 输出字段分隔符， 默认也是空格，可以改为制表符等         |
| ORS           | 输出的记录分隔符，默认为换行符,即处理结果也是一行一行输出到屏幕 |
| -F'[:#/]'     | 定义三个分隔符                          |
| ARGC          | 命令行参数个数                          |
| ARGV          | 命令行参数数组,ARGV[0]                  |

#### 参数及一些解释

- Pattern和{Action}需要用单引号引起来，防止shell作解释。
- Pattern是可选的。如果不指定，awk将处理输入文件中的所有记录。如果指定一个模式，awk则只处理匹配指定的模式的记录。
- {Action}为awk命令，可以是但个命令，也可以多个命令。整个Action（包括里面的所有命令）都必须放在{ 和 }之间。
- Action必须被{ }包裹，没有被{ }包裹的就是Patern
- file要处理的目标文件

### 基本的模式和动作

```awk
[root@dveng ~]# awk -F ":" 'NR>=2 && NR<=5{print NR,$1}' /etc/passwd
2 daemon
3 bin
4 sys
5 sync
命令说明：
-F 指定分隔符为冒号，相当于以“：”为菜刀，进行字段的切割。
NR>=2 && NR<=6：这部分表示模式，是一个条件，表示取第2行到第6行。
{print NR,$1}： 这部分表示动作，表示要输出NR行号和$1第一列。
```

### 只有模式

```awk
[root@dveng ~]# awk -F ":" 'NR>=2&&NR<=6' /etc/passwd
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin           
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync

命令说明：
-F指定分隔符为冒号
NR>=2&&NR<=6这部分是条件，表示取第2行到第6行。
但是这里没有动作，如果只有条件（模式）而没有动作，awk默认输出整行
```

### 只有动作

```awk
[root@dveng ~]# awk -F ":" '{print NR,$1}' /etc/passwd
1 root
2 bin
3 daemon
4 adm
5 lp
以下省略....

命令说明：
-F指定分隔符为冒号
这里没有条件，表示对每一行都处理
{print NR,$1}表示动作，显示NR行号与$1第一列
这里要理解没有条件的时候，awk会处理每一行。
```

#### 特殊动作 BEGIN

BEGIN 是 awk 的保留字，是一种特殊的条件类型。  
BEGIN 的执行时间是"在 awk 程序一开始，尚未读取任何数据之前"。

一旦 BEGIN 后的动作执行一次，当 awk 开始从文件中读入数据时，  
BEGIN 的条件就不再成立，所以 BEGIN 定义的动作只能被执行一次。

```shell
[root@dveng ~]# awk -F: 'BEGIN{printf "This is password file\n"}
{printf $1 "\t" $3 "\n"}' /etc/passwd
This is password file
root    0
daemon  1
bin     2
sys     3
sync    4
games   5
# awk命令只要检测不到完整的单引号就不会执行 
# 所以这条命令的换行不用加入"\"，就是一行命令
```

#### 特殊动作 END

END 也是 awk 的保留字，不过刚好和 BEGIN 相反。   
END 是在 awk 程序处理完所有数据，即将结束时执行的。  
END 后的动作只在程序结束时执行一次。

```shell
[root@dveng ~]# awk -F: 'END{printf "The END\n"}
{printf $1 "\t" $3 "\n"}' /etc/passwd
root    0
......
gitlog  112
gitdaemon       113
The END
```

#### 关系运算符

```shell
[root@dveng ~]$ awk -F: '$3 >= 87 {printf $1"\n"}' /etc/passwd;
nobody
systemd-network
systemd-resolve
systemd-timesync
messagebus

[root@dveng ~]$ awk -F: '$3 >= 87 {printf $1" "length($1) "\n"}' /etc/passwd;
nobody 6           
systemd-network 15 
systemd-resolve 15 
systemd-timesync 16
messagebus 10      
syslog 6


[root@dveng ~]$ awk -F: '$5 -/back/ {printf $1 "\n"}' /etc/passwd
backup
# # 如果第5个字段中包含"back"字符，则打印第1个字段
```
> 注意，在 awk 中，只有使用"//"包含的字符串，awk 命令才会査找。  
> 也就是说，字符串必须用"//"包含，awk 命令才能正确识别。

#### 正则表达式

+ 如果想让 awk 识别字符串，则必须使用"//"包含  

```awk
[root@dveng ~] # awk -F: '/oo/ {print}' /etc/passwd
root:x:0:0:root:/root:/bin/bash
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin

[root@dveng ~] $ df -h | awk '/sda[0-9]?/ {printf $1 "\t" $5 "\n"}' 
/dev/sda        6%
# 查询包含"sda"的行，并打印第一个字段和第五个字段
```

### 多个模式和动作

```awk
[root@dveng ~]# awk -F ":" 'NR==1{print NR,$1}NR==2{print NR,$NF}' /etc/passwd
1 root
2 /sbin/nologin

等价于: awk 'BEGIN{FS=":"} NR==1{print NR,$1} NR==2{print NR,$NF}' /etc/passwd
命令说明：
-F指定分隔符为冒号
这里有多个条件与动作的组合
NR==1表示条件，行号（NR）等于1的条件满足的时候，执行{print NR,$1}动作，输出行号与第一列。
NR==2表示条件，行号（NR）等于2的条件满足的时候，执行{print NR,$NF}动作，输出行号与最后一列（$NF）
```

### awk流程控制

* 多个条件{动作}可以用空格分隔，也可以用回车分隔。  
* 在一个动作中，如果需要执行多条命令，则需要用分隔，或用回车分隔。  
* 在awk中，变量的赋值与调用都不需要加入"$"符号。  
* 在条件中判断两个值是否相同，请使用"=="，以便和变量赋值进行区分。 

```awk
[root@dveng ~]# awk -F: '{if($3>100) print "large"; else print "small"}' /etc/passwd
small
small
small
以下省略....

[root@dveng ~]# awk -F: 'BEGIN{i=1} {while(i<NF) print NF,$i,i++}' /etc/passwd 
7 root 1
7 x 2
7 0 3
7 0 4
7 root 5
7 /root 6
以下省略....

# netstat -anp|awk 'NR!=1{a[$6]++} END{for (i in a) printf "%-20s %-10s %-5s \n", i,"\t",a[i]}'
[root@dveng ~]# netstat -anp|awk 'NR!=1{a[$6]++} END{for (i in a) print i,"\t",a[i]}'
(No info could be read for "-p": geteuid()=1000 but you should be root.)
SEQPACKET        1
and      1
I-Node   1
Foreign          1
以下省略....


```

[go top](#awk-命令使用)
<br />
<br />
<br />
<br />
<br />

......   
[返回](./Readme.md)  
......    


