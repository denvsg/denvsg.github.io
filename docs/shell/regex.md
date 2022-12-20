# 正则表达式

* linux awk  默认使用 ERE,  
* linux grep 默认使用 BRE, 可以通过 egrep或 grep -E 使用ERE  
* linux sed  默认使用 BRE的一个子集  

| 符号      | 解释              | 基本正则         | 拓展正则    | python正则 | perl正则  | 示例          |
|---------|-----------------|--------------|---------|----------|---------|-------------|
| \       | 转义符             | \            | \       | \        | \       | a\.b        | 
| ^       | 匹配行首            | ^            | ^       | ^        | ^       | ^hello      |
| $       | 匹配行为            | $            | $       | $        | $       | world$      |
| .       | 匹配任意一个字符        | .            | .       | .        | .       | he.         |       
| []      | 匹配[]中一个字符       | []           | []      | []       | []      | [abc]       |    
| [^]     | 匹配[]外一个字符       | [^]          | [^]     | [^]      | [^]     | [^0-9]      |
| [-]     | 匹配[]范围的一个字符     | [-]          | [-]     | [-]      | [-]     | [0-9]       |
| *       | 匹配前面的0次或多次      | *            | *       | *        | *       | hel*o       |
| ?       | 匹配前面的0次或1次      | 不支持,`\?`     | ?       | ?        | ?       | woo?rld     |
| +       | 匹配前面的1次或多次      | 不支持,`\+`     | +       | +        | +       | he+         |
| ()      | 匹配()字串          | 不支持,`\(\)`   | ()      | ()       | ()      | ma(tri)?x   |
| `{n}`   | 匹配前面的n次         | 不支持,`\{\}`   | `{n}`   | `{n}`    | `{n}`   |             |
| `{m,}`  | 匹配前面的至少m次       | 不支持          | `{m,}`  | `{m,}`   | `{m,}`  |             | 
| `{m,n}` | 匹配前面的m-n次       | 不支持          | `{m,n}` | `{m,n}`  | `{m,n}` |             |   
| &#124;  | 匹配&#124;左右的任意一项 | 不支持,\\&#124; | &#124;  | &#124;   | &#124;  | (a&#124;b)c |         
|         |                 |              |         |          |         |          



### POSIX 字符类(基础正则,拓展正则, python正则,perl正则均支持)

| 符号         | 解释            | 示例            |
|------------|---------------|---------------|
| [:alnum:]  | 匹配任意一个字母或数字   | [\[:alnum:]]  | 
| [:alpha:]  | 匹配任意一个字母      | [\[:alpha:]]  | 
| [:blank:]  | 匹配空格或制表符      | [\[:blank:]]  |
| [:digit:]  | 匹配任意一个数字      | [\[:digit:]]  |
| [:lower:]  | 匹配任意一个小写字母    | [\[:lower:]]  |
| [:upper:]  | 匹配任意一个大写字母    | [\[:upper:]]  |
| [:punct:]  | 匹配标点符号        | [\[:punct:]]  |
| [:space:]  | 匹配一个换行回车等空白字符 | [\[:space:]]  |
| [:graph:]  | 匹配一个看得见可打印的字符 | [\[:graph:]]  |
| [:cntrl:]  | 匹配一个控制字符      | [\[:cntrl:]]  
| [:print:]  | 匹配一个可打印的字符    | [\[:print:]]  
| [:xdigit:] | 匹配一个16进制数     | [\[:xdigit:]] |



### 元字符(基础正则,拓展正则少量支持; python正则,perl正则完全支持)

基础正则,拓展正则支持：

+ \b 单词边界
+ \B 非单词边界
+ \w 单个单词字符
+ \W 单个非单词字符 

python正则,perl正则完全

| 符号  | 解释              | 示例  |
|-----|-----------------|-----|
| \b  | 单词边界            |     |
| \B  | 非单词边界           |     |
| \d  | 一个数字字符          |     |
| \D  | 一个非数字字符         |     |
| \w  | 一个单词字符(字母数字下划线) |     |
| \W  | 一个非单词字符         |     |
| \n  | 换行符             |     |
| \s  | 一个空白字符          |     |
| \S  | 一个非空白字符         |     |
| \r  | 回车              |     |
| \t  | 横向制表符           |     |
| \v  | 纵向制表符           |     |
| \f  | 换页符             |     |
