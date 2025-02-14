#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 两球之间的磁力 ———— 二分查找。
时间复杂度：O(NLogN)
空间复杂度：O(1)
执行用时：360 ms
消耗内存：29.95 mb
"""
from typing import List
from bisect import bisect_left
from math import inf


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 定义一个辅助函数，用于检查是否可以在最小间距为f的情况下放置m个球
        def check(f: int) -> bool:
            prev = -inf  # 上一个球的位置，初始化为负无穷
            cnt = 0  # 已放置的球的数量
            for curr in position:
                # 如果当前球的位置与上一个球的位置之间的距离大于等于f，则可以放置一个球
                if curr - prev >= f:
                    prev = curr  # 更新上一个球的位置
                    cnt += 1  # 增加已放置球的数量
            # 如果放置的球的数量小于m，说明f过大，需要减小f
            return cnt < m

        position.sort()  # 对位置进行排序，方便后续计算
        l, r = 1, position[-1]  # 初始化二分搜索的左右边界，最小间距为1，最大间距为最大位置值

        # 使用二分搜索找到最大的f，使得check(f)为True
        # bisect_left返回的是第一个使得check(f)为True的f的索引
        return bisect_left(range(l, r + 1), True, key=check)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistance([1, 2, 3, 4, 7], 3))
