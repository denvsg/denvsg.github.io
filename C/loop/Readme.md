# C 语言 循环

## 循环语句类型

### 1. for 循环

多次执行一个语句序列，简化管理循环变量的代码。

```C
#include <stdio.h>

int main()
{
    int i;
    int a=5;
    for(i=0;i<a;i++)
    {
        printf("%d\n",i);
    }
    return 0;
}
```

### 2. while 循环

当给定条件为真时，重复语句或语句组。它会在执行循环主体之前测试条件。

```C
#include <stdio.h>

int main()
{
    int a=5;
    while(i<a)
    {
        i++;
        printf("%d\n",i);
    }
    return 0;
}
```

### 3. do...while 循环

除了它是在循环主体结尾测试条件外，其他与 while 语句类似。

### 4. 嵌套循环

在 while、for 或 do..while 循环内使用一个或多个循环。

## 控制语句类型

### 1. break 语句

终止循环或 switch 语句，程序流将继续执行紧接着循环或 switch 的下一条语句。

```C
#include <stdio.h>

int main()
{
    int i;
    int a=5;
    for(i=0;i<a;i++)
    {
        if(i == 2) break;
        printf("%d\n",i);
    }
    return 0;
}
```

### 2. continue 语句

告诉一个循环体立刻停止本次循环迭代，重新开始下次循环迭代。

```C
#include <stdio.h>

int main()
{
    int i;
    int a=5;
    for(i=0;i<a;i++)
    {
        if(i == 2) continue;
        printf("%d\n",i);
    }
    return 0;
}
```

### 3. goto 语句

将控制转移到被标记的语句。但是不建议在程序中使用 goto 语句。

<br />
<br />
<br />
<br />
<br />

......     
[回到目录](../contents_page.md)     
......
