#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0574.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 当选者。
"""
import pandas as pd


def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    """
    报告获胜候选人的名字(即获得最多选票的候选人)
    """
    vote = vote.groupby('candidateId')['id'].nunique().reset_index()
    max_vote = vote[vote['id'] == vote['id'].max()]['candidateId']
    candidate_filter = candidate[candidate['id'].isin(max_vote)]
    return candidate_filter[['name']]


if __name__ == '__main__':
    data = [[1, 'A'], [2, 'B'], [3, 'C'], [4, 'D'], [5, 'E']]
    candidate = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 2], [2, 4], [3, 3], [4, 2], [5, 5]]
    vote = pd.DataFrame(data, columns=['id', 'candidateId']).astype({'id': 'Int64', 'candidateId': 'Int64'})
    print(winning_candidate(candidate, vote))
