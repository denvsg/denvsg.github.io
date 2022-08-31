# sed 命令使用

[1. 输出](#1-输出)  
[2. 删除](#2-删除)  
[3. 新增插入](#3-新增插入)  
[4. 新增追加](#4-新增追加)  
[5. 取代](#5-取代)  
[6. 修改](#6-修改)  
[7. 高阶操作](#7-高阶操作)  

## sed 参数

+ -i  &nbsp;  &nbsp; 修改文件内容 备份可以 -i.bak, bak为备份文件拓展名
+ -e  &nbsp;  &nbsp; 脚本, 多个条件
+ -f  &nbsp;  &nbsp; 使用脚本文件
+ -F  &nbsp;  &nbsp; 文本字段分隔符  
+ -n  &nbsp;  &nbsp; 取消自动打印,只输出指定行 一般和p搭配使用
+ -r  &nbsp;  &nbsp; 使用拓展正则表达式  
+ -v  &nbsp;  &nbsp; 自定义变量  

### 1 输出

```shell
[root@dveng ~] $ sed -n '5p' file # 输出第5行

[root@dveng ~] $ sed -n '5p' /etc/passwd
sync:x:4:65534:sync:/bin:/bin/sync

[root@dveng ~] $ sed -n '5,9p' file # 输出第5-9行

[root@dveng ~] $ sed -n '5,9p' /etc/passwd
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin

# 正则搜索输出
[root@dveng ~] $ sed -n '/com/p' file  # 输出包含 com 内容的行

[root@dveng ~] $ sed -n '/oo/p' /etc/passwd
root:x:0:0:root:/root:/bin/bash
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
```

### 2 删除

```shell
[root@dveng ~] $ sed [-i] '5d' file # 删除第5行

[root@dveng ~] $ sed [-i] '2,5d' file # 删除第2-5行

[root@dveng ~] $ sed [-i] '5,$d' file # 删除第5到最后的行

[root@dveng ~] $ sed [-i] '/^$/d' file # 删除空行

[root@dveng ~] $ sed [-i] '/./,$/!d' file # 删除开头的空行

[root@dveng ~] $ sed '/./,/^$/!d' file # 删除连续的空行,只保留一个空行

# 正则搜索删除
[root@dveng ~] $ sed '/com/d' file  # 删除包含 com 内容的行，输出其他行内容
```

### 3 新增插入

```shell
[root@dveng ~] $ sed [-i] '2i new line' file # 第2行前新增一行，即原第二行变成第三行

[root@dveng ~] $ sed '2i new line' /etc/passwd
root:x:0:0:root:/root:/bin/bash
new line
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin

```

### 4 新增追加

```shell
[root@dveng ~] $ sed [-i] '2a new line' file # 第2行后新增一行，即原第三行变成第四行

[root@dveng ~] $ sed '2a new line' /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
new line
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin

```

### 5 取代

```shell
[root@dveng ~] $ sed '3,8c new modify line' file  # 3-8行(包含3，8行)修改成 new modify line

[root@dveng ~] $ sed '3,8c new modify line' /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
new modify line
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin

```

### 6 修改

```shell
[root@dveng ~] $ sed -e 's/con/com/g' file

[root@dveng ~] $ sed -e 's/:/ /g' /etc/passwd
root x 0 0 root /root /bin/bash
daemon x 1 1 daemon /usr/sbin /usr/sbin/nologin
bin x 2 2 bin /bin /usr/sbin/nologin
sys x 3 3 sys /dev /usr/sbin/nologin

[root@dveng ~] $ sed -e 's/nol/AAAAA/g' /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/AAAAAogin
bin:x:2:2:bin:/bin:/usr/sbin/AAAAAogin
sys:x:3:3:sys:/dev:/usr/sbin/AAAAAogin


[root@dveng ~] $ sed -i 's/\.$/\!/g' file # 将每一行结尾 . 则换成 !

# 正则搜索输出
[root@dveng ~] $ sed -n 's/com/""/' file  # 将 com 替换为“”

[root@dveng ~] $ sed -e 's/nol/""/' /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/""ogin
bin:x:2:2:bin:/bin:/usr/sbin/""ogin
sys:x:3:3:sys:/dev:/usr/sbin/""ogin
```

### 7 高阶操作

#### 7.1. 多行命令

**sed 特殊命令**

- N: 将数据流的下一行加到当前行,组成多行处理
- D: 删除多行组的一行
- P: 打印多行组的一行

```shell
[root@dveng ~] $ sed -n 's/root/toor/p' /etc/passwd 
toor:x:0:0:root:/root:/bin/bash

[root@dveng ~] $ sed -n 'N;s/root/toor/p' /etc/passwd 
toor:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

```shell
[root@dveng ~] $ cat test.txt  
Today, I goto
center park with my friend.
There has flowers, beaufiful.

[root@dveng ~] $ sed 'N;/goto\ncenter/d' test.txt # 注意: 此处删除了两行
There has flowers, beaufiful.

[root@dveng ~] $ sed 'N;/goto\ncenter/D' test.txt
center park with my friend.
There has flowers, beaufiful.

# d 指令删除模式空间的当前行, 使用N指令时，下一行也加入了所以也被删除
# D 指令只删除模式空间的第一行, 到换行符为止(\n)
# 同理, 使用下面的命令可以删除goto字符之前的空行

[root@dveng ~] $ sed 'N;/^$/{N;/goto/D}' test.txt
```

#### 7.2. next命令

sed 的 n 指令会将sed编辑器移到数据流的下一行文本.  
sed 移到下一行前会执行完所有预设的命令,next改变了这个流程.

```shell
[root@dveng ~] $ cat file.txt
line 1 apple

line 3 pear


line 6 banans

[root@dveng ~] $ sed '/^$/d' file.txt  # 删除空行
line 1 apple
line 3 pear
line 6 banans

[root@dveng ~] $ sed '/apple/{n;d}' file.txt  # 删除apple后的空行
line 1 apple
line 3 pear


line 6 banans
```

#### 7.3. 合并文本行

- N 指令将下一行文本添加到模式空间中已有的文本后面，实现多行文本处理

```shell
[root@dveng ~] $ cat file.txt
line 1 apple
line 2 pear
line 6 banans


[root@dveng ~] $ sed '/apple/{N;s/\n/ /}' file.txt
line 1 apple line 2 pear
line 6 banans


[root@dveng ~] $ cat test.txt
Today, I goto
center park with my friend.
There has flowers, beaufiful.

[root@dveng ~] $ sed '
> s/goto center/go home/
> N
> s/goto\ncenter/go\nhome/
> ' test.txt
Today, I go
home park with my friend.
There has flowers, beaufiful.
```

```shell
[root@dveng ~] $ cat file.txt
line 1 apple
line 2 pear
line 6 banans

[root@dveng ~] $ sed '=' file.txt # sed 可以使用=打印当前行号
1
line 1 apple
2
line 2 pear
3
line 6 banans

[root@dveng ~] $ sed '=' file.txt | sed 'N;s/\n/ /' # sed 给文本添加行号
1 line 1 apple
2 line 2 pear
3 line 6 banans

````

#### 7.4. 保持空间

**保持空间(缓冲区)命令**

- h 将模式空间复制到保持空间
- H 将模式空间附加到保持空间
- g 将保持空间复制到模式空间
- G 将保持空间附加到模式空间
- x 交换模式空间和保持空间的内容

```shell
[root@dveng ~] $ cat test.txt
Today, I goto
center park with my friend.
There has flowers, beaufiful.

[root@dveng ~] $ sed -n '/park/{h;p;n;p;g;p}' test.txt
center park with my friend.
There has flowers, beaufiful.
center park with my friend.

# 1.过滤park字符的行
# 2.出现park行时，复制该行到保持空间
# 3.p指令打印模式空间第一行数据即park行
# 4.n指令将下一行问放到模式空间
# 5.p指令打印模式空间内容，也就是上面的, 即park的下一行
# 6.g指令将保持空间的内容放回模式空间，替换当前文本
# 7.p指令再次输出模式空间的内容，即park行
```

```shell
[root@dveng ~] $ cat test.txt
Today, I goto
center park with my friend.
There has flowers, beaufiful.

[root@dveng ~] $ sed 'G' test.txt # 添加空行，初始时，保持空间默认只有一个空行
Today, I goto

center park with my friend.

There has flowers, beaufiful.


[root@dveng ~] $ sed '$!G' test.txt # 最后一行不添加空行使用!排除
Today, I goto

center park with my friend.

There has flowers, beaufiful.


````

#### 7.5. 排除指令

sed支持使用"!"排除命令

```shell
[root@dveng ~] $ cat test.txt
Today, I goto
center park with my friend.
There has flowers, beaufiful.

[root@dveng ~] $ sed -n '/park/!p' test.txt
Today, I goto
There has flowers, beaufiful.
```

[go top](#sed-命令使用)  

<br />
<br />
<br />
<br />
<br />

......   
[返回](./Readme.md)  
......    
