#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3293.py
作者: Bolun Xu
创建日期: 2025/5/7
版本: 1.0
描述: 计算产品最终价格。
"""
import pandas as pd


def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    merged_df = products.merge(discounts, on='category', how='left').fillna(0)
    merged_df['final_price'] = merged_df['price'] * (100 - merged_df['discount']) / 100
    return merged_df[['product_id', 'final_price', 'category']]


if __name__ == '__main__':
    data = [[1, 'Electronics', 1000], [2, 'Clothing', 50], [3, 'Electronics', 1200], [4, 'Home', 500]]
    products = pd.DataFrame(data, columns=['product_id', 'category', 'price']).astype(
        {'product_id': int, 'category': str, 'price': float})

    data = [['Electronics', 10], ['Clothing', 20]]
    discounts = pd.DataFrame(data, columns=['category', 'discount']).astype({'category': str, 'discount': int})

    print(calculate_final_prices(products, discounts))