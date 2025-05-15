#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1435.py
作者: Bolun Xu
创建日期: 2025/5/15
版本: 1.0
描述: 制作会话柱状图。
"""
import pandas as pd


def time_bin(d):
    if d / 60 < 5:
        return '[0-5>'
    elif d / 60 < 10:
        return '[5-10>'
    elif d / 60 < 15:
        return '[10-15>'
    else:
        return '15 or more'


def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    sessions['bin'] = sessions['duration'].apply(time_bin)  # 计算时长区间
    df_grp = sessions.groupby('bin')['session_id'].count().reset_index()  # 分组计数
    df_merge = (pd.DataFrame([['[0-5>'], ['[5-10>'], ['[10-15>'], ['15 or more']], columns=['bin'])
                .merge(df_grp, on='bin', how='left')).fillna(0)
    df_merge = df_merge.rename(columns={'session_id': 'total'})
    return df_merge


if __name__ == '__main__':
    data = [[1, 30], [2, 199], [3, 299], [4, 580], [5, 1000]]
    sessions = pd.DataFrame(data, columns=['session_id', 'duration']).astype(
        {'session_id': 'Int64', 'duration': 'Int64'})
    print(create_bar_chart(sessions))
