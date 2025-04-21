#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0541.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 反转字符串 II。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        char = ''
        while left < right:
            char = s[left]
            s[left] = s[right]
            s[right] = char

            left += 1
            right -= 1
        return s

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        rev = 1
        for i in range(0, len(s), k):
            if i + k > len(s) and rev == 1:
                print(s[i:])
                s[i:] = self.reverseString(s[i:])
                print('reverse:', s[i:])
            else:
                if rev == 1:
                    print(s[i:i + k])
                    s[i:i + k] = self.reverseString(s[i:i + k])
                    rev = -1
                    print('reverse:', s[i:i + k])
                else:
                    print(s[i:i + k])
                    rev = 1
        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr(s = "abcdefg", k = 2))