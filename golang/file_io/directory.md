# golang 目录操作

### 获取当前目录
 使用os库的 os.Getwd() 方法
```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	pwd, _ := os.Getwd()
	fmt.Println(pwd)
}
```
### 获取当前目录下的文件及目录
```golang
package main

import (
	"fmt"
	"os"
)

func main() {
	pwd, _ := os.Getwd()
	fmt.Println(pwd)
	
	fileList,err:=ioutil.ReadDir(pwd)
	if err!=nil{
		fmt.Printf("error,%v\n",err)
		return
	}
	fmt.Println(len(fileList))
	for i:=range fileList{
		fmt.Println(fileList[i].Name())
	}
}
```


### 获取当前目录下的所有文件及目录
```golang
package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	pwd, _ := os.Getwd()
	fmt.Println(pwd)
	
	filepath.Walk(pwd,func(path string, info os.FileInfo, err error) error {
		fmt.Println(path)
		fmt.Println(info.Name())
		return nil
	})
}
```

```golang
```

<br />
<br />
<br />
<br />
<br />

......     
[返回](./Readme.md)      
[回到目录](../Readme.md)     
......
