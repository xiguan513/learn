#!/bin/bash

#
#获取每个工程原始的git 远程地址
#直接通过变量替换内容的方法更好git远程地址
#
#
#
#

dir=/home/hptx/code/
for i in $(ls ${dir})
do
cd ${dir}${i}
i=$(git remote -v |grep push |awk '{print $2}')
b=${a/123/321}
i=${i/192.168.0.118/192.168.1.239/}
git remote set-url origin $i
git remote -v |grep push
done
