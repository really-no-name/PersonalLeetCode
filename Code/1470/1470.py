#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 重新排列数组。
时间复杂度： O(N)
空间复杂度： O(N)
执行用时： 0 ms
消耗内存： 17.81 mb
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        ans = []
        for i in range(n):
            ans.append(x[i])
            ans.append(y[i])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))
