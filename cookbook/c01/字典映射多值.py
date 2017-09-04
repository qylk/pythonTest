# -*- coding: utf-8 -*-
__author__ = 'qylk'
from collections import defaultdict

# defaultdict的好处在于免去了初始化的操作，直管append或者add，比如dict_list['c']不存在时，则需要创建一个空列表

dict = {'a': [1, 2, 3], 'b': [4, 5]}
dict_list = defaultdict(list)  # list作为factory，保持顺序
dict_list['c'].append(1)
dict_list['d'].append(2)
print dict_list

dict_set = defaultdict(set)  # set作为factory，不保持顺序
dict_set['c'].add(1)
dict_set['c'].add(5)
dict_set['c'].add(2)
print dict_set
