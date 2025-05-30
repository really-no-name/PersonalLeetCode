#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1867.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 最大数量高于平均水平的订单。
"""
import pandas as pd


def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:
    df = orders_details.copy()
    df = df.groupby(['order_id'])['quantity'].agg(avg='mean', max='max').reset_index()

    # 获取 order_avg_quantity
    max_avg = df['avg'].max()
    df_filter = df[max_avg < df['max']]

    return df_filter[['order_id']]


if __name__ == '__main__':
    data = [[1, 1, 12], [1, 2, 10], [1, 3, 15],
            [2, 1, 8], [2, 4, 4], [2, 5, 6],
            [3, 3, 5], [3, 4, 18], [4, 5, 2],
            [4, 6, 8], [5, 7, 9], [5, 8, 9],
            [3, 9, 20], [2, 9, 4]]
    orders_details = pd.DataFrame(data, columns=['order_id', 'product_id', 'quantity']).astype(
        {'order_id': 'Int64', 'product_id': 'Int64', 'quantity': 'Int64'})
    print(orders_above_average(orders_details))