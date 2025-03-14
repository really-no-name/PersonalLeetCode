#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3305.py
作者: Bolun Xu
创建日期: 2025/3/12
版本: 1.0
描述: 元音辅音字符串计数 I。
时间复杂度： O(N ^ 2 )
空间复杂度： O(1)
"""


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        count = 0

        for left in range(n):
            vowel_count = 0
            consonant_count = 0
            seen_vowels = set()

            for right in range(left, n):
                char = word[right]
                if char in vowels:
                    seen_vowels.add(char)
                    vowel_count += 1
                else:
                    consonant_count += 1

                # 如果辅音字母数量超过k，直接跳出循环
                if consonant_count > k:
                    break

                # 如果满足条件：包含所有元音字母且辅音字母数量恰好为k
                if len(seen_vowels) == len(vowels) and consonant_count == k:
                    count += 1

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countOfSubstrings(word="aeioqq", k=1))
