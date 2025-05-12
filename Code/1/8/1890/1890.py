#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1890.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 2020年最后一次登录。
"""
import pandas as pd


def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins['year'] = logins['time_stamp'].dt.strftime('%Y')
    df_fllt = logins[logins['year'] == '2020']
    df_sort = df_fllt.sort_values('time_stamp', ascending=False)
    df = df_sort.drop_duplicates(subset=['user_id'], keep='first')
    df = df[['user_id', 'time_stamp']].rename(columns={'time_stamp': 'last_stamp'})
    return df


if __name__ == '__main__':
    data = [[6, '2020-06-30 15:06:07'],
            [6, '2021-04-21 14:06:06'],
            [6, '2019-03-07 00:18:15'],
            [8, '2020-02-01 05:10:53'],
            [8, '2020-12-30 00:46:50'],
            [2, '2020-01-16 02:49:50'],
            [2, '2019-08-25 07:59:08'],
            [14, '2019-07-14 09:00:00'],
            [14, '2021-01-06 11:59:59']]
    logins = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
    print(latest_login(logins))