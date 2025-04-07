#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2748.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 美丽下标对的数目。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
import math
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print(int(str(nums[i])[0]), int(str(nums[j])[-1]))
                if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBeautifulPairs([31,25,72,79,74]))