#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1939.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 主动请求确认消息的用户。
"""
import pandas as pd


def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # 将时间戳列转换为 datetime 类型
    # confirmations['time_stamp'] = pd.to_datetime(confirmations['time_stamp'])

    # 按照用户分组，计算两次请求确认消息的时间差，并筛选出在 24 小时窗口内的用户
    result_df = (confirmations.sort_values(['user_id', 'time_stamp'])
    .assign(time_diff=lambda x: x.groupby('user_id')['time_stamp'].diff().dt.total_seconds())
    .query('time_diff <= 86400')
    .drop_duplicates('user_id')[['user_id']])

    return result_df


if __name__ == "__main__":
    data = [[3, '2020-03-21 10:16:13'], [7, '2020-01-04 13:57:59'], [2, '2020-07-29 23:09:44'],
            [6, '2020-12-09 10:39:37']]
    signups = pd.DataFrame(data, columns=['user_id', 'time_stamp']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]'})
    data = [[3, '2021-01-06 03:30:46', 'timeout'],
            [3, '2021-01-06 03:37:45', 'timeout'],
            [7, '2021-06-12 11:57:29', 'confirmed'],
            [7, '2021-06-13 11:57:30', 'confirmed'],
            [2, '2021-01-22 00:00:00', 'confirmed'],
            [2, '2021-01-23 00:00:00', 'timeout'],
            [6, '2021-10-23 14:14:14', 'confirmed'],
            [6, '2021-10-24 14:14:13', 'timeout']]
    confirmations = pd.DataFrame(data, columns=['user_id', 'time_stamp', 'action']).astype(
        {'user_id': 'Int64', 'time_stamp': 'datetime64[ns]', 'action': 'object'})
    print(find_requesting_users(signups, confirmations))