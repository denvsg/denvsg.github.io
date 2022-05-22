# golang 内置库 strings

## 常用函数

### 1. func Clone(s string) string // 克隆返回 的全新副本。它保证将 s 的副本复制到新的分配中，这在仅保留大得多的字符串的一个小子字符串时可能很重要。使用克隆可以帮助此类程序使用更少的内存。当然，由于使用克隆会复制副本，因此过度使用克隆会使程序使用更多内存。克隆通常只应很少使用，并且仅当分析表明需要时才使用。对于长度为零的字符串，将返回字符串 “”，并且不进行任何分配。
### 2. func Compare(a, b string) int // Compare 返回一个整数，该整数按字典顺序比较两个字符串。如果 a == b，则结果为 0;如果 a < b，则结果为 -1;如果> b，则结果为 +1。
包含比较仅用于与包字节的对称性。使用内置的字符串比较运算符 ==、<、>等通常更清晰且始终更快。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Compare("a", "b"))
	fmt.Println(strings.Compare("a", "a"))
	fmt.Println(strings.Compare("b", "a"))
}
```


### 3. func Contains(s, substr string) bool // 包含子字符串是否在 s 内的报告。
```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Contains("seafood", "foo"))  // true
	fmt.Println(strings.Contains("seafood", "bar"))  // false
	fmt.Println(strings.Contains("seafood", ""))  // true
	fmt.Println(strings.Contains("", ""))  //true
}
```

### 4. func Count(s, substr string) int // Count 计算以 s 为单位的 substr 的非重叠实例数。如果 substr 是空字符串，则 Count 返回 1 + 以 s 为单位的 Unicode 码位数

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Count("cheese", "e"))  // 3
	fmt.Println(strings.Count("five", "")) // before & after each rune  // 5
}
```

### 5. func Index(s, substr string) int // 返回 s 中 substr 的第一个实例的索引，如果 s 中不存在 substr，则返回 -1
```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Index("chicken", "ken"))  // 4
	fmt.Println(strings.Index("chicken", "dmr"))  / -1
}
```
### 6. func Join(elems []string, sep string) string  // Join 连接其第一个参数的元素以创建单个字符串。分隔符字符串 sep 放置在结果字符串中的元素之间。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	s := []string{"foo", "bar", "baz"}
	fmt.Println(strings.Join(s, ", ")) // foo, bar, baz
}
```

### 7. func LastIndex(s, substr string) int // LastIndex 返回 s 中 substr 的最后一个实例的索引，如果 s 中不存在 substr，则返回 -1。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Index("go gopher", "go"))  // 0
	fmt.Println(strings.LastIndex("go gopher", "go")) // 3
	fmt.Println(strings.LastIndex("go gopher", "rodent")) // -1
}
```

### 8. func Map(mapping func(rune) rune, s string) string // Map 返回字符串 s 的副本，其中所有字符都根据映射函数进行了修改。如果映射返回负值，则从字符串中删除该字符，不进行替换。
```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	rot13 := func(r rune) rune {
		switch {
		case r >= 'A' && r <= 'Z':
			return 'A' + (r-'A'+13)%26
		case r >= 'a' && r <= 'z':
			return 'a' + (r-'a'+13)%26
		}
		return r
	}
	fmt.Println(strings.Map(rot13, "'Twas brillig and the slithy gopher..."))
}
// 'Gjnf oevyyvt naq gur fyvgul tbcure...
```

### 9. func Replace(s, old, new string, n int) string //Replace 返回字符串 s 的副本，其中包含由 new 替换的旧实例的前 n 个非重叠实例。如果 old 为空，它将在字符串的开头和每个 UTF-8 序列之后匹配，从而为 k-rune 字符串产生最多 k+1 个替换。如果 n < 0，则对替换次数没有限制。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Replace("oink oink oink", "k", "ky", 2)) // oinky oinky oink
	fmt.Println(strings.Replace("oink oink oink", "oink", "moo", -1)) // moo moo moo
}
```

### 10. func Split(s, sep string) []string // 将切片 s 拆分为由 sep 分隔的所有子字符串，并在这些分隔符之间返回子字符串的切片。  
如果 s 不包含 sep 并且 sep 不为空，则 Split 返回长度为 1 的切片，其唯一元素为 s。  
如果 sep 为空，则拆分在每个 UTF-8 序列之后拆分。如果 s 和 sep 都为空，则 Split 返回一个空切片。  
它等效于计数为 -1 的 SplitN。  

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Printf("%q\n", strings.Split("a,b,c", ",")) // ["a" "b" "c"]
	fmt.Printf("%q\n", strings.Split("a man a plan a canal panama", "a ")) // ["" "man " "plan " "canal panama"]
	fmt.Printf("%q\n", strings.Split(" xyz ", "")) // [" " "x" "y" "z" " "]
	fmt.Printf("%q\n", strings.Split("", "Bernardo O'Higgins")) // [""]
}
```
### 11. func ToLower(s string) string // ToLower 返回 s，其中所有 Unicode 字母都映射到其小写字母。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ToLower("Gopher")) // gopher
}
```
### 12. func ToUpper(s string) string // ToUpper 返回 s，其中所有 Unicode 字母都映射到其大写字母。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ToUpper("Gopher")) // GOPHER
}
```
### 13. func Trim(s, cutset string) string // Trim 返回字符串 s 的一个切片，其中删除了 cutset 中包含的所有前导和尾随 Unicode 代码点。

```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Print(strings.Trim("¡¡¡Hello, Gophers!!!", "!¡")) // Hello, Gophers
}
```
### 14. func TrimFunc(s string, f func(rune) bool) string // TrimFunc 返回字符串 s 的一部分，其中删除了满足 f（c） 的所有前导和尾随 Unicode 码位 c。

```golang
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Print(strings.TrimFunc("¡¡¡Hello, Gophers!!!", func(r rune) bool {
		return !unicode.IsLetter(r) && !unicode.IsNumber(r)
	}))
}
// Hello, Gophers
```
### 15. func TrimPrefix(s, prefix string) string // TrimPrefix 返回不带前导前缀字符串的 s。如果 s 不以前缀开头，则返回 s 不变。
```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	var s = "¡¡¡Hello, Gophers!!!"
	s = strings.TrimPrefix(s, "¡¡¡Hello, ")
	s = strings.TrimPrefix(s, "¡¡¡Howdy, ") 
	fmt.Print(s) // Gophers!!!
}
```

### 16. func TrimSuffix(s, suffix string) string // TrimSendix 返回 s 而不提供尾随后缀字符串。如果 s 不以后缀结尾，则返回 s 不变。


```golang
package main

import (
	"fmt"
	"strings"
)

func main() {
	var s = "¡¡¡Hello, Gophers!!!"
	s = strings.TrimSuffix(s, ", Gophers!!!")
	s = strings.TrimSuffix(s, ", Marmots!!!")
	fmt.Print(s) // ¡¡¡Hello
}
```



[strings usage](https://pkg.go.dev/strin)