#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
问题：
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
"""

from collections import deque

def search(lines,pattern,history=5):
    previous_lines=deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(li)

if __name__=="__main__":
    with open(r'31.log') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end="")
                print("+"*20)
            print(line,end="")
            print('-'*20)