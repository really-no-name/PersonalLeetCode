#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2461.py
作者: Bolun Xu
创建日期: 2025/2/27
版本: 1.0
描述: 长度为 K 子数组中的最大和。
时间复杂度：
空间复杂度：
"""
from collections import Counter
from typing import List


# class Solution:
#     def maximumSubarraySum(self, nums: List[int], k: int) -> int:
#         ans = 0
#         window = []  # 当前窗口
#         s = 0  # 当前窗口的和
#         for i, num in enumerate(nums):
#             # 进入窗口
#             window.append(num)
#             s += num
#             # 窗口长度不足
#             if i < k - 1:
#                 continue
#             # 更新最大值
#             if len(set(window)) == len(window):  # 列表中是否所有元素各不相同
#                 # !!每次判断窗口中是否有重复元素时，都需要将列表转换为集合
#                 ans = max(ans, s)
#             # 离开窗口
#             window = window[1:]
#             s -= nums[i - k + 1]
#         return ans

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # 初始化最大子数组和为 0
        ans = 0

        # 使用 Counter 来记录当前窗口中每个元素的出现次数
        # 初始化 Counter，记录前 k-1 个元素的出现次数
        cnt = Counter(nums[:k - 1])

        # 初始化当前窗口的和，计算前 k-1 个元素的和
        s = sum(nums[:k - 1])

        # 使用滑动窗口的思想，遍历数组
        # in_ 是即将进入窗口的元素，out 是即将离开窗口的元素
        for in_, out in zip(nums[k - 1:], nums):
            # 将 in_ 加入窗口
            cnt[in_] += 1  # 更新 in_ 的计数
            s += in_  # 更新窗口的和

            # 如果当前窗口中的元素个数等于 k，说明窗口大小满足条件
            # 并且 cnt 的大小等于 k，说明窗口中的元素互不相同
            if len(cnt) == k:
                ans = max(ans, s)  # 更新最大子数组和

            # 将 out 移出窗口
            cnt[out] -= 1  # 更新 out 的计数
            if cnt[out] == 0:
                del cnt[out]  # 如果 out 的计数为 0，从 Counter 中移除，避免干扰 len(cnt) 的判断
            s -= out  # 更新窗口的和

        # 返回最大子数组和
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
