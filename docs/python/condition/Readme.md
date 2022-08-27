# first

#### 介绍

本目录是一个关于 ```python``` 条件语句学习

#### [python条件语句](Readme.md)

### 单 if 语句

```python
a = 5
if a > 0:
    print("a > 0")
```

### if-else 语句

```python
a = 5
if a > 0:
    print("a > 0")
else:
    print("a < 0")
```

### if-elif-else 嵌套语句

```python
a = 5
if a > 4:
    print("a > 0")
elif 0 < a < 4:
    print("0 < a < 4")
else:
    print("a < 0")
```

### 成员判断用作 if 条件

```python
a = "hello world,hello python!"
if "hello" in a:
    print("a contains hello")

l = ["hello", "world", "hello python!", 123.5]
if "world" in l:
    print("list l contains world")
```

### 字符串 列表 判空

```python
a = "hello world,hello python!"
if a:
    print("a is not None.")

l = ["hello", "world", "hello python!", 123.5]
if l:
    print("list l is not None.")
```

<br/>
<br/>

### 以下为 if 条件语句中常用的操作运算符:

| 操作符    | 描述           |  
|--------|--------------|
| <      | 小于           |  
| <=     | 小于或等于        |  
| \>     | 大于           |  
| \>=    | 大于或等于        |  
| ==     | 等于，比较两个值是否相等 |  
| !=     | 不等于          |
| in     | 成员存在         |
| not in | 成员不存在        |

<br />
<br />
<br />
<br />
<br />

......      
[回到目录](../contents_page.md)     
......   


