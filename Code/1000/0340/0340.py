#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0340.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 至多包含 K 个不同字符的最长子串。
时间复杂度： O(N)
空间复杂度： O(K)
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        找出 至多 包含 k 个 不同 字符的最长子串
        :param s:
        :param k:
        :return: 返回该子串的长度
        """
        ans = left = 0
        window = []
        for right, char in enumerate(s):
            window.append(char)

            while len(set(window)) > k:
                window = window[1:]
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct(s="eceba", k=2))
