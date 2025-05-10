#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1565.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 按月统计订单数与顾客数。
"""
import pandas as pd


def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_month'] = orders['order_date'].dt.strftime('%Y-%m')
    df_flitered = orders[orders['invoice'] > 20]
    order_cnt = df_flitered.groupby('order_month')['order_id'].nunique().reset_index()
    customer_cnt = df_flitered.groupby('order_month')['customer_id'].nunique().reset_index()
    df_merged = pd.merge(order_cnt, customer_cnt, on='order_month')
    df_merged = df_merged.rename(columns={'order_month': 'month', 'order_id': 'order_count', 'customer_id': 'customer_count'})
    return df_merged


if __name__ == '__main__':
    data = [[1, '2020-09-15', 1, 30],
            [2, '2020-09-17', 2, 90],
            [3, '2020-10-06', 3, 20],
            [4, '2020-10-20', 3, 21],
            [5, '2020-11-10', 1, 10],
            [6, '2020-11-21', 2, 15],
            [7, '2020-12-01', 4, 55],
            [8, '2020-12-03', 4, 77],
            [9, '2021-01-07', 3, 31],
            [10, '2021-01-15', 2, 20]]
    orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'customer_id', 'invoice']).astype(
        {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'invoice': 'Int64'})
    print(unique_orders_and_customers(orders))