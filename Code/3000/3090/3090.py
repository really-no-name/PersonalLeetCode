#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3090.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 每个字符最多出现两次的最长子字符串。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, letter in enumerate(s):
            # 右侧字符加入窗口
            cnt[letter] += 1

            # 如果letter在哈希表次数大于2
            while cnt[letter] > 2:
                cnt[s[left]] -= 1  # left 移出窗口
                left += 1  # 左侧指针右移

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumLengthSubstring("bcbbbcba"))
