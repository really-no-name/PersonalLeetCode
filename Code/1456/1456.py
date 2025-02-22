#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 定长子串中元音的最大数目。
时间复杂度： O(N)
空间复杂度： O(1)
执行用时： 99 ms
消耗内存： 17.94 mb
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0  # 答案
        vow = 0  # 当前滑窗内的元音数
        for i, c in enumerate(s):
            # 进入窗口
            # print(f"DEBUG: ----------------------------------------")
            # print(f"DEBUG: s[{i}]= {c} 进入窗口")
            if c in "aeiou":
                # print(f"DEBUG: s[{i}]= {c} 是元音")
                vow += 1
            if i < k - 1:
                # print(f"DEBUG: 滑窗长度不满足")
                continue
            # 更新答案
            # print(f"DEBUG: 当前滑窗内元音数为 {vow}")
            ans = max(ans, vow)
            # 离开窗口
            # print(f"DEBUG: s[{i - k + 1}]= {s[i - k + 1]} 离开窗口")
            if s[i - k + 1] in "aeiou":
                # print(f"DEBUG: s[{i - k + 1}]= {s[i - k + 1]} 是元音")
                vow -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxVowels(s="abciiidef", k=3))
