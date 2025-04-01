#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0410.py
作者: Bolun Xu
创建日期: 2025/4/1
版本: 1.0
描述: 分割数组的最大值。
时间复杂度： O(NLog(Sum(Nums)))
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(s: int) -> bool:
            cnt = 1
            x = 0
            for num in nums:
                if x + num <= s:
                    x += num
                    continue
                if cnt == k:
                    return False
                cnt += 1
                x = num
            return True

        left = max(nums) - 1
        right = sum(nums) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if check(mid):
                right = mid
            else:
                left = mid
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.splitArray(nums=[1,4,4], k=3))
