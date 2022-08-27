# if 语句的判断种类

shell 的判断语句有三种：   
1： test 条件表达式  
2： [ 条件表达式 ]  
3： `[[ 条件表达式 ]] `   
其中，test+表达式 与 [] 一样，所以[] 中的字段需要使用空格隔开    
`[[]]` 和 [] 的区别为 双[] 支持拓展语法
> 注意：==，!= 符号默认是字符测试

## 1. if 条件判断

以等于为例：

| 符号  | 意义   |
|-----|------|
| -eq | 等于   |
| -ne | 不等于  |
| -gt | 大于   |      
| -lt | 小于   |      
| -ge | 大于等于 |
| -le | 小于等于 |

### 1.1 等于判断

```shell
# 判断上一条命令是否执行成功
echo hello shell
if [ $? -eq 0 ];then
  echo 执行成功！
fi 

# 上方的脚步也可写为：
echo hello shell
if [[ $? == 0 ]];then
  echo 执行成功！
fi 
```

### 1.2 字符串判断

| 字符   | 意义                                        |  
|------|-------------------------------------------|
| =,== | 等于                                        | 
| !=   | 不等于                                       | 
| -z   | 判断字符长度是为0                                 | 
| -n   | 判断字符长度不是为0                                | 
| $    | 检测字符串是否不为空，不为空返回 true。    [ $a ] 返回 true。 | 

> 注意：使用 `=` 作为条件判断时，等号左右要加上空格，否则会作为赋值语句

```shell
# 例1
str=hello
[ ${str} = "hello" ] && echo ${str} is hello

# 例1
[ ${str} == "hello" ] && echo ${str} is hello

# 例3 # 注意 [] 不支持拓展符号及正则，此处要使用 [[]]
[[ ${str} =~ ^h ]] && echo ${str} start with h

# 例4 # 变量为空好哦在为定义长度都是0
[ -z ${str} ] && echo ${str} lenth is zero.

# 例5
[ -n ${str} ] && echo ${str} lenth is not zero.

# 例6  判断字符串是否为空
[ ${str} ] && echo ${str} is not null

# 例7  获取字符串的长度
echo ${str} length is ${#str}
```

### 1.3 文件判断

| 字符       | 意义                                       | 简单示例                           |
|----------|------------------------------------------|--------------------------------|
| -b file  | 检测文件是否是块设备文件，如果是，则返回 true。               | [ -b $file ] 返回 false。         |
| -c file  | 检测文件是否是字符设备文件，如果是，则返回 true。              | [ -c $file ] 返回 false。         |
| -d file  | 检测文件是否是目录，如果是，则返回 true。                  | [ -d $file ] 返回 false。         |
| -e file  | 检测文件（包括目录）是否存在，如果是，则返回 true。             | [ -e $file ] 返回 true。          |
| -f file  | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。          |
| -g file  | 检测文件是否设置了 SGID 位，如果是，则返回 true。           | [ -g $file ] 返回 false。         |
| -h file  | 检测文件是否存在且是连接符号文件，如果是，则返回 true。           | [ -g $file ] 返回 false。         |
| -k file  | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。   | [ -k $file ] 返回 false。         |
| -p file  | 检测文件是否是有名管道，如果是，则返回 true。                | [ -p $file ] 返回 false。         |
| -u file  | 检测文件是否设置了 SUID 位，如果是，则返回 true。           | [ -u $file ] 返回 false。         |
| -r file  | 检测文件是否可读，如果是，则返回 true。                   | [ -r $file ] 返回 true。          |
| -s file  | 检测文件是否为空（文件大小是否大于0），不为空返回 true。          | [ -s $file ] 返回 true。          |
| -S file  | 检测文件是否是Socket文件，是则返回 true。               | [ -S $file ] 返回 true。          |
| -w file  | 检测文件是否可写，如果是，则返回 true。                   | [ -w $file ] 返回 true。          |
| -x file  | 检测文件是否可执行，如果是，则返回 true。                  | [ -x $file ] 返回 true。          |
| -nt file | 左边文件比右边文件新返回 true。                       | [ $file1 -nt $file2 ] 返回 true。 |
| -ot file | 左边文件比右边文件旧返回 true。                       | [ $file1 -ot $file2 ] 返回 true。 |

```shell
file1=a.sh
file2=b.sh

[ $file2 -nt $file1 ] && echo  $file2 is new than $file1
[ $file1 -ot $file2 ] && echo  $file1 is old than $file2
```

### 1.4 成员判断

```shell
str="hello world. This is a shell script"
if [[ ${str} =~ "shell" ]]; then
    echo shell in ssentence: ${str}
fi
```

### 1.5 逻辑运算

逻辑的(and)与(or)  (not)
&& 逻辑的 AND 的意思, -a 也是这个意思，两个条件同时成立，为真。    
|| 逻辑的 OR 的意思， -o 也是这个意思，两个条件一个成立，为真。
! 逻辑的 NOT 的意思,对条件去反值
> 注意： 使用 && 或 || 符号时，要使用 [[]]

## if 语句的分支结构

#### 1.单 if 分支结构

```shell
if condition;then 
    statement
fi
```

#### 2.if-else 分支结构

```shell
if condition ;then
    statement
else 
    statement
fi
```

#### 3.if-else-if 多分支嵌套结构

```shell
# 多分支
if condition1;then 
    statement
elif condition2;then 
    statement
elif condition3;then 
    statement
else 
    statement
fi

# 嵌套
if condition; then
    if condition;then 
        statement
    else 
        statement
    fi
else 
    statement
fi
```

#### 4.case 语句

```shell
case variable in
　　　　　mode1)
    statement1
    ;;
　　　　　mode2)
    statement2
    ;;
　　　　　mode3)
    statement3
    ;;
　　　　　*)
    default 
    ;;
esac
```


### [返回](Readme.md)