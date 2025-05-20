#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1045.py
作者: Bolun Xu
创建日期: 2025/5/20
版本: 1.0
描述: 买下所有产品的客户。
"""
import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    报告 Customer 表中购买了 Product 表中所有产品的客户的 id
    """
    product_nums = product.shape[0]
    df_grp = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    df_filter = df_grp[df_grp['product_key'] == product_nums][['customer_id']]
    return df_filter


if __name__ == '__main__':
    data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
    customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype(
        {'customer_id': 'Int64', 'product_key': 'Int64'})
    data = [[5], [6]]
    product = pd.DataFrame(data, columns=['product_key']).astype({'product_key': 'Int64'})
    print(find_customers(customer, product))
