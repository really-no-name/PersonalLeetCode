#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0076.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 最小覆盖子串。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        给一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
        如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
        """
        if len(t) > len(s):
            return ""
        # 统计 t 中每个字符的出现次数
        cnt = Counter(t)
        # 记录当前窗口中还需要的字符数量
        required = len(t)

        left = 0
        min_len = float('inf')
        min_window = ""

        # print(f"初始化: cnt = {cnt}, required = {required}")

        for right, char in enumerate(s):
            # print(f"\n右指针移动到 {right}, 当前字符: '{char}'")

            # 如果当前字符在 t 中，减少需要的字符数量
            if char in cnt:
                if cnt[char] > 0:
                    required -= 1
                cnt[char] -= 1
                # print(f"字符 '{char}' 在 t 中，更新 cnt = {cnt}, required = {required}")
            # else:
                # print(f"字符 '{char}' 不在 t 中，跳过")

            # 当窗口包含了 t 中的所有字符时，尝试缩小窗口
            while required == 0:
                # print(f"\n当前窗口 [{left}, {right}] 包含了 t 的所有字符")

                # 更新最小窗口
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                    # print(f"更新最小窗口: '{min_window}', 长度 = {min_len}")

                # 左指针右移，尝试缩小窗口
                left_char = s[left]
                if left_char in cnt:
                    cnt[left_char] += 1
                    if cnt[left_char] > 0:
                        required += 1
                    # print(
                        # f"左指针移动到 {left}, 字符 '{left_char}' 移出窗口，更新 cnt = {cnt}, required = {required}")
                left += 1

        # print(f"\n最终最小窗口: '{min_window}'")
        return min_window


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
