#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1234.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 替换子串得到平衡字符串。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        """
        :param s: 一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。s.length 是 4 的倍数 !!!
        :return: 待替换子串的最小可能长度
        在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」
        """
        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:  # 已经符合要求啦
            return 0
        left = 0
        ans = len(s)
        print(f"DEBUG: {cnt}")
        for right, char in enumerate(s):
            # 进入窗口
            cnt[char] -= 1
            print(f"DEBUG: {left}, {right}")
            print(f"DEBUG: {cnt}")

            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                print(f"DEBUG: {ans}")
                cnt[s[left]] += 1
                left += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.balancedString("QQWE"))