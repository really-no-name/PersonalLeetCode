#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2070.py
作者: Bolun Xu
创建日期: 2025/3/4
版本: 1.0
描述: 每一个查询的最大美丽值 -- 二分查找。
时间复杂度： O(Nlogn+Mlogn)
空间复杂度： O(1)
"""
import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
        对于每个查询 queries[j] ，你想求出价格小于等于 queries[j] 的物品中，最大的美丽值 是多少。如果不存在符合条件的物品，那么查询的结果为 0 。
        :param items: 二维整数数组，其中 items[i] = [pricei, beautyi] 分别表示每一个物品的 价格 和 美丽值 。
        :param queries: 一个下标从 0 开始的整数数组 queries
        :return: 返回一个长度与 queries 相同的数组 answer，其中 answer[j]是第 j 个查询的答案。
        """
        ans = [0] * len(queries)
        items.sort(key=lambda x: x[0])
        # print(f"DEBUG: {items}")
        for i in range(1, len(items)):
            items[i][1] = max(items[i - 1][1], items[i][1])
        # print(f"DEBUG: {items}")

        for i, query in enumerate(queries):
            # print(f"DEBUG: {query}")
            j = bisect.bisect_right(items, query, key=lambda item: item[0])
            ans[i] = items[j - 1][1] if j else 0
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumBeauty(items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]))
