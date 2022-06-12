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
	fmt.Print("当前目录是：")
	pwd, _ := os.Getwd()
	fmt.Println(pwd)
	fmt.Printf("输入需要生成的文件数量：")
	var num int
	fmt.Scan(&num)

	targetDirectory := "demo"
	_, errExistDir := os.Stat(targetDirectory)
	if errExistDir == nil {
		fmt.Println("\033[31mdir exist, delete it ...\033[0m")
		os.RemoveAll(targetDirectory)
	}
	err := os.Mkdir(targetDirectory, 0666) //当前目录新建demo目录
	if err != nil {
		fmt.Println(err)
	}
	package_code := generate_code_package(targetDirectory)
	write_to_file(package_code, targetDirectory+"/package.json")
	index_code := generate_code_index()
	write_to_file(index_code, targetDirectory+"/index.js")

	for i := 0; i < num-1; i++ {
		fn := fmt.Sprintf(targetDirectory+"/demo%d.js", i)
		code := generate_code(i)
		write_to_file(code, fn)
		fmt.Println(code)
	}

	end_file := generate_code_end_file(num - 1)
	end_file_name := fmt.Sprintf(targetDirectory+"/demo"+"%d"+".js", num-1)
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
	code_template := `const { infoDemo0, showInfoDemo0} = require("./demo0")

export let info = "hello world demo"

export const showInfo = function () {
    console.log(infoDemo0)
    showInfoDemo0()
    console.log("show info")
}` + "\n"

	codes := fmt.Sprintf(code_template)
	return codes
}

func generate_code(number int) string {
	// code_template := `module.exports=function demo` + "%d" + `(){
	//     for (var i = 0; i < 10; i++) {
	//         console.log("this is " + i + " times")
	//     }
	// }` + "\n"

	code_template2 := `const { infoDemo` + "%d" + `, showInfoDemo` + "%d" + ` } = require("./demo` + "%d" + `")

export let infoDemo` + "%d" + ` = "hello world demo"

export const showInfoDemo` + "%d" + ` = function () {
    for (var i = 0; i < 10; i++) { 
        console.log(infoDemo` + "%d" + `)
        showInfoDemo` + "%d" + `()
        console.log("show info")
    }
}` + "\n"
	codes := fmt.Sprintf(code_template2, number+1, number+1, number+1, number, number, number+1, number+1)
	return codes
}

func generate_code_end_file(num int) string {
	code_template := `export let infoDemo` + "%d" + ` = "hello world demo"

export const showInfoDemo` + "%d" + ` = function () {
    for (var i = 0; i < 10; i++) { 
        console.log(infoDemo` + "%d" + `)
        console.log("infoDemoshowInfoDemo` + "%d" + `()")
        console.log("show info")
    }
}` + "\n"

	codes := fmt.Sprintf(code_template, num, num, num, num)
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
