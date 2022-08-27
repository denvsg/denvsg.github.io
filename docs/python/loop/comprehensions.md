# python 推导式

什么是推导式

#### 推导式是 for 循环的简化使用方法，使用推导式，将一个可迭代对象中的数据遍历到某一个容器当中。简单的来说就是用一行for循环语句，遍历一个可迭代对象中的所有数据，然后将遍历出来的数据进行处理放入对应的容器中的一个过程和方式。

和推导类似作用的还有三元运算符，三元运算符是条件判断语句的简化使用方法。

语法结构 `val for val in Iterable`

就是 存入容器中的数据 + for循环语句

表达方式 推导式有三种表达方式，分别用对应的符号包裹推导式语句。

```
列表推导试：[val for val in Iterable]
集合推导式：{val for val in Iterable}
字典推导式：{x,y for x,y in Iterable}
```

### 列表推导式

列表推到式，遍历出来的数据最终就会变成一个列表数据。

基本语法 列表中存入10条数据。

#### 常规写法

lst = []
for i in range(1, 11):
lst.append(i)
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#### 推导式写法

lst = [i for i in range(1, 11)]
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
其它使用方法 单循环推导式

#### 处理容器中的数据：[1, 2, 3, 4, 5] -> [3, 6, 9, 12, 15]

lst = [1, 2, 3, 4, 5]

#### 普通写法

new_lst = []
for i in lst:
res = i * 3 new_lst.append(res)
print(new_lst)  # [3, 6, 9, 12, 15]

#### 推导式写法

new_lst = [i * 3 for i in lst]
print(new_lst)  # [3, 6, 9, 12, 15]
带有判断条件的单循环推导式

#### 过滤出奇数

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#### 普通写法

new_lst = []
for i in lst:
if i % 2 == 1:
new_lst.append(i)
print(new_lst)  # [1, 3, 5, 7, 9]

#### 推导式写法

#### 推导式使用单项分支只能是在for语句结束之后使用

new_lst = [i for i in lst if i % 2 == 1]
print(new_lst)  # [1, 3, 5, 7, 9]
多循环推导式

#### 两个列表中的数据相加求和

lst = [1, 2, 3]
lst1 = [11, 22, 33]

#### 普通方法

new_lst = []
for i in lst:
for j in lst1:
res = i + j new_lst.append(res)
print(new_lst)  # [12, 23, 34, 13, 24, 35, 14, 25, 36]

#### 推导式写法

new_lst = [i + j for i in lst for j in lst1]
print(new_lst)  # [12, 23, 34, 13, 24, 35, 14, 25, 36]

## 列表推导式练习题

1、将字典中的数据变成['x=A', 'y=B', 'z=c']的样式 {'x': 'A', 'y': 'B', 'z': 'C' }

2、将所用元素变成纯小写
["ADDD","dddDD","DDaa","sss"]

3、x是0-5之间的偶数,y是0-5之间的奇数 把x,y组成一起变成元组,放到列表当中

4、使用列表推导式 制作所有99乘法表中的运算

5、求M,N中矩阵和元素的乘积 M = [[1,2,3], [4,5,6], [7,8,9]]
N = [[2,2,2], [3,3,3], [4,4,4]]

# 第五题解法之一

# =>实现效果1   [2, 4, 6, 12, 15, 18, 28, 32, 36]

# =>实现效果2   [[2, 4, 6], [12, 15, 18], [28, 32, 36]]

# 实现效果 1

lst_new = []
for i in range(len(M)) :
for j in range(len(N)) :
res = M[i][j] * N[i][j]
lst_new.append(res)
print(lst_new)

# 推导式写法

res = [M[i][j]*N[i][j] for i in range(len(M)) for j in range(len(N))]
print(res)

# 实现效果 2

lst_new = []
for i in range(len(M)) :
lst_new2 = []
for j in range(len(N)) :
res = M[i][j] * N[i][j]
lst_new2.append(res)
lst_new.append(lst_new2)
print(lst_new)

# 推导式写法

res = [[M[i][j]*N[i][j] for j in range(len(M))] for i in range(len(N))]
print(res)
集合推导式 集合推导式和列表推导式的用法基本一样，但是外面使用大括号包括，得到的数据是一个集合。

例题
'''
案例： 满足年龄在18到21，存款大于等于5000，小于等于5500的人 开卡格式为：尊贵VIP卡老X（姓氏），否则开卡格式为：抠脚大汉老X（姓氏） 把开卡的种类统计出来
'''
lst = [
{"name": "刘鑫炜", "age": 18, "money": 10000}, {"name": "刘聪", "age": 19, "money": 5100}, {"name": "刘子豪", "age": 20, "money": 4800}, {"name": "孔祥群", "age": 21, "money": 2000}, {"name": "宋云杰", "age": 18, "money": 20}
]

# 常规写法

setvar = set()

for i in lst:
if (18 <= i['age'] <= 21) and (5000 <= i['money'] <= 5500):
res = '尊贵VIP老' + i['name'][0]
else:
res = '抠脚老汉' + i['name'][0]
setvar.add(res)
print(setvar)   # {'尊贵VIP老刘', '抠脚老汉刘', '抠脚老汉孔', '抠脚老汉宋'}

# 打印显示只有4个元素，是因为集合的自动去重

# 使用集合推导式

# 推导式只能使用单项分支，但是可以在返回值使用三元运算符

