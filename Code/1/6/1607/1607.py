#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1607.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 没有卖出的卖家。
"""
import pandas as pd


def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    # 筛选 2020
    orders_filter = orders[(orders['sale_date'] >= '2020-01-01') & (orders['sale_date'] <= '2020-12-31')]
    seller_list = orders_filter['seller_id'].unique()
    seller_filter = seller[~seller['seller_id'].isin(seller_list)]
    df_sort = seller_filter[['seller_name']].sort_values('seller_name', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[101, 'Alice'], [102, 'Bob'], [103, 'Charlie']]
    customer = pd.DataFrame(data, columns=['customer_id', 'customer_name']).astype(
        {'customer_id': 'Int64', 'customer_name': 'object'})
    data = [[1, '2020-03-01', 1500, 101, 1], [2, '2020-05-25', 2400, 102, 2], [3, '2019-05-25', 800, 101, 3],
            [4, '2020-09-13', 1000, 103, 2], [5, '2019-02-11', 700, 101, 2]]
    orders = pd.DataFrame(data, columns=['order_id', 'sale_date', 'order_cost', 'customer_id', 'seller_id']).astype(
        {'order_id': 'Int64', 'sale_date': 'datetime64[ns]', 'order_cost': 'Int64', 'customer_id': 'Int64',
         'seller_id': 'Int64'})
    data = [[1, 'Daniel'], [2, 'Elizabeth'], [3, 'Frank']]
    seller = pd.DataFrame(data, columns=['seller_id', 'seller_name']).astype(
        {'seller_id': 'Int64', 'seller_name': 'object'})
    print(sellers_with_no_sales(customer, orders, seller))