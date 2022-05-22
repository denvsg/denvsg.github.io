# golang 正则表达式

```golang
# 示例，匹配电子邮件 及字符
package main

import (
	"fmt"
	"regexp"
)

const text = "which can be used to provide project-specific argument overrides."
const text2 = "my email is abc@def.com"

func main() {
	re := regexp.MustCompile("[a-zA-Z0-9]+@.+\\..+")
	re1 := regexp.MustCompile("\\bp[a-z]+\\b")
	match := re.FindString(text2)
	match2 := re1.FindString(text)
	match3 := re1.FindAllString(text,-1)
	fmt.Println(match)
	fmt.Println(match2)
	fmt.Println(match3)
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
