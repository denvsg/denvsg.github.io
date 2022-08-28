# sort 命令使用

## sort 命令可以对文件或标准输入进行排序

### 1. 排序一组文件

```shell
$ sort file1.txt file2.txt
andriod     2007
clang      1967
golang     2006
ios         2003
java       1991
python     1989
rust       2011
ubuntu      1999

$ sort file1.txt file2.txt > sorted.txt # 输出到文件
$ sort file1.txt file2.txt -o sorted.txt # 输出到文件
```

### 2. 按照数字排序

```shell
$ sort -n file1.txt file2.txt
1967     clang   
1989     python  
1991     java    
1999     ubuntu  
2003     ios     
2006     golang  
2007     andriod 
2011     rust    
```

### 3. 反序

```shell
$ sort -n -r file1.txt file2.txt
2011     rust  
2007     andriod
2006     golang
2003     ios    
1999     ubuntu 
1991     java  
1989     python
1967     clang    
```

### 4. 按月份排序

```shell
$ sort -M months.txt

```

### 5. 合并排序的文件

```shell
$ sort -m sorted1 sorted2
andriod     2007
clang      1967
golang     2006
ios         2003
java       1991
python     1989
rust       2011
ubuntu      1999
```

### 6. 检查文件是否排序

```shell
#!/usr/bin/env bash
sort -C filename
[ $? -eq 0 ] && echo Sorted || echo  Unsorted
```

### 7.按照列排序

```shell
$  sort -k 2 file.txt  # 依据第二列排序
mac        1884
unix       1961
linux      1991
windows    1996

$  sort -nk 2 file.txt  # 依据第二列按数字进行排序
mac        1884
unix       1961
linux      1991
windows    1996

$  sort -nrk 2 file.txt  # 依据第二列按数字进行反序排序
windows    1996
linux      1991
unix       1961
mac        1884
```

### 8. 选取键进行排序
```shell
$ sort -k 1.3,1.4 file1.txt  # 依据第一列的第3第4个字符进行排序
sort -k 1.3,1.4 file1.txt
clang      1967
golang     2006
rust       2011
python     1989
java       1991

sort -n -k 2.3,2.4 file1.txt # 依据第二列的第3第4个字符以数字进行排序
golang 2006
rust 2011
clang 1967
python 1989
java 1991
```

### 9. 删除列中相同的行
```shell
$ sort -n -k 3 data.txt
2 bata 200
3 gamma 200
1 alpha 300

$ sort -n -k 3 -u data.txt 
2 bata 200
1 alpha 300
```


......    
[返回](../README.md)   
......    
