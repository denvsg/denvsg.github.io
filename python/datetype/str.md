### 字符串

字符串，就是数字的小数形式 定义字符串可直接 `i = 'hello python'`
字符串都需要使用引号包裹，在 `python` 中，引号都表示字符串，但部分引号有其他作用

##### 字符串特性：

字符串可使用 `for` 循环来进行遍历，如:

```python
str = 'hello world!'
for char in str:
    print(char)
```

字符串具有索引切片：

```python
str = 'hello python'
print(str[3])  # l
print(str[1:3])  # ell
print(str[3:])  # l world
print(str[::-1])  # nohtyp olleh
```

字符串不可修改,不可变对象

```python
str = 'hello'
str1 = 'a' + str[2:]  # al0
print(id(str) == id(str))  # false
```



