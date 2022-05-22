# golang 内置库 os

## 常用函数

1. func Getwd() (dir string, err error) // 获取当前目录
2. func Chdir(dir string) error // 修改工作目录为dir
3. func Chmod(name string, mode FileMode) error // 修改name文件或文件夹的权限（对应linux的chmod命令）
4. func Chown(name string, uid, gid int) error // 修改name文件或文件夹的用户和组（对应linux的chmod命令）
5. func Chtimes(name string, atime time.Time, mtime time.Time) error // 修改文件的访问时间
6. func Mkdir(name string, perm FileMode) error // 使用指定的权限和名称创建一个文件夹（对于linux的mkdir命令）
7. func MkdirAll(path string, perm FileMode) error // 使用指定的权限和名称创建一个文件夹，并自动创建父级目录（对于linux的mkdir -p目录）
8. func ReadFile(name string) ([]byte, error)  // 读取文件并返回文件内容 
9. func Remove(name string) error // 删除指定的文件夹或者目录 ,不能递归删除，只能删除一个空文件夹或一个文件（对应linux的 rm命令）
10. func RemoveAll(path string) error // 递归删除文件夹或者文件（对应linux的rm -rf命令）
11. func Rename(oldpath, newpath string) error // 修改一个文件或文件夹的文字（对应linux的mv命令）
12. func WriteFile(name string, data []byte, perm FileMode) error  //将数据写入命名文件，并在必要时创建该文件。如果该文件不存在，WriteFile将使用perm权限（在umask之前）创建它


[os usage](https://pkg.go.dev/os)