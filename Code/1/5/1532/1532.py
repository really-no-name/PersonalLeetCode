#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1532.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 最近的三笔订单。
"""
import pandas as pd


def recent_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_order =orders.copy()
    # 分组 排序
    df_order['rank'] = df_order.groupby('customer_id')['order_date'].rank(method='first', ascending=False)

    # 保留 后3个
    df_filter = df_order[df_order['rank'] < 4]

    # 合并 排序
    df_merge = df_filter.merge(customers, on='customer_id', how='left')
    df_sort = df_merge.sort_values(by=['name', 'customer_id', 'order_date'], ascending=[True, True, False])

    df_result = df_sort[['name', 'customer_id', 'order_id', 'order_date']].rename(columns={'name': 'customer_name'})
    return df_result


if __name__ == '__main__':
    data = [[1, 'Winston'], [2, 'Jonathan'], [3, 'Annabelle'], [4, 'Marwan'], [5, 'Khaled']]
    customers = pd.DataFrame(data, columns=['customer_id', 'name']).astype({'customer_id': 'Int64', 'name': 'object'})
    data = [[1, '2020-07-31', 1, 30], [2, '2020-7-30', 2, 40], [3, '2020-07-31', 3, 70], [4, '2020-07-29', 4, 100],
            [5, '2020-06-10', 1, 1010], [6, '2020-08-01', 2, 102], [7, '2020-08-01', 3, 111], [8, '2020-08-03', 1, 99],
            [9, '2020-08-07', 2, 32], [10, '2020-07-15', 1, 2]]
    orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'customer_id', 'cost']).astype(
        {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'cost': 'Int64'})
    print(recent_three_orders(customers, orders))