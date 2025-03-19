#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0992.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0 -- 恰好型滑动窗口
描述: K 个不同整数的子数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import defaultdict
from typing import List


class Solution:
    def haha(self, nums: List[int], k: int) -> int:
        """
        某个子数组中不同整数的个数 小于等于 k
        """
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1

            while len(cnt) > k:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        如果 nums 的某个子数组中不同整数的个数恰好为 k，则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。
        返回 nums 中 「好子数组」 的数目。
        """
        if k > len(set(nums)):
            return 0
        upper = self.haha(nums, k)
        lower = self.haha(nums, k - 1)
        return - upper + lower


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
    print(sol.subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
