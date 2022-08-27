# C 语言 条件语句

## C 语言把任何非零和非空的值假定为 true，把零或 null 假定为 false。

#### 1. 单 if 语句

一个 if 语句 由一个布尔表达式后跟一个或多个语句组成。

```C
#include <stdio.h>

int main()
{
    int a=5;
    if(a>0)
    {
        printf("%d > 0\n",a);
    }
    return 0;
}
```

#### 2. if...else 语句

一个 if 语句 后可跟一个可选的 else 语句，else 语句在布尔表达式为假时执行。

```C
#include <stdio.h>

int main()
{
    int a=5;
    if(a>0)
    {
        printf("%d > 0\n",a);
    }else{
        printf("%d <= 0\n",a);
    }
    return 0;
}
```

#### 3. 嵌套 if 语句

在一个 if 或 else if 语句内使用另一个 if 或 else if 语句。

```C
#include <stdio.h>

int main()
{
    int a=5;
    if(a>0)
    {
        if(a > 3){
            printf("%d > 3\n",a);
        }else{
            printf("0 < %d < 3\n",a);
        }
    }else{
        printf("%d <= 0\n",a);
    }
    return 0;
}
```

#### 4. switch 语句

一个 switch 语句允许测试一个变量等于多个值时的情况。

```C
#include <stdio.h>

int main()
{
    int a=5;
    switch(a)
    {
        case 0: printf("%d = 0\n",a); break;
        case 1: printf("%d = 1\n",a); break;
        case 2: printf("%d = 2\n",a); break;
        case 3: printf("%d = 3\n",a); break;
        case 4: printf("%d = 4\n",a); break;
        case 5: printf("%d = 5\n",a); break;
        case 6: printf("%d = 6\n",a); break;
        case 7: printf("%d = 7\n",a); break;
        default:printf("%d more than 7 or less then 0.\n",a);
    }
    return 0;
}
```

#### 5. 嵌套 switch 语句

在一个 switch 语句内使用另一个 switch 语句。

#### 6. 三目运算

`Exp1 ? Exp2 : Exp3;`  
三目运算格式如上，exp1 条件满足执行exp2，否则执行exp3.  
因此，也可将其转化成 if-else 语句

```C
#include <stdio.h>

int main()
{
    int a=5;
    a > 0 : printf("%d > 0\n",a"):printf("%d < 0\n",a);
    return 0;
}
```

<br />
<br />
<br />
<br />
<br />

......     
[回到目录](../contents_page.md)     
......
