#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3220.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 奇数和偶数交易。
"""
import pandas as pd


def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    df_cnt1 = transactions[transactions['amount'] % 2 == 0] \
        .groupby('transaction_date')['amount'].sum().reset_index(name='even_sum')
    df_cnt2 = transactions[transactions['amount'] % 2 == 1] \
        .groupby('transaction_date')['amount'].sum().reset_index(name='odd_sum')

    df_merge = pd.merge(df_cnt2, df_cnt1, on='transaction_date', how='outer').fillna(0)

    df_sort = df_merge.sort_values('transaction_date', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[1, 150, '2024-07-01'], [2, 200, '2024-07-01'], [3, 75, '2024-07-01'], [4, 300, '2024-07-02'],
            [5, 50, '2024-07-02'], [6, 120, '2024-07-03']]
    transactions = pd.DataFrame(data,
        columns=["transaction_id", "amount", "transaction_date"]).astype({
        "transaction_id": "int", "amount": "int", "transaction_date": "datetime64[ns]"})
    print(sum_daily_odd_even(transactions))
