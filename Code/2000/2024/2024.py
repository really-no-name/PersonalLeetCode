#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2024.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 考试的最大困扰度。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """

        :param answerKey: 其中 answerKey[i] 是第 i 个问题的正确结果
        :param k: 表示能进行以下操作的最多次数
        :return:
        """
        ans = 0
        left = 0
        cnt = Counter()
        for right, key in enumerate(answerKey):
            cnt[key] += 1

            while min(cnt['T'], cnt["F"]) > k:
                cnt[answerKey[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxConsecutiveAnswers(answerKey="TTFF", k=2))
    print(solution.maxConsecutiveAnswers(answerKey="TFFT", k=1))
    print(solution.maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
