package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"os/exec"
	"runtime"
	"strings"
)

var root_dir, _ = os.Getwd()

func main() {
	getInfoSystem()

	printInfo("current directory is: ", root_dir)
	os.Chdir("D:\\Docs")
	cwd, _ := os.Getwd()
	printInfo("changed, directory is: ", cwd)

	printInfo()
	// exec_command()
}

//getInfoSystem 获取系统信息
func getInfoSystem() {
	sysType := runtime.GOOS
	printInfo("system type is: ", sysType)

	sysArch := runtime.GOARCH
	printInfo("chip arch is: ", sysArch)

	runtimeVersion := runtime.Version()
	printInfo("go version is: ", runtimeVersion)
}

// exec_command 执行cmd命令，并打印输出
func exec_command() error {
	cwd, _ := os.Getwd()
	fmt.Println("current directory is: ", cwd)
	cmd := exec.Command("ping", "-t", "127.0.0.1")
	fmt.Println(cmd.Args)

	// cmd.Stdin = os.Stdin
	// cmd.Stdout = os.Stdout
	// cmd.Stderr = os.Stderr

	stdout, err := cmd.StdoutPipe()
	stderr, errs := cmd.StderrPipe()
	if err != nil {
		return err
	}
	if errs != nil {
		return err
	}
	go func(err io.ReadCloser) {
		in := bufio.NewScanner(err)
		for in.Scan() {
			cmdRe := string(in.Bytes())
			panic(cmdRe)
		}
	}(stderr)

	// if err = cmd.Start(); err != nil {
	// 	return err
	// }
	// for {
	// 	tmp := make([]byte, 256)
	// 	_, err := stdout.Read(tmp)
	// 	fmt.Println(string(tmp))
	// 	if err != nil {
	// 		break
	// 	}
	// }
	// if err = cmd.Wait(); err != nil {
	// 	return err
	// }
	// return nil
	err = cmd.Start()
	in := bufio.NewScanner(stdout)
	for in.Scan() {
		cmdResult := string(in.Bytes())
		fmt.Println(cmdResult)
	}
	cmd.Wait()
	cmd.Wait()
	return err
}

//printInfo 输出重定向，终端和文件
func printInfo(msg ...string) {
	log_file := fmt.Sprintf("%s\\log.log", root_dir)
	fp, err := os.OpenFile(log_file, os.O_CREATE|os.O_APPEND|os.O_RDWR, os.ModePerm)
	if err != nil {
		return
	}
	defer func() {
		fp.Close()
	}()

	multiprinter := io.MultiWriter(os.Stdout, fp)
	log.SetOutput(multiprinter)

	log.SetFlags(log.Ldate | log.Ltime) // | log.Lshortfile)

	if len(msg) == 0 {
		msg = append(msg, "......")
	}
	massage := fmt.Sprintf(strings.Join(msg, " "))
	log.Println(massage)
}
