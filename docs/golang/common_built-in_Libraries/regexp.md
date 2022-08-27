# golang regexp 库

#### 1. func Match(pattern string, b []byte) (matched bool, err error) // Match 报告字节切片 b 是否包含正则表达式模式的任何匹配项。更复杂的查询需要使用编译和完整的正则表达式接口。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	matched, err := regexp.Match(`foo.*`, []byte(`seafood`))
	fmt.Println(matched, err)
	matched, err = regexp.Match(`bar.*`, []byte(`seafood`))
	fmt.Println(matched, err)
	matched, err = regexp.Match(`a(b`, []byte(`seafood`))
	fmt.Println(matched, err)

}
```

#### 2. func MatchReader(pattern string, r io.RuneReader) (matched bool, err error) // MatchReader 报告 RuneReader 返回的文本是否包含与正则表达式模式的任何匹配项。更复杂的查询需要使用编译和完整的正则表达式接口。

#### 3. func MatchString(pattern string, s string) (matched bool, err error) // MatchString 报告字符串 s 是否包含正则表达式模式的任何匹配项。更复杂的查询需要使用编译和完整的正则表达式接口。

#### 4. func QuoteMeta(s string) string // QuoteMeta 返回一个字符串，该字符串转义参数文本内的所有正则表达式元字符;返回的字符串是与文本文本匹配的正则表达式。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	fmt.Println(regexp.QuoteMeta(`Escaping symbols like: .+*?()|[]{}^$`))
}
// Escaping symbols like: \.\+\*\?\(\)\|\[\]\{\}\^\$
```
#### 5. func Compile(expr string) (*Regexp, error) // 编译将分析正则表达式，如果成功，则返回可用于与文本匹配的正则表达式对象。

#### 6. func MustCompile(str string) *Regexp // MustCompile 类似于编译，但如果表达式无法解析，则会崩溃。它简化了保存已编译正则表达式的全局变量的安全初始化。

#### 7. func (re *Regexp) Find(b []byte) []byte // Find 返回一个切片，其中包含正则表达式 b 中最左边匹配项的文本。返回值为 nil 表示不匹配。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Printf("%q\n", re.Find([]byte(`seafood fool`))) // food
}
```

#### 8. func (re *Regexp) FindAll(b []byte, n int) [][]byte // FindAll是Find的“All”版本;它返回表达式的所有连续匹配项的切片，如包注释中的“All”描述所定义。返回值为 nil 表示不匹配。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Printf("%q\n", re.FindAll([]byte(`seafood fool`), -1)) // ["food" "fool"]
}
```

#### 9. func (re *Regexp) FindAllString(s string, n int) []string // FindAllString是FindString的“All”版本;它返回表达式的所有连续匹配项的切片，如包注释中的“All”描述所定义。返回值为 nil 表示不匹配。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a.`)
	fmt.Println(re.FindAllString("paranormal", -1))
	fmt.Println(re.FindAllString("paranormal", 2))
	fmt.Println(re.FindAllString("graal", -1))
	fmt.Println(re.FindAllString("none", -1))
}
```

#### 10. func (re *Regexp) FindSubmatch(b []byte) [][]byte // FindSubmatch 返回一个切片切片，其中包含 b 中正则表达式最左侧匹配的文本及其子表达式的匹配项（如果有），如包注释中的“子匹配”说明所定义。返回值为 nil 表示不匹配。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo(.?)`)
	fmt.Printf("%q\n", re.FindSubmatch([]byte(`seafood fool`)))
}
```

#### 11. func (re *Regexp) Longest() // 最长使将来的搜索更喜欢最左边最长的匹配项。也就是说，当与文本匹配时，正则表达式返回一个在输入（最左边）中尽可能早开始的匹配项，并在其中选择尽可能长的匹配项。此方法修改正则表达式，不能与任何其他方法同时调用

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(|b)`)
	fmt.Println(re.FindString("ab")) // a
	re.Longest()
	fmt.Println(re.FindString("ab")) // ab
}
```

#### 12. func (re *Regexp) Match(b []byte) bool // Match 报告字节切片 b 是否包含正则表达式 re 的任何匹配项。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`foo.?`)
	fmt.Println(re.Match([]byte(`seafood fool`))) // true
	fmt.Println(re.Match([]byte(`something else`))) // false
}
```

#### 13. func (re *Regexp) ReplaceAll(src, repl []byte) []byte // ReplaceAll 返回 src 的副本，将正则表达式的匹配项替换为替换文本 repl。在 repl 内部，$ 符号被解释为 Expand 中，因此例如 $1 表示第一个子匹配的文本

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`a(x*)b`)
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("T"))) // -T-T-
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("$1"))) // --xx-
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("$1W"))) // ---
	fmt.Printf("%s\n", re.ReplaceAll([]byte("-ab-axxb-"), []byte("${1}W"))) // -W-xxW-
}
```

#### 14. func (re *Regexp) Split(s string, n int) []string // 将切片 s 拆分为由表达式分隔的子字符串，并在这些表达式匹配项之间返回子字符串的切片。

此方法返回的切片由 FindAllString 返回的切片中未包含的所有 s 子字符串组成。在不包含元字符的表达式上调用时，它等效于字符串。

```golang
package main

import (
	"fmt"
	"regexp"
)

func main() {
	a := regexp.MustCompile(`a`) 
	fmt.Println(a.Split("banana", -1)) // [b n n ]
	fmt.Println(a.Split("banana", 0)) // []
	fmt.Println(a.Split("banana", 1)) // [banana]
	fmt.Println(a.Split("banana", 2)) // [b nana]
	zp := regexp.MustCompile(`z+`) 
	fmt.Println(zp.Split("pizza", -1))  // [pi a]
	fmt.Println(zp.Split("pizza", 0)) // []
	fmt.Println(zp.Split("pizza", 1)) // [pizza]
	fmt.Println(zp.Split("pizza", 2)) // [pi a]
}
```

[regexp usage](https://pkg.go.dev/regexp)

[back](Readme.md)