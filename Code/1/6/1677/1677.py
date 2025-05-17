#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1677.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 发票中的产品金额。
"""
import pandas as pd


def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    df_merge = product.merge(invoice, on='product_id', how='left').fillna(0)
    df_grp = df_merge.groupby('name')[['rest', 'paid', 'canceled', 'refunded']].sum().reset_index()
    df_sort = df_grp.sort_values(by='name', ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[0, 'ham'], [1, 'bacon']]
    product = pd.DataFrame(data, columns=['product_id', 'name']).astype({'product_id': 'Int64', 'name': 'object'})
    data = [[23, 0, 2, 0, 5, 0], [12, 0, 0, 4, 0, 3], [1, 1, 1, 1, 0, 1], [2, 1, 1, 0, 1, 1], [3, 1, 0, 1, 1, 1],
            [4, 1, 1, 1, 1, 0]]
    invoice = pd.DataFrame(data, columns=['invoice_id', 'product_id', 'rest', 'paid', 'canceled', 'refunded']).astype(
        {'invoice_id': 'Int64', 'product_id': 'Int64', 'rest': 'Int64', 'paid': 'Int64', 'canceled': 'Int64',
         'refunded': 'Int64'})
    print(analyze_products(product, invoice))
