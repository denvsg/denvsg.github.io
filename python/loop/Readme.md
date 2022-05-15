# first

## 介绍

本目录是一个关于 ```python``` 循环语句学习

### [python循环语句](Readme.md)

python 循环语句有两种， `while` 和 `for`

### while 语句

#### 1. while 语句后条件，满足条件则进入循环

> 注意：python 没有 `++` 语句，累加可以使用 `+= 1` 实现

```python
# 以累加50 为例
s = 0
count = 0
while count <= 50:
    s += count
    count += 1
print(s)
```

#### 2. while 死循环 的条件可以是 True 或者 1

```python
while True:
    s = input("请输入：")
    print("你输入的是：", s)
```

#### 3. while-else 语句

> while 循环条件不满足时，才会执行 else 语句

```python
c = 5
while c < 6:
    c += 1
else:
    print("else statement")
    print(f"c={c}")
```

### for 循环语句

#### 1. 序列迭代

```python
l = [1, 2, 3, 5, 9, 1, "as"]
for element in l:
    print(element)
```

#### 2. range() 函数

```python
l = [1, 2, 3, 5, 9, 1, "as"]
for element in range(7):
    print(l[element])
```

#### 3. for-else 语句

> for 循环正常执行完成，else 块才执行

```python
# 例1.不执行else
l = [1, 2, 3, 5, 9, 1, "as"]
for element in l:
    if element == 3:
        break
    print(element)
else:
    print("for else statement")

# 例2. 执行else
l = [1, 2, 3, 5, 9, 1, "as"]
for element in l:
    if element == 3:
        continue
    print(element)
else:
    print("for else statement")
```

#### 空语句 pass

Python pass是空语句，是为了保持程序结构的完整性。 pass 不做任何事情，一般用做占位语句，带补充内容等。 空语句也可使用 `...`
> 函数中常使用 三引号 作为空语句

```python
for i in range(9):
    pass

for i in range(9):
    ...

for i in range(9):
    ''''''
```

### [for 循环进阶操作：推导式](comprehensions.md)

推导式可以看作 for 的简写形式


<br />
<br />
<br />
<br />
<br />

......      
[回到目录](../Readme.md)     
......   


