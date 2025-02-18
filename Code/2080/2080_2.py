#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 这个文件用于演示Python文件模板的常用结构。
时间复杂度： O(n + logk)
空间复杂度： O(n + 1)
执行用时： 174 ms
消耗内存： 57.94 mb
"""

import bisect
from typing import List

from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        """
        初始化函数，构建一个哈希表，记录每个值在数组中的所有出现位置。

        :param arr: 输入的整数数组
        """
        # 使用 defaultdict 来存储每个值对应的索引列表
        value_to_indices = defaultdict(list)

        # 遍历数组，记录每个值的所有出现位置
        for index, value in enumerate(arr):
            value_to_indices[value].append(index)

        # 将哈希表保存为类的属性
        self.value_to_indices = value_to_indices

    def query(self, left: int, right: int, value: int) -> int:
        """
        查询在区间 [left, right] 内，值等于 value 的元素个数。

        :param left: 区间的左边界
        :param right: 区间的右边界
        :param value: 要查询的值
        :return: 区间内值等于 value 的元素个数
        """
        # 获取值对应的所有索引列表
        indices = self.value_to_indices.get(value, [])

        # 使用 bisect_left 和 bisect_right 来查找在 [left, right] 范围内的元素个数
        left_bound = bisect_left(indices, left)
        right_bound = bisect_right(indices, right)

        # 调试信息：打印查询的中间结果
        # print(f"Debug: value={value}, indices={indices}, left_bound={left_bound}, right_bound={right_bound}")

        # 返回区间内的元素个数
        return right_bound - left_bound



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)


if __name__ == '__main__':
    rangefreq1 = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    print(rangefreq1.query(1, 2, 4))
    print(rangefreq1.query(0, 11, 33))

    rangefreq2 = RangeFreqQuery([1, 1, 1, 2, 2])
    print(rangefreq2.query(0, 1, 2))
