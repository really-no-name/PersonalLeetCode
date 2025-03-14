#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 比较字符串最小字母出现频次。
时间复杂度：
空间复杂度：
执行用时：
消耗内存：
"""
from typing import List
from collections import Counter

from typing import List
from collections import Counter
from bisect import bisect_right
from string import ascii_lowercase


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 定义一个函数 f，用于计算字符串 s 的“最小字母频率”
        def f(s: str) -> int:
            # 使用 Counter 统计字符串中每个字符的出现次数
            cnt = Counter(s)
            # 遍历 ascii_lowercase（即所有小写字母），找到第一个在 cnt 中存在的字母，并返回其频率
            return next(cnt[c] for c in ascii_lowercase if c in cnt)

        # 计算 words 中每个单词的“最小字母频率”，并排序
        word_frequencies = sorted(f(w) for w in words)
        n = len(word_frequencies)  # words 的长度

        # 对于每个查询，计算其“最小字母频率”，并找到在 word_frequencies 中大于该频率的单词数量
        result = [n - bisect_right(word_frequencies, f(q)) for q in queries]
        return result


if __name__ == '__main__':
    sol = Solution()
    queries = ["dcb"]
    words = ["zaaaz"]
    print(sol.numSmallerByFrequency(queries, words))
