#!/bin/bash
# 字符串比较时，请对变量使用引号包裹，可以避免不必要的麻烦。

str="this is test statements."
val="This is Test statements."

# 1.使用两个字符串直接比较  实质上是比较两个字符串的编码[ascii]顺序
if [ "${str}" = "${val}" ]; then
  echo "<${str}> IS THE SAME AS <${val}>"
elif [ "${str}" \< "${val}" ]; then
  echo "<${str}> IS LITTLE THAN <${val}>"
elif [ "${str}" \> "${val}" ]; then
  echo "<${str}> IS GATHER THAN <${val}>"
fi

# 2.字符串空值比较
str1="hello"
str2="     "
str3=''
if [ -n "$str1" ]; then
  echo "'$str1' is not null"
else
  echo "'$str1' is null"
fi

if [ -n "$str2" ]; then
  echo "'$str2' is not null"
else
  echo "'$str2' is null"
fi

if [ -n "$str3" ]; then
  echo "'$str3' is not null"
else
  echo "'$str3' is null"
fi

# 3.字符串全比较
if [[ ${str} == "${val}" ]]; then
  echo "<${str}> IS THE SAME AS <${val}>"
else
  echo "<${str}> IS THE DIFFERENT AS <${val}>"
fi

# same as next:
[[ ${str} == "${val}" ]] && echo "<${str}> IS THE SAME AS <${val}>" || echo "<${str}> IS THE DIFFERENT AS <${val}>"

declare -l val=$val # 将变量字符串声明为小写,  -u[upper] 字符串声明为大写
[[ ${str} == "${val}" ]] && echo "<${str}> IS THE SAME AS <${val}>" || echo "<${str}> IS THE DIFFERENT AS <${val}>"

# 4.字符串全比较
str_tmp="this is test ??????????."
if [[ "${str}" == ${str_tmp} ]]; then # 注意: 等号右边变量加引号和不加引号的区别
  echo "<${str}> IS TEMPLATE OF <${str_tmp}>"
else
  echo "<${str}> IS NOT TEMPLATE OF <${str_tmp}>"
fi

# 5.带正则的匹配
str="this is test statements."
if [[ ${str} =~ ^this.* ]]; then
  echo "<${str}> IS START　WITH　'this'"
else
  echo "<${str}> IS NOT START　WITH　'this'"
fi

# 6. 模式匹配比较
str="this is test statements."
val="This is Test statements."
if [[ $str == t?* ]];then
  echo "$str start with 't'"
elif [[ $str == t* ]];then
  echo "$str not contain 't'"
fi