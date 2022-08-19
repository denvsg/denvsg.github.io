#!/bin/bash
# 字符串比较时，请对变量使用引号包裹，可以避免不必要的麻烦。
# 字符串信息获取, 如: 字符串长度、字符串切片、字符串截取等。

# 1. 字符串输出
str='string'
echo $str
echo ${str} # 注意: 加括号是为了与其他字符串区分，如果单独的变量也可不加括号.
echo '1.========================================================================'
unset str


# 2. 字符串变量设置默认值
str="This is a string."
echo "'${str:-default}'" # 如果变量未声明, 就使用 'default' 作为变量的值.
echo "'${strs:-default}'" # 如果变量未声明, 就使用 'default' 作为变量的值. 默认值临时使用，之后不继承.
echo "'${strss-default}'" # 如果变量未声明, 就使用 'default' 作为变量的值. 默认值临时使用，之后不继承.
echo "str='${str}', strs='${strs}', strss='${strss}'"
echo '------------------------------------------------------------------------'
unset str

str="This is a string."
echo "'${str:=default}'" # 如果变量未声明, 就使用 'default' 作为变量的值.
echo "'${strs:=default}'" # 如果变量未声明, 就使用 'default' 作为变量的值.默认值永久使用，除非删除变量.
echo "'${strs1=default}'" # 如果变量未声明, 就使用 'default' 作为变量的值.默认值永久使用，除非删除变量.
echo "str='${str}', strs='${strs}', strs1='${strs1}'"
echo 2.'========================================================================'
unset str


# 3. 判断变量是否声明
str="This is test strings."
echo "str=${str+'declared'}" # 如变量已声明, 字符串的值即是加号后的字符串.
echo "str=${str:+'declared'}"  # 其中的冒号也可要可不要, 但编写脚本还是推荐写上.
echo "str1=${str+'not declared'}"
echo '3.========================================================================'
unset str; unset str1


# 4. 变量未声明打印警告
str="This is test strings."
echo -e "\e[32m str=${str?'not declared'} \e[0m" # 如变量未声明, 字符串的值即是问号后的字符串.
#echo "undeclared=${undeclared:?'not declared'}"  # 其中的冒号也可要可不要, 但编写脚本还是推荐写上.
#echo "undeclared=${undeclared?'not declared'}"
echo '4.========================================================================'
unset str


# 5. 搜索变量已声明的变量
str="This is test strings."
echo "之前所有以 'st' 开头的变量有: '${!st*}'" # 搜索之前所有以 'st' 开头的变量
echo "之前所有以 'u' 开头的变量有: '${!u@}'"  # 搜索之前所有以 'st' 开头的变量
echo '5.========================================================================'
unset str


# 6. 获取字符串长度
str="this is test statements."
length=${#str}
echo "'${str}' 的长度是 '${length}'."
echo '6.========================================================================'
unset str

# 7. 截取字符串 格式: {变量:起始:长度}
val="This is Test statements."
intercept1=${val:5:12} # 从第5个索引开始截取12个字符
echo "从'${val}' 截取{5:12}的字符串是 '${intercept1}', 长度是 ${#intercept1}. "
echo '------------------------------------------------------------------------'

intercept2=${val:5} # 从第5个索引开始截取, 没有长度一直到字符串结尾.
echo "从'${val}' 截取{5}的字符串是 '${intercept2}', 长度是 ${#intercept2}. "
echo '7.========================================================================'
unset str


# 8. 字符串删除
str="This is test strings."
# {变量#regex} 从开头开始匹配字符串进行删除
echo "${str#T}" # 注意此行和下一行的区别, 井号后实际是正则表达式.
echo "${str#*t}" # 注意此行和下一行的区别, 两个井号表示贪婪模式,即尽可能多的匹配.
echo "${str##*t}" #
echo '------------------------------------------------------------------------'

# {变量%regex} 从结尾开始匹配字符串进行删除
echo "${str%s.}" # 注意此行和下一行的区别, 井号后实际是正则表达式.
echo "${str%s*}" # 注意此行和下一行的区别, 两个井号表示贪婪模式,即尽可能多的匹配.
echo "${str%%s*}" #
echo '8.========================================================================'
unset str


# 9. 字符串修改替换
str="This is test strings."
echo "${str} 把第一个 s 替换为 M：'${str/s/M}'"
echo "${str} 把所有 s 替换为 M：'${str//s/M}'"
echo '------------------------------------------------------------------------'

val="This/is/test/strings."
echo "${val} 把第一个 / 替换为 @：'${val/\//@}'"
echo "${val} 把所有 / 替换为 @：'${val//\//@}'"
echo '9.========================================================================'
unset str


# 10. 字符串转换成数组
# 1. array=(`echo string | tr ',' ' '`)
# 2. array=(${string//,/ })
# 3. array=(`echo $string|sed 's/,/ /g'`)

str="This is test strings."
arr=(${str//e/ })
echo ${arr[@]}
str="The first thing we might need to do is to open the archive we want to decompress."
old_lfs=$IFS
IFS='o'
arr1=(${str// / })
echo ${arr1[@]}
echo '10.========================================================================'