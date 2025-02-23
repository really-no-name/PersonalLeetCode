#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 回文排列。
时间复杂度： O(N)
空间复杂度： O(N)

"""
import math


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 统计每个字符的出现次数
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # 统计出现次数为奇数的字符个数
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1

        # 如果奇数个数的字符超过1个，则不能构成回文串
        return odd_count <= 1


if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("as"))
    print(s.canPermutePalindrome("carerac"))
