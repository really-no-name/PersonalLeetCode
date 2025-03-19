#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3306.py
作者: Bolun Xu
创建日期: 2025/3/13
版本: 1.0 -- 恰好型滑动窗口
描述: 元音辅音字符串计数 II。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import defaultdict


class Solution:
    def haha(self, word: str, k: int) -> int:
        cnt1 = defaultdict(int)  # 统计原因字母
        ans = 0
        left = 0
        cnt2 = 0  # 统计辅音字母
        for right, letter in enumerate(word):
            if letter in 'aeiou':
                cnt1[letter] += 1
            else:
                cnt2 += 1

            while len(cnt1) == 5 and cnt2 >= k:
                if word[left] in 'aeiou':
                    cnt1[word[left]] -= 1
                    if cnt1[word[left]] == 0:
                        del cnt1[word[left]]
                else:
                    cnt2 -= 1
                left += 1

            ans += left

        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.haha(word, k) - self.haha(word, k + 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countOfSubstrings(word="aeioqq", k=1))
