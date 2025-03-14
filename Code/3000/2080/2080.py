#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 区间内查询数字的频率 —— 超出时间限制。
时间复杂度：O(k log k)
空间复杂度：O(k)
执行用时：
消耗内存：
"""
import bisect
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)

    def query(self, left: int, right: int, value: int) -> int:
        list = self.arr[left:right + 1]
        # print(f"选取后的 list: {list}")
        if value not in list:
            # print(f"{value} not in list")
            return 0

        list.sort()
        # print(f"排序后的 list: {list}")
        left_index = bisect.bisect_left(list, value)
        # print(f"value 第一次出现的索引: {left_index}")
        right_index = bisect.bisect_right(list, value)
        # print(f"大于 value 的索引: {right_index}")
        if left_index == right_index:
            return 1
        else:
            return right_index - left_index


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)


if __name__ == '__main__':
    rangefreq1 = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    print(rangefreq1.query(1, 2, 4))
    print(rangefreq1.query(0, 11, 33))

    rangefreq2 = RangeFreqQuery([1, 1, 1, 2, 2])
    print(rangefreq2.query(0, 1, 2))
