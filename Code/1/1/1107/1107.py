#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1107.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 每日新用户统计。
"""
import pandas as pd


def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    # filter login
    df_filter = traffic[traffic['activity'] == 'login']

    # first login
    df_grp = df_filter.groupby('user_id')['activity_date'].min().reset_index()

    # filter 90 days
    # 原始日期字符串
    date_str = '2019-06-30'
    # 转换为 datetime 并减去 90 天
    date_lim = pd.to_datetime(date_str) - pd.Timedelta(days=90)
    df_filter2 = df_grp[df_grp['activity_date'] >= date_lim]

    df_grp2 = df_filter2.groupby('activity_date')['user_id'].nunique().reset_index()
    df_grp2 = df_grp2.rename(columns={'activity_date': 'login_date', 'user_id': 'user_count'})
    return df_grp2


if __name__ == '__main__':
    data = [[1, 'login', '2019-05-01'], [1, 'homepage', '2019-05-01'], [1, 'logout', '2019-05-01'],
            [2, 'login', '2019-06-21'], [2, 'logout', '2019-06-21'], [3, 'login', '2019-01-01'],
            [3, 'jobs', '2019-01-01'], [3, 'logout', '2019-01-01'], [4, 'login', '2019-06-21'],
            [4, 'groups', '2019-06-21'], [4, 'logout', '2019-06-21'], [5, 'login', '2019-03-01'],
            [5, 'logout', '2019-03-01'], [5, 'login', '2019-06-21'], [5, 'logout', '2019-06-21']]
    traffic = pd.DataFrame(data, columns=['user_id', 'activity', 'activity_date']).astype(
        {'user_id': 'Int64', 'activity': 'object', 'activity_date': 'datetime64[ns]'})
    print(new_users_daily_count(traffic))