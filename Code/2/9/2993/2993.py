#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2993.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 发生在周五的交易 I。
"""
import pandas as pd


def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    df_sum = purchases.groupby('purchase_date')['amount_spend'].sum().reset_index()

    df_sum['weekday'] = df_sum['purchase_date'].dt.day_name()
    df_filt = df_sum[df_sum['weekday'] == 'Friday']

    # 计算该月的第几周（从1开始）
    df_filt['week_of_month'] = (df_filt['purchase_date'].dt.day - 1) // 7 + 1
    del df_filt['weekday']
    df_sort = df_filt.sort_values(by='week_of_month')
    result_df = df_sort[['week_of_month', 'purchase_date', 'amount_spend']]
    result_df = result_df.rename(columns={'amount_spend': 'total_amount'})
    return result_df


if __name__ == '__main__':
    data = [[11, '2023-11-07', 1126],
            [15, '2023-11-30', 7473],
            [17, '2023-11-14', 2414],
            [12, '2023-11-24', 9692],
            [8, '2023-11-03', 5117],
            [1, '2023-11-16', 5241],
            [10, '2023-11-12', 8266],
            [13, '2023-11-24', 12000]]
    purchases = pd.DataFrame(data, columns=['user_id', 'purchase_date', 'amount_spend']).astype(
        {'user_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'amount_spend': 'Int64'})
    print(friday_purchases(purchases))