#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1831.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 每天的最大交易。
"""
import pandas as pd


def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    # 提取日期部分
    df['day'] = pd.to_datetime(df['day']).dt.date
    # 分组排序
    df['rank'] = df.groupby('day')['amount'].rank(method='dense', ascending=False)

    # 筛选最高
    df_filter = df[df['rank'] == 1][['transaction_id']]

    # 排序
    df_sort = df_filter.sort_values(by=['transaction_id'], ascending=True)

    return df_sort


if __name__ == '__main__':
    data = [[8, '2021-4-3 15:57:28', 57], [9, '2021-4-28 08:47:25', 21], [1, '2021-4-29 13:28:30', 58],
            [5, '2021-4-28 16:39:59', 40], [6, '2021-4-29 23:39:28', 58]]
    transactions = pd.DataFrame(data, columns=['transaction_id', 'day', 'amount']).astype(
        {'transaction_id': 'Int64', 'day': 'datetime64[ns]', 'amount': 'Int64'})
    print(find_maximum_transaction(transactions))