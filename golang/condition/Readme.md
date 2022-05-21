# golang 条件语句

### Go 的 if 语句与 for 循环类似，表达式外无需小括号 ( ) ，而大括号 { } 则是必须的。

```golang
package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func main() {
	fmt.Println(sqrt(2), sqrt(-4))
}
```

### if 的简短语句

同 for 一样， if 语句可以在条件表达式前执行一个简单的语句。  
该语句声明的变量作用域仅在 if 之内。
> 即先赋值在进入条件语句，复制语句仅在条件语句`(if-else)`内生效

```golang
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}
```

<br />
<br />
<br />
<br />
<br />

......     
[回到目录](../Readme.md)     
......
