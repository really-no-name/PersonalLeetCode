#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2962.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0
描述: 统计最大元素出现至少 K 次的子数组。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        if nums.count(max_num) < k:
            return 0

        left, ans = 0, 0
        cnt_max = 0
        for right, num in enumerate(nums):
            if num == max_num:
                cnt_max += 1
            while cnt_max == k:
                if nums[left] == max_num:
                    cnt_max -= 1
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
