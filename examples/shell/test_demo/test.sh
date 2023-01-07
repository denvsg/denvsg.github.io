#!/bin/bash

set -x

#hvigor -v &> /dev/null
#if ! hvigor -v ;then
#  hvigor clean assembleHap
#else
#  npm run build
#fi
#
#
#hvigor -v &> /dev/null
#if [ $? -eq 0 ];then
#  hvigor clean assembleHap
#else
#  npm run build
#fi

str='987-123-4567
123 456 7890
(001) 345-00001
(001)-345-0000
(123) 456-7890'
echo -e "$str" | grep '^\(([0-9]\{3\}) \|[0-9]\{3\}-\)[0-9]\{3\}-[0-9]\{4\}$'