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
        ans = []  # 用于存储每个窗口的不同数字数量
        window_counts = defaultdict(int)  # 记录窗口中每个数字的出现次数
        distinct_count = 0  # 记录窗口中不同数字的数量

        for i, num in enumerate(nums):
            print(f"处理第 {i} 个元素: {num}")

            # 添加当前数字到窗口
            if window_counts[num] == 0:
                distinct_count += 1  # 如果这个数字之前没有出现过，增加不同数字的数量
                print(f"数字 {num} 第一次出现，当前不同数字数量: {distinct_count}")
            window_counts[num] += 1  # 更新当前数字的出现次数
            print(f"数字 {num} 的出现次数增加到: {window_counts[num]}")

            # 如果窗口大小达到k，开始滑动窗口
            if i < k - 1:
                print(f"窗口大小未达到 {k}，继续添加元素")
                continue

            # 窗口大小达到k，记录当前窗口的不同数字数量
            ans.append(distinct_count)
            print(f"窗口大小达到 {k}，当前窗口的不同数字数量: {distinct_count}")

            # 移除窗口最左边的数字
            left_num = nums[i - k + 1]
            window_counts[left_num] -= 1  # 减少最左边数字的出现次数
            print(f"移除窗口最左边的数字: {left_num}，其出现次数减少到: {window_counts[left_num]}")

            if window_counts[left_num] == 0:
                distinct_count -= 1  # 如果最左边数字的出现次数变为0，减少不同数字的数量
                print(f"数字 {left_num} 的出现次数变为0，当前不同数字数量: {distinct_count}")

        print("最终结果:", ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.distinctNumbers(nums=[1, 2, 3, 2, 2, 1, 3], k=3))
