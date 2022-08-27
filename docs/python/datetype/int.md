### 整型

int 整型，就是数字的整数形式，如 1, 只有一种整数类型 int，表示为长整型，没有 `python2` 中的 Long。

定义整形可直接 `i = 5`
当然，也可以通过字符串强制转化为整型，如

`int(x) `将 x 转换为一个整数。

```python
i = int("123")
print(type(i))  
```

整形数据可直接进行数学运算：

##### 1. 加法

```python
a = 3
b = 5
print(a + b)
```

##### 2. 减法

```python
a = 13
b = 5
print(a + b)
```

##### 3. 乘法

```python
a = 3
b = 5
print(a * b)
```

##### 4. 除法

> 注意： python除法 `/` 默认是带有小数位的，如需整除，可使用 `//`

```python
a = 3
b = 5
print(a / b)  # 0.8
print(a // b)  # 0
```

##### 5. 求模运算

> 取模即取余数

```python
a = 3
b = 5
print(a % b)  # 3 
```

##### 6. 乘方

> python 中，`**` 表示幂运算 `3**2` 便是3 的 平方

```python
a = 3
b = 5
print(a ** b)  
```

##### 6. 数值比较

数字还可以进行比较大小，一般用作条件判断

```python
a = 5
print(a > 5)  # False
```

[数字还可直接转换成 bool 类型](bool.md)

```python
a = 5
print(bool(a))
```

<br />
<br />
<br />
<br />
<br />

......     
[回到目录](../contents_page.md)   
[下一篇：浮点型](float.md)    
......    