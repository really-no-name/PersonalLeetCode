#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 无重复字符的最长子串。
时间复杂度：
空间复杂度：
执行用时：19 ms
消耗内存：17.75 mb
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用滑动窗口方法
        char_set = set()  # 用于存储当前窗口中的字符
        left = 0  # 滑动窗口的左指针
        max_length = 0  # 记录最长子串的长度

        for right in range(len(s)):  # 右指针遍历字符串
            while s[right] in char_set:  # 如果字符重复，则缩小窗口
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])  # 添加当前字符到集合中
            max_length = max(max_length, right - left + 1)  # 更新最长长度

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
