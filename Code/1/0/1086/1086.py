#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1086.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 前五科的均分。
时间复杂度： O(NLogN)
空间复杂度： O(N)
"""
from collections import defaultdict
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Step 1: 分组
        student_scores = defaultdict(list)
        for student_id, score in items:
            student_scores[student_id].append(score)
        print(student_scores)

        result = []

        # Step 2: 按学生ID递增顺序处理
        for student_id in sorted(student_scores.keys()):
            print(student_id)
            scores = sorted(student_scores[student_id], reverse=True)  # 降序排序
            print(scores)
            top_five = scores[:5]  # 取前五科
            print(top_five)
            average = sum(top_five) // 5  # 计算平均分（整数除法）
            result.append([student_id, average])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.highFive(
        [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
    print(solution.highFive(
        [[5, 91], [5, 92], [3, 93], [3, 97], [5, 60], [3, 77], [5, 65], [5, 87], [5, 100], [3, 100], [3, 76]]))
