## 列表 (`list`)

### 列表是 Python 中最基本的数据类型，也是最常用的数据类型之一。

列表的数据称为元素    
列表中的每个元素都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。

列表都可以进行的操作包括索引，切片，加，乘，检查成员。

### 列表是最常用的 Python 数据类型，使用方括号标记 `[]`

##### 列表的元素不需要具有相同的类型,并且，列表的元素可以是另一个列表。

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

> Python3包含6中内建的序列:
> 即列表、元组、字符串、Unicode字符串、buffer对象和 xrange 对象
> 但最常见最常用的是列表和元组。

```python
list1 = ['Google', 'Microsoft', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6]
list3 = ["a", "b", "c", "d", "e", "f"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```

#### 可以使用索引访问列表的值

```python
list1 = ['Google', 'Microsoft', 1997, 2000]
print(list1[1])  # Microsoft
print(list1[1:3])  # ['Microsoft',1997]
```

### 列表 `[list]` 的一些操作

#### 1. 增加元素 append

```python
lis1 = ["hello", 1, 2, 3]
lis1[2:] = [4, 5, 6, 7]
print(lis1)  # ["hello", 1, 2, 4, 5, 6, 7]

lis2 = ["hello", 1, 2, 3]
lis2.append(4)
print(lis2)  # ["hello", 1, 2, 3, 4]

lis3 = ["hello", 1, 2, 3]
lis3.insert(1, "python")
print(lis3)  # ['hello', 'python', 1, 2, 3]
```

#### 2. 删除元素

```python
lis0 = ["hello", 1, 2, 3]
lis0.clear()
print(lis0)  # []

lis1 = ["hello", 1, 2, 3]
del lis1[0]
print(lis1)  # [1, 2, 3]

lis2 = ["hello", 1, 2, 3]
lis2.remove(1)
print(lis2)  # ['hello', 2, 3]

lis3 = ["hello", 1, 2, 3]
p1 = lis3.pop()
print(p1, lis3)  # 3 ['hello', 1, 2]
p2 = lis3.pop(0)
print(p2, lis3)  # hello [1, 2]
```

#### 3. 更新列表

```python
lis1 = ["hello", 1, 2, 3]
lis1[1] = "python"
print(lis1)  # ['hello', 'python', 2, 3]
```

#### 4. 删除列表

```python
lis1 = ["hello", 1, 2, 3]
print(lis1)  # ['hello', 1, 2, 3]
del lis1
print(lis1)
# ['hello', 1, 2, 3]
# Traceback (most recent call last):
#  File "C:/Users/dsg/PycharmProjects/first/python/datetype/test.py", line 11, in <module>
#    print(lis1)
# NameError: name 'lis1' is not defined
```

### 列表 `[list]` 的一些内建函数

#### 获取列表元素len

```python
lis1 = ["hello", 1, 2, 3]
len_lis1 = len(lis1)
print(len_lis1)  # 4
```

#### 获取列表元素最值

```python
lis1 = [0, 34, 23, 1, 2, 3]
print(max(lis1))  # 34
print(min(lis1))  # 0
```

#### 列表拷贝

<br />
<br />
<br />
<br />
<br />

......     
[上一篇：元组](tuple.md)     
[回到目录](../Readme.md)    
[下一篇：字典](dict.md)    
......    



