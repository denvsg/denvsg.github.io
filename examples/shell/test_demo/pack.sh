#!/bin/bash

# set -x
function version_gt() { test "$(echo "$@" | tr " " "\n" | sort -V | head -n 1)" != "$1"; }
if ! node -v &> /dev/null ;then
    echo -e "\e[31m 请配置node和npm环境变量 \e[0m"
    exit 9
else
    # node版本要求： v14.18.3以及以上版本
    node_version=`node -v`
    if version_gt ${node_version:1} 14.18.3; then
        echo " ${node_version:1} is greater than 14.18.3" &> /dev/null 
    else
        echo -e "\e[31m Please upgrade nodejs version\n\e[0m"
    fi
fi

read -p "请输入工程根目录名:" root_dir
echo "你输入的工程根目录是 ${root_dir}" 

if [ -d "${root_dir}" ];then
    cd ${root_dir}
    root_dir=${root_dir//'\'/'/'}
    ls
else
    echo "输入的路径不正确，windows路径分割符 '\' 请替换成 '\\\' 或 '/' "
    exit 0
fi

if [ ! -d node_modules ];then
    npm install
else
    echo "npm install 已执行，跳过" 
fi

echo "开始编译打包"

if ! grep 'hvigor clean' package.json &> /dev/null;then
    compile_cmd=' "scripts": {\n    "build": "hvigor clean assembleHap",\n    "clean": "hvigor clean"\n  },'
    sed -i "/version/ i\ ${compile_cmd}" package.json
fi

if hvigor -v &> /dev/null ;then
  hvigor clean assembleHap
else
  npm run build
  status=$?
fi


pages='/entry/build/default/intermediates/assets/default/ets/pages'
node_modules_path='/entry/build/default/intermediates/assets/default/node_modules'
page_compile_path=${root_dir}${pages}
node_modules_compile_path=${root_dir}${node_modules_path}
if [ ${status} -eq 0 ];then
    if find ${page_compile_path} -name index.js &> /dev/null;then
        echo -e "\033[32m Case ${root_dir##*/} pages compiler success\033[0m"
    else
        echo -e "\e[31m Case ${root_dir##*/} pages compiler fail\e[0m"
    fi
    if find ${node_modules_compile_path} -name "*.js" &> /dev/null;then
        echo -e "\033[32m Case ${root_dir##*/} node_modules compiler success\n\033[0m"
    else
        echo -e "\e[31m Case ${root_dir##*/} node_modules compiler fail\n\e[0m"
    fi
fi

echo "modify compile mode"
compile_mode='    "compileMode":"esmodule",'
if ! grep '^[[:blank:]]\+"compileMode"' entry/build-profile.json5 &> /dev/null;then
    sed -a "/buildOption/a ${compile_mode}" entry/build-profile.json5
    if [ $? -ne 0 ];then
        echo -e "\033[31m modify compile mode fail\n\033[0m"
    fi
else
    echo -e "compile mode has been modified."
fi

sleep 2
exit 0
C:\Users\dsg\DevEcoStudioProjects\MyApplication        x
C:\\Users\\dsg\\DevEcoStudioProjects\\MyApplication    v