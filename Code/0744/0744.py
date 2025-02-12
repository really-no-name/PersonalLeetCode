#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 寻找比目标字母大的最小字母。
时间复杂度：O(LogN)
空间复杂度：O(1)
执行用时：0 ms
消耗内存： 18.77 mb
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 开区间
        left, right = -1, len(letters)
        while left + 1 < right:
            mid = (left + right) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid
            else:
                right = mid
        return letters[right] if right < len(letters) else letters[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
    print(solution.nextGreatestLetter(letters=["c", "f", "j"], target="d"))
    print(solution.nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))
