package test

import (
	"bytes"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"syscall"
	"testing"
)

const (
	ProjectPath    string = "C:/Users/dsg/DevEcoStudioProjects/MyApplication"
	PagesPath             = ProjectPath + "/entry/build/default/intermediates/assets/default/ets/pages"
	NodeModulePath        = ProjectPath + "/entry/build/default/intermediates/assets/default/node_modules"
)

func CheckEnv() {
	//name := os.Getenv("PATH")
	//fmt.Println("name is:", name)
	fmt.Println()
	gitCmd := exec.Command("git", "--version")
	errGit := gitCmd.Run()
	if errGit != nil {
		fmt.Println(errGit)
		fmt.Println("fail")
		return
	}
	fmt.Println("git ready.")

	nodeCmd := exec.Command("node", "-v")
	errNode := nodeCmd.Run()
	if errNode != nil {
		fmt.Println(errNode)
		fmt.Println("fail")
		return
	}
	fmt.Println("node ready.")

	npmCmd := exec.Command("npm", "-v")
	errNpm := npmCmd.Run()
	if errNpm != nil {
		fmt.Println(errNpm)
		fmt.Println("fail")
		return
	}
	fmt.Println("npm ready.")
	fmt.Println()
}

func f3() {
	binary, lookErr := exec.LookPath("sh 文件名")
	if lookErr != nil {
		panic(lookErr)
	}
	args := []string{""}
	env := os.Environ()
	execErr := syscall.Exec(binary, args, env)
	if execErr != nil {
		panic(execErr)
	}
}

func compile() {
	fmt.Println(os.Getwd())

	chErr := os.Chdir(ProjectPath)
	if chErr != nil {
		return
	}
	command := exec.Command("npm", "run", "build")
	command.Dir = ProjectPath

	//读取io.Writer类型的cmd.Stdout，再通过bytes.Buffer(缓冲byte类型的缓冲器)将byte类型转化为string类型(out.String():这是bytes类型提供的接口)
	var out bytes.Buffer
	command.Stdout = &out

	//Run执行c包含的命令，并阻塞直到完成。  这里stdout被取出，cmd.Wait()无法正确获取stdin,stdout,stderr，则阻塞在那了
	err := command.Run()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(out.String(), err)
	fmt.Println("compile complete.")
}

func clear() {
	fmt.Println(os.Getwd())

	chErr := os.Chdir(ProjectPath)
	if chErr != nil {
		return
	}

	//函数返回一个*Cmd，用于使用给出的参数执行name指定的程序
	command := exec.Command("npm", "run", "clear")
	command.Dir = ProjectPath

	//读取io.Writer类型的cmd.Stdout，再通过bytes.Buffer(缓冲byte类型的缓冲器)将byte类型转化为string类型(out.String():这是bytes类型提供的接口)
	var out bytes.Buffer
	command.Stdout = &out

	err := command.Run()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(out.String(), err)
	fmt.Println("Clean up complete.")

}

func TestMain(m *testing.M) {
	fmt.Println("start testing setup ...") // 测试之前的做一些设置
	CheckEnv()

	// 如果 TestMain 使用了 flags，这里应该加上flag.Parse()

	compile()
	retCode := m.Run() // 执行测试

	clear()
	fmt.Println("End test teardown ...") // 测试之后做一些拆卸工作
	os.Exit(retCode)                     // 退出测试
}

func TestCompilePages(t *testing.T) {

	_, err := os.Stat(PagesPath)
	if err == nil {
		fmt.Println("File exist")
	}
	if os.IsNotExist(err) {
		return
	}

	errDirs := filepath.Walk(PagesPath, func(path string, info os.FileInfo, err error) error {
		//fmt.Println(path)
		//fmt.Println(info.Name())
		if info.Name() == "index.abc" {
			fmt.Println("compile success")
		}
		return nil
	})
	if errDirs != nil {
		fmt.Println(errDirs)
		return
	}

	//files, err := ioutil.ReadDir(PagesPath)
	//if err != nil {
	//	log.Fatal(err)
	//}
	//for _, file := range files {
	//	if file.Name() == "index.abc" {
	//		fmt.Println("compile success")
	//	}
	//}
}

func TestCompileNodeModules(t *testing.T) {

	_, errExistDir := os.Stat(NodeModulePath)
	if errExistDir == nil {
		fmt.Println("dir exist")
	}
	if os.IsNotExist(errExistDir) {
		t.Error("dir not exist")
		return
	}

	err := filepath.Walk(NodeModulePath, func(path string, info os.FileInfo, err error) error {
		fmt.Println(path)
		fmt.Println(info.Name())
		return nil
	})
	if err != nil {
		return
	}
	t.Log(os.Getwd())
	fmt.Println(os.Getwd())
}

//C:\Users\dsg\DevEcoStudioProjects\MyApplication\entry\.preview\default\intermediates\assets\default\ets\pages
