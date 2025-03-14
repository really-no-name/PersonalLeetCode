#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 大小为 K 且平均值大于等于阈值的子数组数目。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        ans = 0
        s = 0
        for i, a in enumerate(arr):
            # 第 i 项 a 进入窗口
            s += a
            # 窗口长度不足
            if i < k - 1:
                continue
            # 更新答案
            if s >= threshold:
                ans += 1
            # 第 i - k + 1 项离开窗口
            s -= arr[i - k + 1]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
