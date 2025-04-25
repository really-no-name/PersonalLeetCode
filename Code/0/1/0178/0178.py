#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0178.py
作者: Bolun Xu
创建日期: 2025/4/23
版本: 1.0
描述: 分数排名。
"""
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    result = scores.sort_values(by=['rank'])
    return result[['score', 'rank']]


if __name__ == '__main__':
    data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id': 'Int64', 'score': 'Float64'})
    print(order_scores(scores))