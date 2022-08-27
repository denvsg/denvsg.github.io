# sed 命令使用

### 1. 输出

```shell
sed -n '5p' file # 输出第5行
sed -n '5,9p' file # 输出第5-9行

# 正则搜索输出
sed -n '/com/p' file  # 输出包含 com 内容的行
```

### 2. 删除

```shell
sed [-i] '5d' file # 删除第5行
sed [-i] '2,5d' file # 删除第2-5行
sed [-i] '5,$d' file # 删除第5到最后的行

# 正则搜索输出
sed '/com/d' file  # 删除包含 com 内容的行，输出其他行内容
```

### 3. 新增 i 前面新增一行

```shell
sed [-i] '2i new line' file # 第2行前新增一行，即原第二行变成第三行
```

### 4. 新增 a 后面新增一行

```shell
sed [-i] '2a new line' file # 第2行后新增一行，即原第三行变成第四行
```

### 5. 取代 c 多行变成一行

```shell
sed '3,8c new modify line' file  # 3-8行(包含3，8行)修改成 new modify line
```

### 6. 修改

```shell
sed -e 's/con/com/g' file

sed -i 's/\.$/\!/g' file # 将每一行结尾 . 则换成 !

# 正则搜索输出
sed -n 's/com/""/' file  # 输出包含 com 内容的行
```
