#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0586.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 订单最多的客户。
"""
import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df_cnt = orders.groupby('customer_number')['order_number'].count().reset_index()
    df_cnt['rank'] = df_cnt['order_number'].rank(method='dense', ascending=False)
    return df_cnt[df_cnt['rank'] == 1][['customer_number']]


if __name__ == '__main__':
    data = [[1, 1], [2, 2], [3, 3], [4, 3]]
    orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
        {'order_number': 'Int64', 'customer_number': 'Int64'})
    print(largest_orders(orders))