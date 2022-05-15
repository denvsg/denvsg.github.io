# first

## 介绍

本目录是一个关于 ```python``` while 循环语句学习主题

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

<br />
<br />
<br />
<br />
<br />

......      
[for 循环](for_loop_satetement.md)    
[回到目录](../Readme.md)      
......   


