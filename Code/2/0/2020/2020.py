#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2020.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 无流量的帐户数。
"""
import pandas as pd


def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    # 筛选2021年有订阅的账户
    subscriptions_2021 = subscriptions[
        ((subscriptions['start_date'].dt.year == 2021) |
         (subscriptions['end_date'].dt.year == 2021)) |
        ((subscriptions['start_date'] <= '2021-12-31') &
         (subscriptions['end_date'] >= '2021-01-01'))
        ]

    # 筛选2021年有会话的账户
    streams_2021 = streams[streams['stream_date'].dt.year == 2021]

    # 找出2021年有订阅但没有会话的账户
    no_streams = subscriptions_2021[
        ~subscriptions_2021['account_id'].isin(streams_2021['account_id'])
    ]

    # 统计数量
    accounts_count = len(no_streams['account_id'].unique())

    # 返回结果
    return pd.DataFrame({'accounts_count': [accounts_count]})


if __name__ == "__main__":
    data = [[9, '2020-02-18', '2021-10-30'], [3, '2021-09-21', '2021-11-13'], [11, '2020-02-28', '2020-08-18'],
            [13, '2021-04-20', '2021-09-22'], [4, '2020-10-26', '2021-05-08'], [5, '2020-09-11', '2021-01-17']]
    subscriptions = pd.DataFrame(data, columns=['account_id', 'start_date', 'end_date']).astype(
        {'account_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]'})
    data = [[14, 9, '2020-05-16'], [16, 3, '2021-10-27'], [18, 11, '2020-04-29'], [17, 13, '2021-08-08'],
            [19, 4, '2020-12-31'], [13, 5, '2021-01-05']]
    streams = pd.DataFrame(data, columns=['session_id', 'account_id', 'stream_date']).astype(
        {'session_id': 'Int64', 'account_id': 'Int64', 'stream_date': 'datetime64[ns]'})
    print(find_target_accounts(subscriptions, streams))