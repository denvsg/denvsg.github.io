# golang 内置库 path

## 常用函数

1. func Base(path string) string // 返回路径的最后一个元素
2. func Clean(path string) string // 返回同目录的最短路径
3. func Dir(path string) string // 返回路径中目录部分
4. func Ext(path string) string // 返回路径中扩展部分
5. func IsAbs(path string) bool // 判断是否是一个绝对路径
6. func Join(elem ...string) string // 将多个字符串合并为一个路径
7. func Match(pattern, name string) (matched bool, err error) // 正则是否匹配路径（shell 文件名匹配）
8. func Split(path string) (dir, file string) // 将路径分割为路径和文件名

[path usage](https://pkg.go.dev/path)

# golang 内置库 path/filepath

## 常用函数

1. filepath.Separator // 预定义变量，表示路径分隔符 /
2. filepath.ListSeparator // 预定义变量，表示环境变量分隔符 :
3. func Abs(path string) (string, error) // 返回path 相对当前路径的绝对路径
4. func Base(path string) string // 返回路径的文件或目录名
5. func Clean(path string) string // 返回path 的最短路径
6. func Dir(path string) string  // 返回文件的路径
7. func EvalSymlinks(path string) (string, error) // 返回软链指向的路径
8. func FromSlash(path string) string // / 替换为路径分隔符
9. func IsAbs(path string) bool  // 检查路径是否是绝对路径
10. func Rel(basepath, targpath string) (string, error) // 返回targpath 相对 basepath路径
11. func VolumeName(path string) string // 返回路径最前面的卷名
12. func Split(path string) (dir, file string) // 拆分紧跟在最后一个分隔符之后的路径，将其分隔为目录和文件名组件。
13. func SplitList(path string) []string // 分隔环境变量里面的路径
14. func ToSlash(path string) string // 路径分隔符替换为 /
15. func Walk(root string, fn WalkFunc) error // 遍历 root 目录下的文件树，为树中的每个文件或目录（包括根目录）调用 fn
16. func WalkDir(root string, fn fs.WalkDirFunc) error // 同上，但效率比上高，避免了调用 os

[filepath usage](https://pkg.go.dev/path/filepath)