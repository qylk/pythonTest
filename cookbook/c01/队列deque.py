# -*- coding: utf-8 -*-
__author__ = 'qylk'

from collections import deque

deque = deque((1, 2, 3, 4, 5), 5)
deque.append(6)
deque.appendleft(0)
deque.pop()  # 移出
deque.popleft()

print deque
