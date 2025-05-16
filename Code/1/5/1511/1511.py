#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1511.py
作者: Bolun Xu
创建日期: 2025/5/16
版本: 1.0
描述: 消费者下单频率。
"""
import pandas as pd


def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 拼接并计算总消费
    df_merge1 = orders.merge(product, on='product_id', how='left')
    df_merge1['price'] = df_merge1['price'] * df_merge1['quantity']

    # 6月 符合要求的 `customer_id`
    order_June = df_merge1[(df_merge1['order_date'] >= '2020-06-01') & (df_merge1['order_date'] <= '2020-06-30')]
    order_June = order_June.groupby('customer_id')['price'].sum().reset_index()
    customer_June = order_June[order_June['price'] >= 100]['customer_id']

    # 7月 符合要求的 `customer_id`
    order_July = df_merge1[(df_merge1['order_date'] >= '2020-07-01') & (df_merge1['order_date'] <= '2020-07-31')]
    order_July = order_July.groupby('customer_id')['price'].sum().reset_index()
    customer_July = order_July[order_July['price'] >= 100]['customer_id']

    # 筛选`customer_id`同时在6月和7月
    df_filter = customers[(customers['customer_id'].isin(customer_June)) & (customers['customer_id'].isin(customer_July))]
    return df_filter[['customer_id', 'name']]


if __name__ == '__main__':
    data = [[1, 'Winston', 'USA'],
            [2, 'Jonathan', 'Peru'],
            [3, 'Moustafa', 'Egypt']]
    customers = pd.DataFrame(data, columns=['customer_id', 'name', 'country']).astype(
        {'customer_id': 'Int64', 'name': 'object', 'country': 'object'})
    data = [[10, 'LC Phone', 300],
            [20, 'LC T-Shirt', 10],
            [30, 'LC Book', 45],
            [40, 'LC Keychain', 2]]
    product = pd.DataFrame(data, columns=['product_id', 'description', 'price']).astype(
        {'product_id': 'Int64', 'description': 'object', 'price': 'Int64'})
    data = [[1, 1, 10, '2020-06-10', 1],
            [2, 1, 20, '2020-07-01', 1],
            [3, 1, 30, '2020-07-08', 2],
            [4, 2, 10, '2020-06-15', 2],
            [5, 2, 40, '2020-07-01', 10],
            [6, 3, 20, '2020-06-24', 2],
            [7, 3, 30, '2020-06-25', 2],
            [9, 3, 30, '2020-05-08', 3]]
    orders = pd.DataFrame(data, columns=['order_id', 'customer_id', 'product_id', 'order_date', 'quantity']).astype(
        {'order_id': 'Int64', 'customer_id': 'Int64', 'product_id': 'Int64', 'order_date': 'datetime64[ns]',
         'quantity': 'Int64'})
    print(customer_order_frequency(customers, product, orders))