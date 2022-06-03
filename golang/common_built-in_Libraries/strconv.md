# golang 内置库 strconv

**strconv 实现与基本数据类型的字符串表示形式之间的转换。**

### 1. 数值转换

最常见的数字转换是 Atoi（字符串到 int）和 Itoa（int 到字符串）。

```golang
i, err := strconv.Atoi("-42")
s := strconv.Itoa(-42)
```

这些假定为十进制和 Go int 类型。

ParseBool、ParseFloat、ParseInt 和 ParseUint 将字符串转换为值：

```golang
b, err := strconv.ParseBool("true")
f, err := strconv.ParseFloat("3.1415", 64)
i, err := strconv.ParseInt("-42", 10, 64)
u, err := strconv.ParseUint("42", 10, 64)
```

解析函数返回最宽的类型（float64、int64 和 uint64），但如果 size 参数指定较窄的宽度，则结果可以转换为较窄的类型而不会丢失数据：

```golang
s := "2147483647" // biggest int32
i64, err := strconv.ParseInt(s, 10, 32)
...
i := int32(i64)
```

FormatBool、FormatFloat、FormatInt 和 FormatUint 将值转换为字符串：

```golang
s := strconv.FormatBool(true)
s := strconv.FormatFloat(3.1415, 'E', -1, 64)
s := strconv.FormatInt(-42, 16)
s := strconv.FormatUint(42, 16)
```

AppendBool、AppendFloat、AppendInt 和 AppendUint 类似，但将格式化的值追加到目标切片。

### 2. 字符串转换¶

Quote 和 QuoteToASCII 将字符串转换为带引号的 Go 字符串文本。后者通过转义任何非 ASCII Unicode 来保证结果是 ASCII 字符串，其值为 \u：

```golang
q := strconv.Quote("Hello, 世界")
q := strconv.QuoteToASCII("Hello, 世界")
```

QuoteRune 和 QuoteRuneToASCII 是相似的，但接受符文并返回引用的 Go 符文文字。

取消引用和取消引用字符取消引用 Go 字符串和符文文本。

#### Func Atoi

func Atoi(s string) (int, error)    
Atoi 等效于 ParseInt（s， 10， 0），转换为 int 类型。

```golang
package main

import (
    "fmt"
    "strconv"
)

func main() {
    v := "10"
    if s, err := strconv.Atoi(v); err == nil {
        fmt.Printf("%T, %v", s, s)
    }
}
```

```golang

```

```golang

```

```golang

```

[back](Readme.md)