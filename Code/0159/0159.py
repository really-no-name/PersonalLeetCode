#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0159.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 至多包含两个不同字符的最长子串。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        找出 至多 包含 两个不同字符 的最长子串
        :param s:
        :return: 返回该子串的长度
        """
        ans = 0
        left = 0
        window = []
        for right, char in enumerate(s):
            window.append(char)

            while len(set(window)) > 2:
                window = window[1:]
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstringTwoDistinct(s="eceba"))
