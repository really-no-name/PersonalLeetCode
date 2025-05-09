#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1082.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 销售分析 I。
"""
import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df_sum = sales.groupby('seller_id')['price'].sum().reset_index()
    df_sum['rank'] = df_sum['price'].rank(method='dense', ascending=False).astype(int)
    df_filtered = df_sum[df_sum['rank'] == 1]
    return df_filtered[['seller_id']]


if __name__ == '__main__':
    data = [[1, 'S8', 1000],
            [2, 'G4', 800],
            [3, 'iPhone', 1400]]
    product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
        {'product_id': 'Int64',
         'product_name': 'object',
         'unit_price': 'Int64'})
    data = [[1, 1, 1, '2019-01-21', 2, 2000],
            [1, 2, 2, '2019-02-17', 1, 800],
            [2, 2, 3, '2019-06-02', 1, 800],
            [3, 3, 4, '2019-05-13', 2, 2800]]
    sales = pd.DataFrame(data,
                         columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
        {'seller_id': 'Int64',
         'product_id': 'Int64',
         'buyer_id': 'Int64',
         'sale_date': 'datetime64[ns]',
         'quantity': 'Int64',
         'price': 'Int64'})
    print(sales_analysis(product, sales))