# shell 循环

## shell 循环有两种，while 和 for, until

### for 循环常见类型

```shell
# 方式1
for file in $(ls *.sh)  //for in格式是shell for的基本格式和js/python的for in类似 
do
    echo ${file}
done
  
# 方式2
for ((i=0;i<10;i++))    //注意是双小括号,由于受其他语言的影响,很容易搞错 
do
    echo -n $i 
done
  
# 方式3
for i in 0 1 2 3 4 5 6 7 8 9 
do
    echo -n $i 
done

# 方式4
for i in "0 1 2 3 4 5 6 7 8 9"  //这个和上面是有区别的，这个循环只循环了一次，双引号里面只是一个变量 可使用 seq生成序列
do
    echo -n $i 
done

# 方式5  生成序列，与方式3 一致
for i in `seq 1 9`
do
    echo $i
done
```

### while 循环常见类型

```shell
i=0 
while ((i<9)) 
do
    echo $i 
    ((i += 1)) 
done
  
i=0 
while [ $i -lt 9 ] 
do
    echo $i 
    let "i+=1"  
done
```

### until 循环常见类型
```shell
END_CONDITION=end 
until [ "$var1" = "$END_CONDITION" ] //读取的变量根设定的变量相等时退出循环，不然永远循环 
do
    echo "Input variable #1 "
    echo "($END_CONDITION to exit)"
    read var1 
    echo "variable #1 = $var1"
    echo
done 
```

<br />
<br />
<br />
<br />
<br />

......   
[comment]: <> ([上一篇：布尔型]&#40;bool.md&#41;    )
[回到目录](../Readme.md)

[comment]: <> ([下一篇：元组]&#40;tuble.md&#41;    )
......    

