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
	package_code := generate_code_package("demo")
	write_to_file(package_code, "./demo/package.json")
	index_code := generate_code_index()
	write_to_file(index_code, "./demo/index.js")

	for i := 0; i < num-1; i++ {
		fn := fmt.Sprintf("./demo/demo%d.js", i)
		code := generate_code(i)
		write_to_file(code, fn)
		fmt.Println(code)
	}

	end_file := generate_code_end_file()
	end_file_name := fmt.Sprintf("./demo/demo"+"%d"+".js", num-1)
	write_to_file(end_file, end_file_name)

	time.Sleep(time.Duration(3) * time.Second) // wait 3 second
}

func generate_code_package(dirname string) string {
	code_template := `{
    "main":"index.js",
    "name": "` + "%s" + `"
}` + "\n"

	codes := fmt.Sprintf(code_template, dirname)
	return codes
}

func generate_code_index() string {
	code_template := `const { infoDemo, showInfoDemo } = require("./demo0")

export let info = "hello world demo"

export const showInfo = function () {
    console.log(infoDemo)
    showInfoDemo()
    console.log("show info")
}` + "\n"

	codes := fmt.Sprintf(code_template)
	return codes
}

func generate_code(number int) string {
	// code_template := `module.exports=function demo` + "%d" + `(){
	//     for (i = 0; i < 10; i++) {
	//         console.log("this is " + i + " times")
	//     }
	// }` + "\n"

	code_template2 := `const { infoDemo, showInfoDemo } = require("./demo` + "%d" + `")

export let info = "hello world demo"

export const showInfo = function () {
    for (i = 0; i < 10; i++) { 
        console.log(infoDemo)
        showInfoDemo()
        console.log("show info")
    }
}` + "\n"
	codes := fmt.Sprintf(code_template2, number+1)
	return codes
}

func generate_code_end_file() string {
	code_template := `export let info = "hello world demo"

export const showInfo = function () {
    console.log(infoDemo)
    showInfoDemo()
    console.log("show info")
}` + "\n"

	codes := fmt.Sprintf(code_template)
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
