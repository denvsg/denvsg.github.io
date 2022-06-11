// build with command: go build generate_js_code.go
// run with command: go run generate_js_code.go
package main

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

func main() {
	fmt.Printf("输入需要生成的数目：")
	var num int
	fmt.Scan(&num)

	fmt.Println(os.Getwd())
	err := os.Mkdir("./demo", 0666) //当前目录新建demo目录
	if err != nil {
		fmt.Println(err)
	}

	for i := 0; i < num; i++ {
		fn := fmt.Sprintf("./demo/demo%d.js", i)
		code := generate_code(i)
		write_to_file(code, fn)
		fmt.Println(code)
	}
	time.Sleep(time.Duration(3) * time.Second) // wait 3 second
}

func generate_code(number int) string {
	code_template := `module.exports=function demo` + "%d" + `(){
        for (i = 0; i < 10; i++) { 
            console.log("this is " + i + " times")
        }
    }` + "\n"
	codes := fmt.Sprintf(code_template, number)
	return codes
}

func write_to_file(code string, filename string) {
	file, err := os.OpenFile(filename, os.O_TRUNC|os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		fmt.Printf("open file fail, err:%v\n", err)
		return
	}
	defer file.Close()

	write := bufio.NewWriter(file)
	write.WriteString(code)
	write.Flush()
}
