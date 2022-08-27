package main

import (
	"archive/zip"
	"bufio"
	"fmt"
	"io"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
	"sync"
	// "golang.org/x/text/encoding/simplifiedchinese"
)

type Charset string

const (
	UTF8    = Charset("UTF-8")
	GB18030 = Charset("GB18030")
)

func main() {
	fmt.Println(os.Getwd())
	os.Chdir("D:\\program\\Goprom\\src")
	sysType := runtime.GOOS
	fmt.Println(sysType)
	// exec_command()
	// command()
	exec_command_decode()
	// unzip_file("D:\\Docs\\doas-6.3p5.zip")
}
func exec_command() error {
	cmd := exec.Command("ping", "-t", "127.0.0.1")
	fmt.Println(cmd.Args)

	// cmd.Stdin = os.Stdin
	// cmd.Stdout = os.Stdout
	// cmd.Stderr = os.Stderr

	stdout, err := cmd.StdoutPipe()
	cmd.Stderr = cmd.Stdout
	if err != nil {
		return err
	}

	if err = cmd.Start(); err != nil {
		return err
	}

	for {
		tmp := make([]byte, 256)
		_, err := stdout.Read(tmp)
		fmt.Println(string(tmp))
		if err != nil {
			break
		}
	}
	if err = cmd.Wait(); err != nil {
		return err
	}
	return nil
}

func command() error {
	cmd := exec.Command("cmd", "/c", "ping", "-t", "127.0.0.1")
	fmt.Println(cmd.Args)
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return err
	}

	var wg sync.WaitGroup
	var read string
	wg.Add(2)
	go func(wg *sync.WaitGroup) {
		defer wg.Done()
		reader := bufio.NewReader(stdout)
		for {
			read, err = reader.ReadString('\n')
			if err != nil || err == io.EOF {
				return
			}
			fmt.Print(read)
			// if strings.Contains(read, "aaa") {
			// 	fmt.Print(read)
			// 	cancelFunc()
			// }
		}
	}(&wg)

	stderr, err := cmd.StderrPipe()
	if err != nil {
		return err
	}
	go func(wg *sync.WaitGroup) {
		defer wg.Done()
		reader := bufio.NewReader(stderr)
		for {
			read, err = reader.ReadString('\n')
			if err != nil || err == io.EOF {
				return
			}
			fmt.Print(read)
			// if strings.Contains(read, "aaa") {
			// 	fmt.Print(read)
			// 	cancelFunc()
			// }
		}
	}(&wg)

	err = cmd.Start()
	wg.Wait()
	return err
}

func unzip_file(zipFile string) error {
	dstPath := filepath.Dir(zipFile)
	fmt.Println("unzip path: ", dstPath)
	archive, err := zip.OpenReader(zipFile)
	if err != nil {
		return err
	}
	defer archive.Close()

	for _, file := range archive.File {
		filePath := filepath.Join(dstPath, file.Name)
		fmt.Println("unzip file ", filePath)
		if !strings.HasPrefix(filePath, filepath.Clean(dstPath)+string(os.PathSeparator)) {
			fmt.Println("invalid file path", filePath)
			fmt.Println("invalid file path", filepath.Clean(dstPath)+string(os.PathSeparator))
			fmt.Println("invalid file path")
		}

		// 如果是目录，则创建目录
		if file.FileInfo().IsDir() {
			fmt.Println("crearing directory...")
			if err = os.MkdirAll(filePath, os.ModePerm); err != nil {
				return err
			}
			continue
		}
		if err := os.MkdirAll(filepath.Dir(filePath), os.ModePerm); err != nil {
			panic(err)
		}

		dstFile, err := os.OpenFile(filePath, os.O_CREATE|os.O_RDWR|os.O_TRUNC, file.Mode())
		if err != nil {
			return err
		}

		// 获取到 Reader
		fileInArchive, err := file.Open()
		if err != nil {
			return err
		}

		_, err = io.Copy(dstFile, fileInArchive)
		if err != nil {
			panic(err)
		}

		dstFile.Close()
		fileInArchive.Close()
	}
	return nil
}

func exec_command_decode() error {
	var cmd *exec.Cmd
	fmt.Println(os.Getwd())
	sysType := runtime.GOOS
	if sysType == "windows" {
		cmd = exec.Command("cmd", "/c", "ping", "-t", "127.0.0.1")
	} else if sysType == "linux" {
		cmd = exec.Command("bash", "-c", "ping", "-t", "127.0.0.1")
	}
	// cmd := exec.Command("cmd", "/c", "echo", "'o'", ">", "abc.txt")
	fmt.Println(cmd.Args)
	stdout, err := cmd.StdoutPipe()
	stderr, errs := cmd.StderrPipe()
	if err != nil {
		return err
	}
	go func(err io.ReadCloser) {
		in := bufio.NewScanner(err)
		for in.Scan() {
			cmdRe := convertByte2String(in.Bytes(), "GB18030")
			panic(cmdRe)
		}
	}(stderr)
	if errs != nil {
		return err
	}

	err = cmd.Start()
	in := bufio.NewScanner(stdout)
	for in.Scan() {
		cmdRe := convertByte2String(in.Bytes(), "GB18030")
		fmt.Println(cmdRe)
	}
	cmd.Wait()
	cmd.Wait()
	return err
}

func convertByte2String(byte []byte, charset Charset) string {
	var str string
	switch charset {
	case GB18030:
		// var decodeBytes, _ = simplifieschinese.GB18030.NewDecoder().Bytes(byte)
		decodeBytes := string(byte)
		str = string(decodeBytes)
	case UTF8:
		fallthrough
	default:
		str = string(byte)
	}
	return str
}
