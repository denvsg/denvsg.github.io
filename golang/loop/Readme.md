# golang 循环

## Go 只有一种循环结构：for 循环。

基本的 for 循环由三部分组成，它们用分号隔开：

1. 初始化语句：在第一次迭代前执行
2. 条件表达式：在每次迭代前求值
3. 后置语句：在每次迭代的结尾执行  
   4.初始化语句通常为一句短变量声明，该变量声明仅在 for 语句的作用域中可见。

> 初始化语句和后置语句是可选的。

一旦条件表达式的布尔值为 false，循环迭代就会终止。

> 注意：和 C、Java、JavaScript 之类的语言不同，Go 的 for 语句后面的三个构成部分外没有小括号， 大括号 { } 则是必须的。

```golang
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
```

### 用作while 使用

**此时可以去掉分号，因为 C 的 while 在 Go 中也叫做 for。**
```golang
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
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
