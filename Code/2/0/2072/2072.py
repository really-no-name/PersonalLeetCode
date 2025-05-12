#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2072.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 赢得比赛的大学。
"""
import pandas as pd


def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    NewYork_cnt = new_york[new_york['score'] >= 90].shape[0]
    California_cnt = california[california['score'] >= 90].shape[0]

    if NewYork_cnt > California_cnt:
        return pd.DataFrame({'winner': ['New York University']})
    elif California_cnt > NewYork_cnt:
        return pd.DataFrame({'winner': ['California University']})
    else:
        return pd.DataFrame({'winner': ['No Winner']})


if __name__ == "__main__":
    data = [[1, 90], [2, 87]]
    new_york = pd.DataFrame(data, columns=['student_id', 'score']).astype({'student_id': 'Int64', 'score': 'Int64'})
    data = [[2, 89], [3, 88]]
    california = pd.DataFrame(data, columns=['student_id', 'score']).astype({'student_id': 'Int64', 'score': 'Int64'})
    print(find_winner(new_york, california))