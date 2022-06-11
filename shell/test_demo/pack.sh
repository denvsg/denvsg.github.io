#!bash

set -x

if ! node -v &> /dev/null ;then
    echo -e "\e[31m 请配置node和npm环境变量 \e[0m"
    exit 9
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

if ! grep 'hvigor' package.json &> /dev/null ;then
    compile_cmd=' "scripts": {\n    "build": "hvigor clean assembleHap"\n  },'
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
page_path=${root_dir}${pages}
node_kit_path=${root_dir}${node_modules_path}
if [ ${status} -eq 0 ];then
    if find ${page_path} -name index.js ;then
        echo "pages compiler success"
    else
        echo -e "\e[31m pages compiler fail\e[0m"
    fi
    if find ${node_kit_path} -name "*.js" ;then
        echo "node_modules compiler success"
    else
        echo -e "\e[31m node_modules compiler fail\e[0m"
    fi
fi

sleep 2
exit 0
C:\Users\dsg\DevEcoStudioProjects\MyApplication        x
C:\\Users\\dsg\\DevEcoStudioProjects\\MyApplication    v