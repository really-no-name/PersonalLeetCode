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
        """
        使用滑动窗口方法来解决最长无重复字符子串问题。
        参数: s (str): 输入的字符串
        返回: int: 最长无重复字符子串的长度
        """
        # 用于存储当前窗口中的字符，确保窗口内字符不重复
        char_set = set()

        # 滑动窗口的左指针，表示当前窗口的起始位置
        left = 0

        # 记录最长子串的长度
        max_length = 0

        # 右指针遍历字符串
        for right in range(len(s)):
            print("----------------------------------------------------------------")
            # 调试信息：打印当前窗口的左右指针位置
            print(f"DEBUG: 当前窗口: left={left}, right={right}, 窗口内容: {s[left:right + 1]}")

            # 如果当前字符 s[right] 已经在 char_set 中，说明字符重复
            while s[right] in char_set:
                # 调试信息：打印移除字符的过程
                print(f"DEBUG: 字符 '{s[right]}' 重复，移除字符 '{s[left]}'")

                # 缩小窗口：从左指针开始移除字符，直到移除重复字符
                char_set.remove(s[left])
                left += 1  # 左指针右移

                # 调试信息：打印缩小后的窗口
                print(f"DEBUG: 缩小后的窗口: left={left}, right={right}, 窗口内容: {s[left:right + 1]}")

            # 将当前字符 s[right] 添加到 char_set 中
            char_set.add(s[right])

            # 调试信息：打印添加字符后的窗口
            print(f"DEBUG: 添加字符 '{s[right]}' 后的窗口: {char_set}")

            # 更新最大长度：当前窗口的长度为 right - left + 1
            max_length = max(max_length, right - left + 1)

            # 调试信息：打印当前的最大长度
            print(f"DEBUG: 当前最大长度: {max_length}")

        # 返回最终的最大长度
        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
