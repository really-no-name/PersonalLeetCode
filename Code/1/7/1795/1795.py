#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1795.py
作者: Bolun Xu
创建日期: 2025/5/8
版本: 1.0
描述: 每个产品在不同商店的价格。
"""
import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products_melted = products.melt(
        id_vars=['product_id'],  # 保持不变的列（产品名称）
        var_name='store',  # 新列名（季度）
        value_name='price'  # 新列名（销售额）
    )
    result_df = products_melted[products_melted['price'].notna()]
    return result_df


if __name__ == '__main__':
    data = [[0, 95, 100, 105], [1, 70, None, 80]]
    products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype(
        {'product_id': 'Int64', 'store1': 'Int64', 'store2': 'Int64', 'store3': 'Int64'})
    print(rearrange_products_table(products))