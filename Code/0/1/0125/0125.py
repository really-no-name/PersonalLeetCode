#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0125.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 验证回文串。
时间复杂度： O(N)
空间复杂度： O(N)
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # print(f"DEBUG: {s}")
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
