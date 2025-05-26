#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1398.py
作者: Bolun Xu
创建日期: 2025/5/26
版本: 1.0
描述: 购买了产品 A 和产品 B 却没有购买产品 C 的顾客。
"""
import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 对数据进行重构 数据透视（行列转换）
    df_orders = orders.copy()
    df_orders['is'] = 1
    # 确保包含A、B、C三列，即使原始数据中没有某些产品
    df_orders_pivot = df_orders.pivot_table(
        index='customer_id',
        columns='product_name',
        values='is',
        fill_value=0
    ).reindex(columns=['A', 'B', 'C'], fill_value=0).reset_index()

    # 筛选 购买 AB 没买 C
    condition = ((df_orders_pivot['A'] == 1) &
                 (df_orders_pivot['B'] == 1) &
                 (df_orders_pivot['C'] == 0))
    df_filter = df_orders_pivot[condition]

    # 合并查找 name
    df_merge = df_filter[['customer_id']].merge(customers, on='customer_id', how='left')
    df_sort = df_merge.sort_values(by=['customer_id'], ascending=True)
    return df_sort



if __name__ == '__main__':
    data = [[1, 'Daniel'], [2, 'Diana'], [3, 'Elizabeth'], [4, 'Jhon']]
    customers = pd.DataFrame(data, columns=['customer_id', 'customer_name']).astype(
        {'customer_id': 'Int64', 'customer_name': 'object'})
    data = [[10, 1, 'A'], [20, 1, 'B'], [30, 1, 'D'], [40, 1, 'C'], [50, 2, 'A'], [60, 3, 'A'], [70, 3, 'B'],
            [80, 3, 'D'], [90, 4, 'C']]
    orders = pd.DataFrame(data, columns=['order_id', 'customer_id', 'product_name']).astype(
        {'order_id': 'Int64', 'customer_id': 'Int64', 'product_name': 'object'})
    print(find_customers(customers, orders))