#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2026.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 低质量的问题。
"""
import pandas as pd


def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    # 计算 rate 列
    problems['rate'] = problems['likes'] / (problems['likes'] + problems['dislikes'])

    # 筛选 rate < 0.6 的行
    ans = problems[problems['rate'] < 0.6]

    # 提取 problem_id 列并排序，返回为 DataFrame
    result = ans[['problem_id']].sort_values(by='problem_id', ascending=True)

    return result


if __name__ == '__main__':
    problem = pd.DataFrame({
        'problem_id': [6, 11, 1, 7, 13, 10],
        'likes': [1290, 2677, 4446, 8569, 2050, 9002],
        'dislikes': [425, 8659, 2760, 6086, 4164, 7446]
    })
    print(low_quality_problems(problem))
