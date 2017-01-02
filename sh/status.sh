#!/bin/bash

for i in $(ls /home/hptx/code)
do
	cd /home/hptx/code
	echo -e "\033[31m $i \033[0m"
	cd $i
	/usr/bin/git branch
	#/usr/bin/git status
	echo -e "\033[32m ##############Last Log################## \033[0m"
	git log | head -4
	echo -e "\033[32m =============Last Log=================== \033[0m"
	/usr/bin/git status |grep 'origin/deploy'
done
