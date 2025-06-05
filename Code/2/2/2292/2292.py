#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2292.py
作者: Bolun Xu
创建日期: 2025/6/5
版本: 1.0
描述: 连续两年有 3 个及以上订单的产品。
"""
import pandas as pd


def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    # 获取订单年份
    df = orders.copy()
    df['year'] = df['purchase_date'].dt.year

    # 按年和产品计数
    df_grp = df.groupby(['product_id', 'year'])['order_id'].nunique().reset_index(name='cnt')

    # 获取下一年和cnt
    df_grp['next_year'] = df_grp.groupby('product_id')['year'].shift(-1)
    df_grp['next_cnt'] = df_grp.groupby('product_id')['cnt'].shift(-1)
    df_filter = df_grp[~df_grp['next_cnt'].isna()].copy()

    # 计算年份差距
    df_filter['year_diff'] = df_filter['next_year'] - df_filter['year']
    df_filter = df_filter[df_filter['year_diff'] == 1]

    # 筛选 订购三次或三次以上
    df_result = df_filter[(df_filter['cnt'] >= 3) & (df_filter['next_cnt'] >= 3)]

    # 去重返回
    df_drp = df_result[['product_id']].drop_duplicates(keep='first')
    return df_drp


if __name__ == '__main__':
    data = [[1, 1, 7, '2020-03-16'], [2, 1, 4, '2020-12-02'], [3, 1, 7, '2020-05-10'], [4, 1, 6, '2021-12-23'],
            [5, 1, 5, '2021-05-21'], [6, 1, 6, '2021-10-11'], [7, 2, 6, '2022-10-11']]
    orders = pd.DataFrame(data, columns=['order_id', 'product_id', 'quantity', 'purchase_date']).astype(
        {'order_id': 'Int64', 'product_id': 'Int64', 'quantity': 'Int64', 'purchase_date': 'datetime64[ns]'})
    print(find_valid_products(orders))