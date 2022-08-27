## shell 条件语句

### if 条件语句请看 [if condition statement](if_judgment_type.md)

# while 语句

```shell
#!/bin/bash 
num=0 
while ((num<10)) 
do
 echo ${num} 
 ((num += 1)) 
done
  
num=0 
while [ ${num} -lt 10 ] 
do
 echo ${num} 
 let "i+=1"  # 新版本 bash 使用 let 关键字作为数学计算
done
exit 0
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


