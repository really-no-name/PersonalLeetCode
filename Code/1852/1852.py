#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1852.py
作者: Bolun Xu
创建日期: 2025/2/28
版本: 1.0
描述: 每个子数组的数字种类数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List

from collections import defaultdict


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ans = []
        window_counts = defaultdict(int)  # 记录窗口中每个数字的出现次数
        distinct_count = 0  # 记录窗口中不同数字的数量

        for i, num in enumerate(nums):
            # 添加当前数字到窗口
            if window_counts[num] == 0:
                distinct_count += 1
            window_counts[num] += 1

            # 如果窗口大小达到k，开始滑动窗口
            if i < k - 1:
                continue

            ans.append(distinct_count)
            # 移除窗口最左边的数字
            left_num = nums[i - k + 1]
            window_counts[left_num] -= 1
            if window_counts[left_num] == 0:
                distinct_count -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.distinctNumbers(nums=[1, 2, 3, 2, 2, 1, 3], k=3))
