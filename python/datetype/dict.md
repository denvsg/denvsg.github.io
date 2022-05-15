# 字典 dict

### 字典是一种映射类型，由键值对组成

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

d = {key1 : value1, key2 : value2, key3 : value3 }
> 注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。 字典的键必须是唯一的，但值则不必。  
> **字典的键必须是不可变类型，如int，str等**

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。 如：  
`dic = {'name': 'python', 'likes': 123, 'url': 'www.python.org'}`

<br />

##### 遍历字典方式

1. 使用 `for` 循环

```python
dic = {'name': 'python', 'likes': 123, 'url': 'www.python.org'}
for key in dic:
    print(key, dic[key])
```

2. 使用 `for items()`

```python
dic = {'name': 'python', 'likes': 123, 'url': 'www.python.org'}
for key, value in dic.items():
    print(key, value)
```

## 字典基础操作

### 创建字典

1. 使用大括号 { } 创建空字典：

```python
# 使用大括号 {} 来创建空字典
emptyDict = {}

# 输出字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))
```

2. 使用内建函数 dict() 创建字典：

```python
emptyDict = dict()

# 输出字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))
```

### 访问字典里的值

把相应的键放入到方括号中，如:
> _~~可以理解为一种特殊的列表，字典的键则是索引~~_

```python
dic = {'Name': 'python', 'Age': 31, 'Class': 'Math'}
print("dic['Name']: ", dic['Name'])
print("dic['Age']: ", dic['Age'])
```

### 修改字典里的值

```python
dic = {'Name': 'python', 'Age': 31, 'Class': 'Math'}
dic['Age'] = 55
print(dic)  # {'Name': 'python', 'Age': 55, 'Class': 'Math'}
dic["hoppy"] = "write"  # 当键不存在时，会给字典新增键值对，否则则修改键对应的值
print(dic)  # {'Name': 'python', 'Age': 55, 'Class': 'Math', 'hoppy': 'write'}
```

### 删除字典的键值对

```python
dic = {'Name': 'python', 'Age': 31, 'Class': 'Math', 'hoppy': 'write'}
del dic['Name']  # 删除键 'Name'
print(dic)  # {'Age': 31, 'Class': 'Math', 'hoppy': 'write'}
dic.clear()  # 清空字典
print(dic)  # {}
del dic  # 删除字典
print(dic)
# Traceback (most recent call last):
#   File "C:/Users/dsg/PycharmProjects/first/python/datetype/test.py", line 12, in <module>
#     print(dic)
# NameError: name 'dic' is not defined

```

<br />
<br />

## 字典的一些内建方法

### len(dict)

> 功能：计算字典元素个数，即键的总数

```python
dic = {'Name': 'python', 'Age': 31, 'Class': 'Math'}
print(len(dic))
```

### 

<br />
<br />
<br />
<br />
<br />

......     
[上一篇：列表](list.md)     
[回到目录](../Readme.md)    
[下一篇：集合](set.md)    
......   


