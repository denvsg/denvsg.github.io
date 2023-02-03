# 正则表达式 regular expression

## 正则表达式常用的方法：

### 1. re.match(pattern, str)

从头开始匹配，匹配成功返回

### 2. re.search(pattern, str)

从头开始匹配，匹配成功返回

### 3. re.find_all(pattern, str)

全部匹配，以列表形式返回匹配成功的字符  
如匹配失败返回空列表

### 4. re.spilt(pattern, str)

按正则字符开始切片，可以和字符串的split搭配使用，弥补  
字符串切片只能使用单一的字符

```python3
# 多选一匹配
import re

str1 = "This 3h, hello world 57min wait 102s. then there is go 66h."
ret = re.findall(r"\b\d+(?:min|h|s)\b", str1)
```

```shell
# 对应shell

str1 = "This 3h, hello world 57min wait 102s. then there is go 66h."
echo $str1 | grep - on '[0-9]\+[min|h|s]'
```

<br />

......   
<br />
<br />

[返回索引页](Readme.md)  
[回到主目录](../contents_page.md)   
......    
