# -*- coding: utf-8 -*-
__author__ = 'qylk'

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 用一个元组包装item，主要为了排序，先按priority排，再按index排，保证不会出现位置一样的
        # heap默认是从小到大排列，这里priority取负则从大到小排列
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # heappop总是返回最小的元素

    def __str__(self):
        return str(self._queue)


if __name__ == '__main__':
    queue = PriorityQueue()
    queue.push('tom', 1)
    queue.push('tim', 10)
    queue.push('java', 2)
    queue.push('php', 2)
    print queue  # [(-10, 1, 'tim'), (-2, 3, 'php'), (-2, 2, 'java'), (-1, 0, 'tom')]
    print queue.pop()
