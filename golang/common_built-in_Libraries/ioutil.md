# golang 内置库 io/ioutil 库

## io 常用函数

1. func Copy(dst Writer, src Reader) (written int64, err error) // 从 src 复制到 dst，直到在 src 上达到 EOF 或发生错误
2. func CopyBuffer(dst Writer, src Reader, buf []byte) (written int64, err error) // CopyBuffer 与 Copy 相同，只是它暂存提供的缓冲区（如果需要），而不是分配临时缓冲区。如果 buf 为 nil，则分配一个;否则，如果它的长度为零，CopyBuffer就会惊慌失措。  如果 src 实现 WriterTo 或 dst 实现 ReaderFrom，则不会使用 buf 来执行复制。
3. func ReadAll(r Reader) ([]byte, error) // ReadAll 从 r 读取，直到出现错误或 EOF，并返回它读取的数据。成功的调用返回 err == nil，而不是 err == EOF。由于 ReadAll 被定义为从 src 读取直到 EOF，因此它不会将读取中的 EOF 视为要报告的错误。
4. func WriteString(w Writer, s string) (n int, err error) // WriteString 将字符串 s 的内容写入 w，w 接受一段字节。如果 w 实现 StringWriter，则直接调用其 WriteString 方法。否则，w.Write 只调用一次。


[io usage](https://pkg.go.dev/io)

#  io/ioutil 库常用函数

1. func NopCloser(r io.Reader) io.ReadCloser // NopCloser 返回一个 ReadCloser，其中包含一个 no-op Close 方法，包装提供的 Reader r。   从Go 1.16开始，这个函数只调用io。NopCloser
2. func ReadAll(r io.Reader) ([]byte, error) // ReadAll 从 r 读取，直到出现错误或 EOF，并返回它读取的数据。成功的调用返回 err == nil，而不是 err == EOF。由于 ReadAll 被定义为从 src 读取直到 EOF，因此它不会将读取中的 EOF 视为要报告的错误。从Go 1.16开始，这个函数只调用io。
3. func ReadDir(dirname string) ([]os.FileInfo, error) // ReadDir 读取由 dirname 命名的目录，并返回 fs 列表。目录内容的文件信息，按文件名排序。如果读取目录时出错，ReadDir 不会随错误一起返回任何目录条目。  从Go 1.16开始，os.ReadDir 是一个更高效、更正确的选择：它返回 fs 列表。DirEntry 而不是 fs。FileInfo，在读取目录的过程中出现错误时，它会返回部分结果。
4. func ReadFile(filename string) ([]byte, error) // ReadFile 读取按文件名命名的文件并返回内容。成功的调用返回 err == nil，而不是 err == EOF。由于 ReadFile 读取整个文件，因此它不会将读取中的 EOF 视为要报告的错误。  从Go 1.16开始，这个函数只调用os。读取文件。
5. func TempDir(dir, prefix string) (name string, err error) // TempDir 在目录目录中创建一个新的临时目录。目录名称是通过采用模式并将随机字符串应用于末尾来生成的。如果模式包含“*”，则随机字符串将替换最后一个“*”。TempDir 返回新目录的名称。如果 dir 是空字符串，TempDir 将使用临时文件的默认目录（请参阅 os.TempDir）。同时调用 TempDir 的多个程序不会选择同一目录。调用方负责在不再需要时删除该目录。  从Go 1.17开始，这个函数只调用os。MkdirTemp.
6. func TempFile(dir, pattern string) (f *os.File, err error) //TempFile 在目录目录中创建一个新的临时文件，打开该文件进行读取和写入，并返回生成的 *os。文件。文件名是通过采用模式并在末尾添加一个随机字符串来生成的。如果模式包含“*”，则随机字符串将替换最后一个“*”。如果 dir 是空字符串，TempFile 将使用临时文件的默认目录（请参阅 os.TempDir）。同时调用 TempFile 的多个程序不会选择同一个文件。调用方可以使用 f.Name（） 查找文件的路径名。调用方有责任在不再需要时删除该文件。  从Go 1.17开始，这个函数只调用os。创建Temp.
7. func WriteFile(filename string, data []byte, perm os.FileMode) error // WriteFile 将数据写入按文件名命名的文件。如果该文件不存在，WriteFile将使用perm权限（在umask之前）创建它;否则，WriteFile 会在写入之前截断它，而不更改权限。  从Go 1.16开始，这个函数只调用os。写入文件。





[io/ioutil usage](https://pkg.go.dev/io/ioutil)