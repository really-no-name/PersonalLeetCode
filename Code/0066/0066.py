#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 加一。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        a = 1
        for d in digits[::-1]:
            if a + d >= 10:
                ans.append(a + d - 10)
                a = 1
            else:
                ans.append(a + d)
                a = 0
        if a == 1:
            ans.append(a)
        return ans[::-1]



if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))