setvar = {
"尊贵VIP卡老" + i["name"][0] if 18 <= i["age"] <= 21 and 5000 <= i["money"] <= 5500 else "抠脚大汉卡老" + i["name"][0] for i in
lst} print(setvar)   # {'抠脚大汉卡老孔', '抠脚大汉卡老刘', '尊贵VIP卡老刘', '抠脚大汉卡老宋'} 字典推导式
字典推导式也是一样的用法，但是字典的数据是以键值对的形式存在的，所以返回的数据、或者要将返回的数据变成两个，以对应键值。

基础语法 将列表中的键值对的变成一个字典

lst = [{'A': 'a'}, {'B': 'b'}]

dct = {k:v for i in lst for k,v in i.items()}

print(dct)  # {'A': 'a', 'B': 'b'} 字典推导式常用以配合的函数 函数 作用 enumerate 枚举，根据索引号码将可迭代对象中的值一一配对成元组，返回迭代器。 zip
将多个可迭代对象中的值一一对应组成元组，返回迭代器。 enumerate 功能 枚举，根据索引号码 和 Iterable 中的值，一个一个拿出来配对组成元组，放入迭代器中，然后返回迭代器。

语法 enumerate(iterable, [start = 0])

参数 iterable：可迭代数据 start：可以选择开始的索引号（默认从0开始索引）

返回值 迭代器

基本语法 from collections import Iterator lst = ['东', '南', '西', '北']

# 基本使用

it = enumerate(lst)  # 实现功能返回迭代器 print(isinstance(it, Iterator))     # True

# 强转成列表

new_lst = list(it)
print(new_lst)  # [(0, '东'), (1, '南'), (2, '西'), (3, '北')]

"""
可以看到里面的元列表中的数据和对应的索引号码一一对应成了元组
"""
上面的举例当中，如果使用字典推导式和enumerate函数配合，就可以用一句话达成组成一个字典的目的。

from collections import Iterator lst = ['东', '南', '西', '北']

# enumerate 配合使用字典推导式 变成字典

dct = {k: v for k, v in enumerate(lst)} print(dct)  # {0: '东', 1: '南', 2: '西', 3: '北'} zip 功能
将多个Iterable中的值，一个一个拿出来配对组成元组放入迭代器中，如果某个元素多出，没有匹配项就会被舍弃。

语法 zip(iterable, iterable1, ……)

参数就是一个个的可迭代对象。

返回值 迭代器

基本语法 下面的举例当中，将三个列表中的元素以一一对应组成元组，但是最小的列表中只有三个元素，所以只能一一对应组成三对元组，而多出的元素就被舍弃。

lst1 = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c', 'd']
lst3 = ['A', 'B', 'C']

it = zip(lst1, lst2, lst3)
lst = list(it)
print(lst)  # [(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C')]
为什么没有元组推导式 推导式我们到此学习完了，但是我们就发现，推导式就是在容器中使用一个for循环而已，为什么没有元组推导式？

请见生成器

优先使用推导式 在有的时候，我们需要在一个列表或者其它的一些容器中存放大量的值，我们一般会怎么使用呢？比如在初始化一个列表的时候我们使用for循环和append的方法去创建吗？

这里大家注意，如果条件允许的话，那么我们一定是要优先使用推导式而不是for循环加append的方式，原因很简单，因为底层逻辑的不同，使推导式的执行速度相比for循环加append更快。

import time

# 列表循环插入数据

start_time = time.perf_counter()
lst = []
for i in range(15000000):
lst.append(i)
end_time = time.perf_counter()
print(end_time - start_time)  # 1.7453036000000002

""" 推导式比循环速度更快 """
start_time = time.perf_counter()
new_lst1 = [i for i in range(15000000)]
end_time = time.perf_counter()
print(end_time - start_time)  # 0.7337192000000001 经过测试我们可以看到，推导式的速度大约是for循环的2倍多，是什么导致的？还记得我们之前使用过的dis模块吗？

import dis

def loop():
lst = []
for i in range(10):
lst.append(i)
return lst

def der():
lst = [i for i in range(10)]
return lst

dis.dis(loop)
print('-' * 100)
dis.dis(der)
结果如下：

4 0 BUILD_LIST 0 2 STORE_FAST 0 (lst)

5 4 SETUP_LOOP 26 (to 32)
6 LOAD_GLOBAL 0 (range)
8 LOAD_CONST 1 (10)
10 CALL_FUNCTION 1 12 GET_ITER
> > 14 FOR_ITER                14 (to 30)
16 STORE_FAST               1 (i)

6 18 LOAD_FAST 0 (lst)
20 LOAD_ATTR 1 (append)
22 LOAD_FAST 1 (i)
24 CALL_FUNCTION 1 26 POP_TOP 28 JUMP_ABSOLUTE 14
> > 30 POP_BLOCK

7     >>   32 LOAD_FAST 0 (lst)
34 RETURN_VALUE
-----------------------------------------------------------------------------
11 0 LOAD_CONST 1 (<code object <listcomp> at 0x000002C71AD950C0, file "tset.py", line 11>)
2 LOAD_CONST 2 ('der.<locals>.<listcomp>')
4 MAKE_FUNCTION 0 6 LOAD_GLOBAL 0 (range)
8 LOAD_CONST 3 (10)
10 CALL_FUNCTION 1 12 GET_ITER 14 CALL_FUNCTION 1 16 STORE_FAST 0 (lst)

12 18 LOAD_FAST 0 (lst)
20 RETURN_VALUE 从上述结果中我们就是可以看出，在这种情况下，for循环因为开始定义列表、循环中的append方法的是使用，比推导式要多出几个环节，因此速度相比之下变得很慢，这就是原因。

再次我们也再说一句，之后碰到关于速度和底层之类的疑惑的时候，就可以简单的使用timeit和dis去验证和简答的理解。