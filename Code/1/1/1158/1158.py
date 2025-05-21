#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1158.py
作者: Bolun Xu
创建日期: 2025/5/21
版本: 1.0
描述: 市场分析 I。
"""
import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_filter = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    orders_grp = orders_filter.groupby('buyer_id')['order_id'].count().reset_index()
    df_merge = users.merge(orders_grp, left_on='user_id', right_on='buyer_id', how='left').fillna(0)
    df_merge = df_merge[['user_id', 'join_date', 'order_id']].rename(columns={'user_id': 'buyer_id', 'order_id': 'orders_in_2019'})
    return df_merge


if __name__ == '__main__':
    data = [[1, '2018-01-01', 'Lenovo'], [2, '2018-02-09', 'Samsung'], [3, '2018-01-19', 'LG'], [4, '2018-05-21', 'HP']]
    users = pd.DataFrame(data, columns=['user_id', 'join_date', 'favorite_brand']).astype(
        {'user_id': 'Int64', 'join_date': 'datetime64[ns]', 'favorite_brand': 'object'})
    data = [[1, '2019-08-01', 4, 1, 2], [2, '2018-08-02', 2, 1, 3], [3, '2019-08-03', 3, 2, 3],
            [4, '2018-08-04', 1, 4, 2], [5, '2018-08-04', 1, 3, 4], [6, '2019-08-05', 2, 2, 4]]
    orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'item_id', 'buyer_id', 'seller_id']).astype(
        {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'item_id': 'Int64', 'buyer_id': 'Int64',
         'seller_id': 'Int64'})
    data = [[1, 'Samsung'], [2, 'Lenovo'], [3, 'LG'], [4, 'HP']]
    items = pd.DataFrame(data, columns=['item_id', 'item_brand']).astype({'item_id': 'Int64', 'item_brand': 'object'})
    print(market_analysis(users, orders, items))