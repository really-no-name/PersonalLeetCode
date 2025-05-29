#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1549.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 每件商品的最新订单。
"""
import pandas as pd


def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    # 根据 product_id 进行分组排序
    df_grp = orders.copy()
    df_grp['rnk'] = df_grp.groupby('product_id')['order_date'].rank(method='dense', ascending=False)

    # 筛选保留最新
    df_filter = df_grp[df_grp['rnk'] == 1]

    # 合并
    df_merge = df_filter.merge(products, on='product_id', how='left')

    # 结果
    df_sort = df_merge[['product_name', 'product_id', 'order_id', 'order_date']] \
        .sort_values(by=['product_name', 'product_id', 'order_id'], ascending=[True, True, True])
    return df_sort


if __name__ == '__main__':
    data = [[1, 'Winston'], [2, 'Jonathan'], [3, 'Annabelle'], [4, 'Marwan'], [5, 'Khaled']]
    customers = pd.DataFrame(data, columns=['customer_id', 'name']).astype({'customer_id': 'Int64', 'name': 'object'})
    data = [[1, '2020-07-31', 1, 1], [2, '2020-7-30', 2, 2], [3, '2020-08-29', 3, 3], [4, '2020-07-29', 4, 1],
            [5, '2020-06-10', 1, 2], [6, '2020-08-01', 2, 1], [7, '2020-08-01', 3, 1], [8, '2020-08-03', 1, 2],
            [9, '2020-08-07', 2, 3], [10, '2020-07-15', 1, 2]]
    orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'customer_id', 'product_id']).astype(
        {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_id': 'Int64', 'product_id': 'Int64'})
    data = [[1, 'keyboard', 120], [2, 'mouse', 80], [3, 'screen', 600], [4, 'hard disk', 450]]
    products = pd.DataFrame(data, columns=['product_id', 'product_name', 'price']).astype(
        {'product_id': 'Int64', 'product_name': 'object', 'price': 'Int64'})
    print(most_recent_orders(customers, orders, products))