#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3392.py
作者: Bolun Xu
创建日期: 2025/4/28
版本: 1.0
描述: 统计符合条件长度为 3 的子数组数目。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(2, len(nums)):
            if nums[i - 2] + nums[i] == nums[i - 1] * 0.5:
                print(nums[i - 2], nums[i - 1], nums[i])
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countSubarrays([1,2,1,4,1]))