## 字符串

字符串，就是数字的小数形式 定义字符串可直接 `i = 'hello python'`
字符串都需要使用引号包裹，在 `python` 中，引号都表示字符串，但部分引号也可以有其他作用

### 字符串特性：

##### 字符串可使用 `for` 循环来进行遍历，如:

```python
str1 = 'hello world!'
for char in str1:
    print(char)
```

##### 字符串具有索引切片：

```python
str1 = 'hello python'
print(str1[3])  # l
print(str1[1:3])  # ell
print(str1[3:])  # l world
print(str1[::-1])  # nohtyp olleh
```

##### 字符串不可修改,不可变对象

```python
str = 'hello'
str1 = 'a' + str[2:]  # al0
print(id(str) == id(str))  # false
```

### 字符串的一些函数方法

##### 1. 成员判断

```python
s = "hello python"
print("s" in s)
```

##### 2. 起始结束

```python
s = "hello python"
print(s.startswith("h"))
print(s.endswith("n"))
```

##### 3. 索引

```python
s = "hello python"
print(s.index("o"))  # 返回 o 的索引
print(s.find("llo"))  # 返回 llo 的其实索引
```

##### 4. 字符拼接 

字符拼接有多种方法

4.1. 使用 `+` 号

```python
a = "abc "
b = "hello"
print(a + b)
print(a, b)  # 直接输出也可使用逗号隔开，可以实现类似字符拼接的效果 
```

4.2. 使用占位符

```python
a = "abc "
b = "hello"
print("a: %s b: %s " % (a, b))
print("a: {} b: {}".format(a, b))
print(f"a: {a} b: {b}")  # python3.6+ 支持
```

4.3. 使用join函数

```python
a = "abc "
b = "hello"
print(b.join(a))  # ahellobhellochello 
```

##### 5. 字符串切成列表  
   `split()` 默认是以空格/制表符切割，可以传入指定字符进行分割

```python
a = "hello python nihao "
print(a.split())  # ahellobhellochello 
```

##### 6. 大小写转换  
   upper()  转换字符串中的小写字母为大写.  
   lower()  转换字符串中所有大写字符为小写.

<br />
<br />
<br />
<br />
<br />

......     
[上一篇：布尔型](bool.md)    
[回到目录](../Readme.md)     
[下一篇：元组](tuble.md)    
......    


