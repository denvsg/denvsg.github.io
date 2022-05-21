# first

## 介绍

本目录是一个关于 ```python``` for 循环语句学习

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
[while 循环](while_loop_statement.md)    
[回到目录](../contents_page.md)       
......   


