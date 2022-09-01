# symbol shell的符号

##### . 执行脚本，在当前shell执行不需要执行权限，同 source,当前目录

```shell
[root@dveng ~]# . test.sh

[root@dveng ~]# ls . 
```

##### $ 标记变量和参数

```shell
[root@dveng ~]# cat test.sh 
echo $1,$2,$3,$4

[root@dveng ~]# ./test.sh 1 2 3 4
1,2,3,4

[root@dveng ~]# cat test.sh 
file="test.sh"
echo "file is ${file}"

[root@dveng ~]# cat test.sh 
echo "file is test.sh"
```

##### ^ 正则表达式的起始和排除

```shell
[root@dveng ~]# grep '^[a-d]' /etc/passwd
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
dsg:x:1000:1000:,,,:/home/dsg:/bin/bash

[root@dveng ~]# grep '[^a-z]' /etc/passwd
::_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
_apt:x:0:65534::/nonexistent:/bin/false
```

##### ()  子 shell 执行

##### $()  替换命令，同反引号 `\`\``

##### (())  比较数值，类似C语言，如类C for循环,数学计算

```shell
[root@dveng ~]# for ((i=0;i<3;i++));do echo $i; done
0
1
2

[root@dveng ~]# num=3;((num++));echo ${num}
4
```

##### [] 条件测试，同test 命令

```shell
[root@dveng ~]# [ "$a" ] && echo not null || echo null
null
```

##### $[] 整数数学计算

```shell
[root@dveng ~]# num=5;num=$[ num ** 2 ]; echo $num ;
25
```

##### [[]] 条件测试，支持拓展符号和正则表达式

```shell
[root@dveng ~]# num=5;[[ $num > 3 ]] && echo gather || less
gather

[root@dveng ~]# str="hello"; [[ "$str" == hello ]] && echo hello || echo null
hello

[root@dveng ~]# str="hello"; [[ $str == hell? ]] && echo hello || echo null
hello
```

##### {} 表示连续字符， 如{1..9}={1 2 3 4 5 6 7 8 9}

```shell
[root@dveng ~]# echo {1..8}
1 2 3 4 5 6 7 8

[root@dveng ~]# echo test{1..8}
test1 test2 test3 test4 test5 test6 test7 test8

[root@dveng ~]# echo {a..m}12
a12 b12 c12 d12 e12 f12 g12 h12 i12 j12 k12 l12 m12
```

##### ${} 变量标记和字符串的提取和替换

```shell
[root@dveng ~]# str="hello";echo ${str#*l}
lo
```

##### ～ 双括号正则表达式匹配

```shell
[root@dveng ~]# str="hello"; [[ "$str" =~ ^h ]] && echo hello || echo not
hello

[root@dveng ~]# str="hello"; [[ $str =~ h.*o ]] && echo hello || echo not
hello
```

##### ？

##### &

#####     * 

#####          
