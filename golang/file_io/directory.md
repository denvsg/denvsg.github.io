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
### 新建目录 


```golang
package main

import (
    "os"
    "fmt"
)

func main() {
    err := os.Mkdir('./demo', 0666)  //当前目录新建demo目录
    if err != nil {
        fmt.Println(err)
    }
    
    err := os.MkdirAll("./dir1/dir2/dir3", 0666) //当前目录新建多级目录
    if err != nil {
        fmt.Println(err)
    }
}
```

### 文件拷贝复制
```golang
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	src := "./a.txt"
	dst := "./c.txt"
	err := copy(src, dst)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("复制文件成功")
	}
}

func copy(src string, dst string) (err error) {
	byteStr, err1 := ioutil.ReadFile(src)
	if err1 != nil {
		return err1
	}
	err2 := ioutil.WriteFile(dst, byteStr, 006)
	if err2 != nil {
		return err2
	}
	return nil
}
```

```golang
package main

import (
	"fmt"
	"os"
	"io"
	"io/ioutil"
)

func main() {
	src := "./a.txt"
	dst := "./d.txt"
	err := copy(src, dst)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("复制文件成功")
	}
}


func copy(src string, dst string) (err error) {
    srcFile, err1 := os.Open(src)
    //关闭文件流，防止内存泄露
    defer srcFile.Close()
    dstFile, err2 := os.OpenFile(dst, os.O_CREATE|os.O_WRONLY, 0666)
    defer dstFile.Close()
    if err1 != nil {
        return err1
    }
    if err2 != nil {
        return err2
    }
    var tempSlice = make([]byte, 128)
    // srcFile.Read(tempSlice)
    for {
        //边读边写
        //读取
        n1, err := srcFile.Read(tempSlice)
        //如果读取完毕，跳出for循环
        if err == io.EOF {
            break
        }
        if err != nil {
            return err
        }
        //写入
        if _, err := dstFile.Write(tempSlice[:n1]); err != nil {
            return err
        }
    }
    return nil
}
```

### 删除文件或目录 

```golang
package main

import (
	"fmt"
	"os"
)

func main() {
    err := os.Remove("file.txt") //  删除文件
    if err != nil {
        fmt.Println(err)
    }
    
    err := os.Remove("./demo") // 删除目录
    if err != nil {
        fmt.Println(err)
    }
    
    err := os.RemoveAll("dir") // 
    if err != nil {
        fmt.Println(err)
    }
}
```

<br />
<br />
<br />
<br />
<br />

......     
[返回](./Readme.md)      
[回到目录](../contents_page.md)     
......
