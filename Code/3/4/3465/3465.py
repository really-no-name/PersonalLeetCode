#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3465.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 查找具有有效序列号的产品。
"""
import pandas as pd


def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    pattern = r'\bSN\d{4}-\d{4}\b'  # 正则
    df_filter = products[products['description'].str.contains(pattern,  regex=True, na=False)]
    df_sort = df_filter.sort_values(by=['product_id'], ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [[1, 'Widget A', 'This is a sample product with SN1234-5678'],
            [2, 'Widget B', 'A product with serial SN9876-1234 in the description'],
            [3, 'Widget C', 'Product SN1234-56789 is available now'],
            [4, 'Widget D', 'No serial number here'],
            [5, 'Widget E', 'Check out SN4321-8765 in this description']]
    products = pd.DataFrame(data, columns=['product_id', 'product_name', 'description']).astype(
        {'product_id': 'int32', 'product_name': 'string', 'description': 'string'})
    print(find_valid_serial_products(products))
