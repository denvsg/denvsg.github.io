# json 解析模块

### 对数据进行解码 加载json

#### 1. load 处理文件

```python
import json

with open("demo.json") as fp:
    data = json.load(fp)
```

#### 2. loads 处理字符串

```python
import json

data = {"name": "python", "age": 31, "site": "python.org"}

json_data = json.dumps(data)

json2_data = json.loads(json_data)

```

### 对数据进行编码 写入json

#### 1. dump 处理文件

```python
import json

data = {"name": "python", "age": 31, "site": "python.org"}

with open("demo.json") as fp:
    json.dump(data, fp)
```

#### 2. dumps 处理字符串

```python
import json

data = {"name": "python", "age": 31, "site": "python.org"}

json_data = json.dumps(data)
```
