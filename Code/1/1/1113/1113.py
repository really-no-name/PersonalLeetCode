#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1113.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0
描述: 报告的记录。
"""
import pandas as pd


def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    df_filt = actions[(actions['action_date'] == '2019-07-04') & (actions['action'] == 'report')]
    df_grp = df_filt.groupby('extra')['post_id'].nunique().reset_index()
    df_grp = df_grp.rename(columns={'extra': 'report_reason', 'post_id': 'report_count'})
    return df_grp


if __name__ == '__main__':
    data = [[1, 1, '2019-07-01', 'view', None],
            [1, 1, '2019-07-01', 'like', None],
            [1, 1, '2019-07-01', 'share', None],
            [2, 4, '2019-07-04', 'view', None],
            [2, 4, '2019-07-04', 'report', 'spam'],
            [3, 4, '2019-07-04', 'view', None],
            [3, 4, '2019-07-04', 'report', 'spam'],
            [4, 3, '2019-07-02', 'view', None],
            [4, 3, '2019-07-02', 'report', 'spam'],
            [5, 2, '2019-07-04', 'view', None],
            [5, 2, '2019-07-04', 'report', 'racism'],
            [5, 5, '2019-07-04', 'view', None],
            [5, 5, '2019-07-04', 'report', 'racism']]
    actions = pd.DataFrame(data, columns=['user_id', 'post_id', 'action_date', 'action', 'extra']).astype(
        {'user_id': 'Int64', 'post_id': 'Int64', 'action_date': 'datetime64[ns]', 'action': 'object',
         'extra': 'object'})
    print(reported_posts(actions))