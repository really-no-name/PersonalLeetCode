#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2287.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 重排字符形成目标字符串。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(target)
        ans = float('inf')  # 初始化为无穷大，确保第一次 min 能正确更新
        for k in cnt_t:
            if k not in cnt_s:
                return 0  # 如果 target 的某个字符不在 s 中，直接返回 0
            ans = min(ans, cnt_s[k] // cnt_t[k])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.rearrangeCharacters(s = "ilovecodingonleetcode", target = "code"))