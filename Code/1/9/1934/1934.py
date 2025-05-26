#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1934.py
作者: Bolun Xu
创建日期: 2025/5/23
版本: 1.0
描述: 确认率。
"""
import pandas as pd


def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df_cnt1 = confirmations[confirmations['action'] == 'confirmed'].groupby('user_id')['time_stamp'] \
        .count().reset_index(name='confirm_cnt')
    df_cnt2 = confirmations.groupby('user_id')['time_stamp'].count().reset_index(name='total_cnt')

    df_merge = signups.merge(df_cnt1, on='user_id', how='left') \
        .merge(df_cnt2, on='user_id', how='left') \
        .fillna(0)

    df_merge['confirmation_rate'] = round(df_merge['confirm_cnt'] / df_merge['total_cnt'], 2)

    df_result = df_merge[['user_id', 'confirmation_rate']].fillna(0)
    return df_result


if __name__ == '__main__':
    data = [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'],
            [6, '2020-12-09 10:39:37']]
    signups = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
    data = [[3, '2021-01-06 03:30:46', 'timeout'], [3, '2021-07-14 14:00:00', 'timeout'],
            [7, '2021-06-12 11:57:29', 'confirmed'], [7, '2021-06-13 12:58:28', 'confirmed'],
            [7, '2021-06-14 13:59:27', 'confirmed'], [2, '2021-01-22 00:00:00', 'confirmed'],
            [2, '2021-02-28 23:59:59', 'timeout']]
    confirmations = pd.DataFrame(data, columns=['user_id', 'time_stamp', 'action']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'action': 'object'})
    print(confirmation_rate(signups, confirmations))
