#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1285.py
作者: Bolun Xu
创建日期: 2025/5/22
版本: 1.0
描述: 找到连续区间的开始和结束数字。
"""
import pandas as pd


def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs.copy()

    # 计算每个log_id与其排名的差值
    df['rank'] = df['log_id'].rank(method='first')
    df['rank_diff'] = df['log_id'] - df['rank']

    # 根据rnk_diff分组，计算每组的最小和最大log_id
    df_result = df.groupby(['rank_diff']).agg(
        start_id=('log_id', 'min'),  # 连续区间的起始log_id
        end_id=('log_id', 'max'),  # 连续区间的结束log_id
    ).reset_index()

    df_result = df_result[['start_id', 'end_id']].sort_values('start_id')
    return df_result


if __name__ == '__main__':
    data = [[1], [2], [3], [7], [8], [10]]
    logs = pd.DataFrame(data, columns=['log_id']).astype({'log_id': 'Int64'})
    print(find_continuous_ranges(logs))