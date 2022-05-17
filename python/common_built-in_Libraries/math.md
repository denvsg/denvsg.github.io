# math 数学模块

### math模块用于数学意义上的一些计算，常用的方法有：

1. math.pi：PI的值（3.141592653589793）。
2. math.floor(x)：返回一个小于等于x的最大整数（浮点类型），x可以是整数，也可以是小数，比如math.floor(1.001)返回1.0。
3. math.ceil(x)：返回一个大于等于x的最小整数（浮点类型），x可以是整数，也可以是小数，比如math.ceil(1.001)返回2.0。
4. math.fabs(x)：返回一个x的绝对值（浮点类型）。
5. math.factorial(x)：如果x是一个负数或是非整数（1.0这种数视为整数），则抛出一个ValueError异常。
6. math.fmod(x, y)：返回x除以y的余数（浮点类型）。
7. math.fsum(iterable)：返回一个浮点数迭代对象的和（浮点类型）。
8. math.pow(x, y)：返回x的y次幂（浮点类型）。

> 注：math模块中还有一些用于数学上的专业计算的函数，比如math.sin(s)、math.cos(x)等。