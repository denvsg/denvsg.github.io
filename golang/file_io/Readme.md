# golang 文件读写

### 1. 打开文件

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("./a.txt")
	if err != nil {
		fmt.Printf("open file fail, err:%v\n", err)
		return
	}
	fmt.Println("open file success.")
	defer file.Close()
}
```

### 2. 读取文件内容

##### 1. 使用 os 库 和切片读取文件

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("./a.txt")
	if err != nil {
		fmt.Printf("open file fail, err:%v\n", err)
		return
	}
	fmt.Println("open file success.")
	defer file.Close()
	
	var tmp = make([]byte, 128)
	size, err := file.Read(tmp)
	if err != nil {
		fmt.Printf("read file fail, err:%v\n", err)
		return
	}

	fmt.Printf("read file success, size is %d.\n", size)
	fmt.Println(string(tmp))
}
```

```golang
// 文件太大时循环读取
package main

import (
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("./a.txt")
	if err != nil {
		fmt.Printf("open file fail, err:%v\n", err)
		return
	}
	fmt.Println("open file success.")
	defer file.Close()
	
		for {
		var tmp = make([]byte, 128)
		size, err := file.Read(tmp)
		if err == io.EOF { // 读取到文件结尾
			fmt.Println(string(tmp))
			return
		}
		if err != nil {
			fmt.Printf("read file fail, err:%v\n", err)
			return
		}

		fmt.Printf("read file success, size is %d.\n", size)
		fmt.Println(string(tmp))
	}
}
```

##### 2. 使用 ioutil 库 和切片读取文件

```golang
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	data, err := ioutil.ReadFile("./a.txt")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Print(string(data))
}
```

##### 3. 使用 bufio 库读取文件

```golang
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	file, err := os.Open("./a.txt")
	if err != nil {
		fmt.Printf("open file fail, err:%v\n", err)
		return
	}
	fmt.Println("open file success.")
	defer file.Close()

	reader := bufio.NewReader(file)
	for {
		line,err:=reader.ReadString('\n')
		if err == io.EOF { // 读取到文件结尾
			fmt.Println(string(line))
			return
		}
		if err != nil {
			fmt.Println(err)
		}

		// if it was successful in reading the file then
		// print out the contents as a string
		fmt.Print(line)
	}
}
```

### 3. 写入文件内容

**打开文件方式**  

| 模式          | 意义  |
|-------------|-----|
| os.O_CREATE | 创建  |
| os.O_WRONLY | 只写  |
| os.O_APPEND | 追加  |
| os.O_RDONLY | 只读  |
| os.O_RWRD   | 读写  |
| os.O_TRUNC  | 清空  |

##### 1. 直接写入 使用 io/ioutil 库

```golang
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	data := []byte("Study golang make me happy.\n")
	err := ioutil.WriteFile("./b.txt", data, 0777)
	
	if err != nil {
		fmt.Println(err)
	}
}
```

##### 2. 直接写入,使用 bufio 库
```golang
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	data := "new data that wasn't there originally\n"

	file, err := os.OpenFile("b.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		fmt.Printf("open file fail, err:%v\n", err)
		return
	}
	defer file.Close()

	write := bufio.NewWriter(file)
	write.WriteString(data)
	write.Flush()
}
```

##### 3. 追加写入

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	data := "new contents lines\n"

	f, err := os.OpenFile("b.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	if _, err = f.WriteString(data); err != nil {
		panic(err)
	}
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
