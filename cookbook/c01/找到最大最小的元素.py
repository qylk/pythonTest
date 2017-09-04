# -*- coding: utf-8 -*-
__author__ = 'qylk'

import heapq

nums = [1, 7, 9, 2, 5, 10, 25, 0, 4]
print max(nums)
print min(nums)
print heapq.nlargest(2, nums)  # 找出前2个最大值
print heapq.nsmallest(2, nums)  # 找出前2个最小值

sort = sorted(nums)  # 先整体排序
print sort[-3:]  # 再切片，最大的3个值

tmp = list(nums)
heapq.heapify(tmp)  # 堆里的第一个元素总是最小的元素
print tmp

sort = []  # 通过不断的pop,即可找出所有排完序的列表
while tmp:
    sort.append(heapq.heappop(tmp))
print sort
