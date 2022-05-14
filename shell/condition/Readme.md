## shell 条件语句

1. 数字比较  
   数字比较有两种形式   
   1.1. 使用 eq 的形式

```shell
if [ a -eq 0 ];then
    echo a=0
fi 
```

1.2. 使用 = 的形式

```shell
if [[ a == 0 ]];then
    echo a=0
fi 
```  

2. 字符串比较
3. 字符串成员判断

```shell
a=(abc def ghm)
if [[ a =~ abc ]];then
    echo abc in a
fi 
```  

<br />
<br />
<br />
<br />
<br />

[comment]: <> ([上一篇：布尔型]&#40;bool.md&#41;    )
[回到目录](../Readme.md)

[comment]: <> ([下一篇：元组]&#40;tuble.md&#41;    )
......    


