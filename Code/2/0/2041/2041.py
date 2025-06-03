#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2041.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 面试中被录取的候选人。
"""
import pandas as pd


def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    # 计算面试分数之和
    df_rounds = rounds.groupby('interview_id')['score'].sum().reset_index()

    # 合并
    df_merge = candidates.merge(df_rounds, on='interview_id', how='left').fillna(0)

    # 筛选
    df_filter = df_merge[(df_merge['years_of_exp'] >= 2) & (df_merge['score'] > 15)]

    return df_filter[['candidate_id']]


if __name__ == '__main__':
    data = [[11, 'Atticus', 1, 101], [9, 'Ruben', 6, 104], [6, 'Aliza', 10, 109], [8, 'Alfredo', 0, 107]]
    candidates = pd.DataFrame(data, columns=['candidate_id', 'name', 'years_of_exp', 'interview_id']).astype(
        {'candidate_id': 'Int64', 'name': 'object', 'years_of_exp': 'Int64', 'interview_id': 'Int64'})
    data = [[109, 3, 4], [101, 2, 8], [109, 4, 1], [107, 1, 3], [104, 3, 6], [109, 1, 4], [104, 4, 7], [104, 1, 2],
            [109, 2, 1], [104, 2, 7], [107, 2, 3], [101, 1, 8]]
    rounds = pd.DataFrame(data, columns=['interview_id', 'round_id', 'score']).astype(
        {'interview_id': 'Int64', 'round_id': 'Int64', 'score': 'Int64'})
    print(accepted_candidates(candidates, rounds))