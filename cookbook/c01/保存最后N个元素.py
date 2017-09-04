# -*- coding: utf-8 -*-
from collections import deque


def search(file, pattern, max_history=5):
    queue = deque(maxlen=max_history)
    for line in file:
        if pattern in line:
            yield line, queue  # 生成器
        queue.append(line)


with open("../../pythonTest.iml") as f:
    for line, queue in search(f, 'true', 5):
        for pline in queue:  # 打印queue
            print pline
        print line  # 打印匹配行
        print '_' * 20  # 打印分隔符
